# -*- coding: utf-8 -*-
__author__ = "Mengxuan Chen"
__email__  = "chenmx19@mails.tsinghua.edu.cn"
__date__   = "20200601-20200622"


import numpy as np
import pandas as pd
from tqdm import tqdm
from scipy.stats import spearmanr
from getTradingDate import getTradingDateFromJY
from utils import weightmeanFun, basic_data, stock_dif, performance, performance_anl
from datareader import loadData
import matplotlib.pyplot as plt
import matplotlib.dates as mdate
import warnings
from MAC_RP import withoutboundary
from datetime import datetime
warnings.filterwarnings('ignore')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

class Para():
    startDate = 20091231
    endDate = 20200508
    groupnum = 10
    weightMethod = '市值加权'
    # ['简单加权', '市值加权',  'MAC', 'RP']
    ret_calMethod = '简单'
    # ['简单','对数']
    factor = '半衰IC加权_Factor_shrink_10'
    '''
    [
    '等权重_Factor',
    'IC均值加权_Factor', 
    'ICIR加权_Factor',  
    '最大化IR加权_Factor', 
    '半衰IC加权_Factor'
    ]
    '''
    data_path = '.\\data\\'
    result_path = '.\\result\\'
    listnum = 121 # for stock sample at least be listed for listnum of days
    backtestwindow = 60 # number of days used to form portfolios
    fin_stock = 'no' # include finnacial stock or not
    dataPathPrefix = 'D:\caitong_security'
    pass
para = Para()

