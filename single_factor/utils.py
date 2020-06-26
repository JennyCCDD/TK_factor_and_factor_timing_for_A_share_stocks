# -*- coding: utf-8 -*-

__author__ = "Mengxuan Chen"
__email__  = "chenmx19@mails.tsinghua.edu.cn"
__date__   = "20191130"

#--* pakages*--
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from datetime import datetime

# function for size weighted portfolio calculation
def weightmeanFun(df):
    df['weight'] = df['Size'] / df['Size'].sum()
    df.loc[:, 'RETmWeight'] = df.loc[:, 'RET'] * df.loc[:, 'weight']
    df.loc[:, 'RETmWeight_'] = df['RETmWeight'].sum()
    df.drop_duplicates(subset='RETmWeight_', keep='last', inplace=True)
    df = df.loc[:, 'RETmWeight_']
    size_weight_mean = np.array(df)[0]
    return size_weight_mean

# 定义一个函数使得股票无法对齐时，df1的股票column与df2保持一致
def stock_dif(df1,df2):
    column_num = len(df2.index)
    df_merge = pd.DataFrame(columns=df2.index, index=df2.columns)
    dff = pd.merge(df1.T, df_merge, how='inner', left_index=True, right_index=True)
    dff = pd.merge(dff, df_merge, how='outer', left_index=True, right_index=True)
    dff = dff.iloc[:, :-column_num]
    dff = dff.dropna(how='all', axis=1)
    dff = dff.T
    dff.index = df2.index
    return dff

def basic_data(para):
    ################################# 处理好的后后复权价格，用于计算月度收益率数据 3847支股票
    Price = pd.read_hdf(
    para.dataPathPrefix + '\DataBase\Data_AShareEODPrices\BasicDailyFactor_StockForwardClosePrice.h5')

    ################################# 涨跌停数据：1表示是涨停，-1表示跌停，0表示非涨跌停
    UpDownLimitStatus = pd.read_hdf(
    para.dataPathPrefix + '\DataBase\Data_AShareEODPrices\BasicDailyFactor_UpDownLimitStatus.h5')
    LimitStatus = UpDownLimitStatus.loc[para.startDate:para.endDate, :]

    ################################# ST/ST*数据： 1表示正常
    StockTradeStatus = pd.read_hdf(
    para.dataPathPrefix + '\DataBase\Data_AShareTradeStatus\BasicDailyFactor_StockTradeStatus.h5')
    Status = StockTradeStatus.loc[para.startDate:para.endDate, :]

    ############################### 过去交易的天数
    StockListDateNum = pd.read_hdf(
    para.dataPathPrefix + '\DataBase\Data_AShareDescription\BasicDailyFactor_StockListDateNum.h5')
    listDateNum = StockListDateNum.loc[para.startDate:para.endDate, :]

    ################################# 行业分类数据
    Data_AShareIndustryClass = pd.read_hdf(
    para.dataPathPrefix + '\DataBase\Data_AShareIndustryClass\AShareIndustriesClassCITICSNew_FirstIndustries.h5')
    Industry = Data_AShareIndustryClass.loc[para.startDate:para.endDate, :]
    Industry = stock_dif(Industry, LimitStatus)
    Industry.index = LimitStatus.index

    ################################# A股总市值
    StockTotalMV = pd.read_hdf(
    para.dataPathPrefix + '\DataBase\Data_AShareEODDerivativeIndicator\BasicDailyFactor_StockTotalMV.h5')
    Size = StockTotalMV.loc[para.startDate:para.endDate, :]
    Size = stock_dif(Size, LimitStatus)
    Size.index = LimitStatus.index
    return Price,LimitStatus,Status,listDateNum,Industry,Size

def performance(strategy,para):
    rety = (strategy.nav[strategy.index[-1]] / strategy.nav[strategy.index[0]]) ** (12 / strategy.shape[0]) - 1
    STD = np.std(strategy.ret) * np.sqrt(12)
    Sharp = rety / STD
    DD = 1 - strategy.nav / strategy.nav.cummax()
    MDD = max(DD)
    def Reward_to_VaR(s, alpha=0.99):
        RET = s.pct_change(1).fillna(0)
        sorted_Returns = np.sort(RET)
        index = int(alpha * len(sorted_Returns))
        var = abs(sorted_Returns[index])
        RtoVaR = np.average(RET) / var
        return -RtoVaR
    R2VaR = Reward_to_VaR(strategy.nav)
    def Reward_to_CVaR(s, alpha=0.99):
        RET = s.pct_change(1).fillna(0)
        sorted_Returns = np.sort(RET)
        index = int(alpha * len(sorted_Returns))
        sum_var = sorted_Returns[0]
        for i in range(1, index):
            sum_var += sorted_Returns[i]
            CVaR = abs(sum_var / index)
        RtoCVaR = np.average(RET) / CVaR
        return -RtoCVaR
    R2CVaR = Reward_to_CVaR(strategy.nav)

    result = {'Sharp': Sharp,
              'RetYearly': rety,
              'STD':STD,
              'MDD': MDD,
              'R2VaR':R2VaR,
              'R2CVaR':R2CVaR }
    result = pd.DataFrame.from_dict(result, orient='index').T
    # print(result.T)
    return result


# define the function to calculate the performance of the strategy for each year
# take a year as 252 days
def performance_anl(strategy, para):
    def MaxDrawdown(return_list):
        RET_ACC = []
        sum = 1
        for i in range(len(return_list)):
            sum = sum * (return_list[i] + 1)
            RET_ACC.append(sum)
        index_j = np.argmax(np.array((np.maximum.accumulate(RET_ACC) - RET_ACC) / np.maximum.accumulate(RET_ACC)))
        index_i = np.argmax(RET_ACC[:index_j])
        MDD = (RET_ACC[index_i] - RET_ACC[index_j]) / RET_ACC[index_i]
        return sum, MDD, RET_ACC

    """def MaxDrawdown2(return_list):
        value = (1 + return_list).cumprod()
        MDD = ffn.calc_max_drawdown(value)
        return -MDD"""

    def Reward_to_VaR(strategy=strategy, alpha=0.99):
        RET = strategy.nav.pct_change(1).fillna(0)
        sorted_Returns = np.sort(RET)
        index = int(alpha * len(sorted_Returns))
        var = abs(sorted_Returns[index])
        RtoVaR = np.average(RET) / var
        return -RtoVaR

    def Reward_to_CVaR(strategy=strategy, alpha=0.99):
        RET = strategy.nav.pct_change(1).fillna(0)
        sorted_Returns = np.sort(RET)
        index = int(alpha * len(sorted_Returns))
        sum_var = sorted_Returns[0]
        for i in range(1, index):
            sum_var += sorted_Returns[i]
            CVaR = abs(sum_var / index)
        RtoCVaR = np.average(RET) / CVaR
        return -RtoCVaR

    strategy['Y'] = strategy.index
    strategy['Y'] = strategy['Y'].apply(lambda x: datetime.strptime(str(x), "%Y%m%d"))
    strategy['Y'] = strategy.Y.apply(lambda x: x.year)
    n_year = strategy['Y'].value_counts()
    n_year_index = n_year.index.sort_values()
    RET_list = []
    T_list = []
    STD_list = []
    MDD_list = []
    ACC_list = []
    SHARP_list = []
    R2VaR_list = []
    R2CVaR_list = []
    for i in n_year_index:
        x = strategy.loc[strategy['Y'] == i]
        ts = x.nav.pct_change(1).fillna(0)
        RET = (x.nav[x.index[-1]] / x.nav[x.index[0]]) ** (12 / x.shape[0]) - 1
        T = stats.ttest_1samp(ts, 0)[0]
        STD = np.std(ts) * np.sqrt(252)
        MDD = MaxDrawdown(ts)[1]
        # MDD = MaxDrawdown2(ts)
        ACC = MaxDrawdown(ts)[0]
        SHARP = (RET - 0.03) / STD
        R2VaR = Reward_to_VaR(x)
        R2CVaR = Reward_to_CVaR(x)
        RET_list.append(RET)
        T_list.append(T)
        STD_list.append(STD)
        MDD_list.append(MDD)
        ACC_list.append(ACC)
        SHARP_list.append(SHARP)
        R2VaR_list.append(R2VaR)
        R2CVaR_list.append(R2CVaR)
    RET_df = pd.DataFrame(RET_list)
    RET_df.columns = {'RET'}
    T_df = pd.DataFrame(T_list)
    T_df.columns = {'T'}
    STD_df = pd.DataFrame(STD_list)
    STD_df.columns = {'STD'}
    MDD_df = pd.DataFrame(MDD_list)
    MDD_df.columns = {'MDD'}
    ACC_df = pd.DataFrame(ACC_list)
    ACC_df.columns = {'ACC'}
    SHARP_df = pd.DataFrame(SHARP_list)
    SHARP_df.columns = {'SHARP'}
    R2VaR_df = pd.DataFrame(R2VaR_list)
    R2VaR_df.columns = {'R2VaR'}
    R2CVaR_df = pd.DataFrame(R2CVaR_list)
    R2CVaR_df.columns = {'R2CVaR'}
    P = pd.concat([RET_df, T_df, STD_df, MDD_df, ACC_df, SHARP_df, R2VaR_df, R2CVaR_df], axis=1, ignore_index=False)
    P.index = n_year_index
    print(P)
    P.to_csv(para.path_results+'P.csv')
    return P