class SingleFactor():
    def __init__(self,para):
        # get trading date list as monthly frequancy
        self.tradingDateList = getTradingDateFromJY(para.startDate,
                                                    para.endDate,
                                                    ifTrade=True,
                                                    Period='M')
        self.Price, self.LimitStatus, self.Status, self.listDateNum, self.Industry, self.Size = basic_data(para)
        self.Factor = pd.read_csv(para.result_path+para.factor+'.csv',index_col=0)
        pass

    def DES(self):
        Des = pd.DataFrame(self.Factor.describe())
        Des['all'] = Des.apply(lambda x: x.sum(), axis = 1)
        return Des['all']

    def every_month(self):
        # deal with the data every month
        self.Price = self.Price.loc[para.startDate:para.endDate, :]
        meanlist = []
        corr_list = []
        for i,currentDate in enumerate(tqdm(self.tradingDateList[:-1])):
            # get lastDate for corresponding time frequancy(for return calculation)
            lastDate = self.tradingDateList[self.tradingDateList.index(currentDate) - 1]

            # use different method to calculate the return
            # logreturn for short time period and simple return calculation for long time period
            if para.ret_calMethod == '对数':
                self.ret = np.log(self.Price.loc[currentDate,:]/self.Price.loc[lastDate,:])
            elif para.ret_calMethod == '简单':
                self.ret = self.Price.loc[currentDate, :] / self.Price.loc[lastDate, :] - 1

            # set the basid dataFrame for each cross-section
            # index is the totle stock list
            self.dataFrame = pd.concat([self.Factor.loc[currentDate,:],
                                       self.ret,
                                       self.LimitStatus.loc[currentDate,:],
                                       self.Status.loc[currentDate,:],
                                       self.listDateNum.loc[currentDate,:],
                                       self.Industry.loc[currentDate,:],
                                       self.Size.loc[currentDate,:]],
                                       axis=1, sort=True)
            self.dataFrame = self.dataFrame.reset_index()
            self.dataFrame.columns = ['stockid',
                                     'factor',
                                     'RET',
                                     'LimitStatus',
                                     'Status',
                                     'listDateNum',
                                     'Industry',
                                     'Size']

            # drop NaN and unwanted stocks
            self.dataFrame = self.dataFrame.dropna()
            # get the normal trading stocks
            self.dataFrame = self.dataFrame.loc[self.dataFrame['LimitStatus'] == 0]
            # get not ST/ST*/dropped out stocks
            self.dataFrame = self.dataFrame.loc[self.dataFrame['Status'] == 1]
            # get listed number of days is over para.listnum stocks
            self.dataFrame = self.dataFrame.loc[self.dataFrame['listDateNum'] >= para.listnum]
            # determine if we want financial stocks(codes = 41)
            if para.fin_stock == 'no':
                self.dataFrame = self.dataFrame.loc[self.dataFrame['Industry'] != 41]

            # get the ranking score of single factor
            # the ranking is decending rank
            self.dataFrame = self.dataFrame.sort_values(by = 'factor', ascending = False)
            self.Des = self.dataFrame['factor'].describe()

            # calculate spearman rank correlation
            corr, t = spearmanr(
                self.dataFrame.loc[:, 'factor'],
                self.dataFrame.loc[:, 'RET'])
            corr_list.append(corr)

            # FIRST, give the stocks scores
            self.dataFrame['Score'] = ''
            # eachgroup is the number of stocks in each group
            eachgroup = int(self.Des['count'] / para.groupnum)
            # give the group0 to group (i-1) scores
            for groupi in range(0, para.groupnum - 1):
                self.dataFrame.iloc[groupi * eachgroup:
                                    (groupi+1) * eachgroup,
                                    -1] = groupi + 1
            # give the final group score
            self.dataFrame.iloc[(para.groupnum - 1) * eachgroup:, -1] = para.groupnum

            # HERE is four ways of weights calculation for the stocks in the portfolio
            self.dataFrame['Score'].type = np.str
            # simple average weights
            if para.weightMethod == '简单加权':
                meanlist.append(np.array(self.dataFrame.groupby('Score')['RET'].mean()))
            # weights according to the size( market value of the stocks)
            elif para.weightMethod == '市值加权':
                meanlist_group = []
                for groupi in range(0,para.groupnum):
                    dataFrame_ = self.dataFrame.iloc[groupi * eachgroup:(groupi + 1) * eachgroup, :]
                    meanlist_g = weightmeanFun(dataFrame_)
                    meanlist_group.append(meanlist_g)
                meanlist.append(meanlist_group)

            # weights according to risk control method
            # MAC：Markovitz Mean-Variance Model
            # RP: risk parity
            # https://blog.csdn.net/weixin_42294255/article/details/103836548
            elif para.weightMethod == 'MAC' or 'RP':
                nextDate = self.tradingDateList[self.tradingDateList.index(currentDate) + 1]
                NAV = self.Price.loc[:nextDate,:]

                meanlist_group = []
                for groupi in range(1, para.groupnum + 1):
                    data_ = self.dataFrame.loc[self.dataFrame['Score'] == groupi]
                    data_ = data_.set_index('stockid')
                    data_nav = pd.merge(data_, NAV.T, how = 'inner',left_index = True,right_index = True)
                    ret = data_nav['RET']
                    data_nav = data_nav.drop(columns=['factor',
                                                      'RET',
                                                      'Status',
                                                      'listDateNum',
                                                      'LimitStatus',
                                                      'Industry',
                                                      'Size',
                                                      'Score'])
                    data_nav = data_nav.T
                    data_nav['date'] = data_nav.index.copy()
                    data_nav['date'] = data_nav['date'].apply(lambda x: str(x))
                    data_nav['date'] = data_nav['date'].apply(lambda x: datetime.strptime(str(x), '%Y%m%d'))
                    data_nav = data_nav.set_index('date')
                    weights = withoutboundary(data_nav, period = 1, rollingtime = 21,
                                                   method = para.weightMethod)
                    menlist_g = np.sum(np.array(weights) * np.array(ret))
                    # append all of the groups
                    meanlist_group.append(menlist_g)

                # append all of the days
                meanlist.append(meanlist_group)

        # self.meanDf is the portfolio monthly return timeseries list for each group
        self.meanDf = pd.DataFrame(meanlist,index = self.tradingDateList[:-1])
        self.corr_avg = np.mean(corr_list)
        print('RankIC', round(self.corr_avg, 6))
        return self.meanDf


    def portfolio_test(self):
        # portfolio_test function is to calculate the index of the porfolio
        # https://blog.csdn.net/weixin_42294255/article/details/103836548
        sharp_list = []
        ret_list = []
        std_list = []
        mdd_list = []
        r2var_list = []
        cr2var_list = []
        compare= pd.DataFrame()
        for oneleg in tqdm(range(len(self.meanDf.columns))):
            portfolioDF = pd.DataFrame()
            portfolioDF['ret'] = self.meanDf.iloc[:,oneleg]
            portfolioDF['nav'] = (portfolioDF['ret']+1).cumprod()
            performance_df = performance(portfolioDF,para)
            # performance_df_anl = performance_anl(portfolioDF,para)
            sharp_list.append(np.array(performance_df.iloc[:,0].T)[0])
            ret_list.append(np.array(performance_df.iloc[:,1].T)[0])
            std_list.append(np.array(performance_df.iloc[:,2].T)[0])
            mdd_list.append(np.array(performance_df.iloc[:,3].T)[0])
            r2var_list.append(np.array(performance_df.iloc[:,4].T)[0])
            cr2var_list.append(np.array(performance_df.iloc[:,5].T)[0])
            compare[str(oneleg)] = portfolioDF['nav']
        performanceDf = pd.concat([pd.Series(sharp_list),
                                   pd.Series(ret_list),
                                   pd.Series(std_list),
                                   pd.Series(mdd_list),
                                   pd.Series(r2var_list),
                                   pd.Series(cr2var_list)],
                                    axis = 1, sort = True)
        performanceDf.columns = ['Sharp',
                                 'RetYearly',
                                 'STD',
                                 'MDD',
                                 'R2VaR',
                                 'R2CVaR']
        compare.index = self.meanDf.index
        plt.plot(range(len(compare.iloc[1:, 1])),
                 compare.iloc[1:, :])
        plt.title(para.factor)
        plt.xticks([0, 25, 50, 75, 100, 125],
                   ['2009/12/31', '2011/01/31', '2013/02/28', '2015/03/31', '2017/04/30', '2020/04/30'])
        plt.grid(True)
        plt.xlim((0, 125))
        plt.legend()
        plt.savefig(para.result_path + para.factor +'_' + para.weightMethod + '_performance_nav.png')
        plt.show()
        return performanceDf,compare

if __name__ == "__main__":
    para = Para()
    main_fun = SingleFactor(para)
    des = main_fun.DES()
    result = main_fun.every_month()
    print(result)
    result.to_csv(para.result_path+'_' + para.factor +'_' + para.weightMethod +'_result.csv')
    test, test_nav = main_fun.portfolio_test()
    print(test)
    test.to_csv(para.result_path +'_'+ para.factor +'_' + para.weightMethod +'_performance.csv')