# -*- coding: utf-8 -*-
__author__ = "Mengxuan Chen"
__email__  = "chenmx19@mails.tsinghua.edu.cn"
__date__   = "20200527-20200623"

# This is to test different factor synthesis method
# based on factor_list

import numpy as np
import pandas as pd
from tqdm import tqdm
from scipy.stats import spearmanr
from getTradingDate import getTradingDateFromJY
from utils import weightmeanFun, basic_data, stock_dif, performance, performance_anl
from datareader import loadData
import matplotlib.pyplot as plt
import matplotlib.dates as mdate
from sklearn.covariance import LedoitWolf
import warnings
warnings.filterwarnings('ignore')

class Para():
    startDate = 20091231
    endDate = 20200508
    groupnum = 10
    ret_calMethod = '简单' # 对数
    synthesis_Method = ['等权重' ,
                        'IC均值加权',
                        'ICIR加权',
                        '最大化IR加权',
                        '半衰IC加权']
    data_path = '.\\data\\'
    result_path = '.\\result\\'
    listnum = 121 # for stock sample at least be listed for listnum of days
    backtestwindow = 60 # number of days used to form portfolios
    fin_stock = 'no' # include finnacial stock or not
    dataPathPrefix = 'D:\caitong_security'
    shrink_weight = 1 / 5
    factorlist = [
        'Beta252',
        'GPOA',
        'GPOAQ',
        'GrossProfitMargin',
        'GrossProfitMarginQ',
        'NetProfitMargin',
        'NetProfitMarginQ',
        'ROA',
        'ROAQ',
        'ROE_Diluted',
        'ROE_DilutedQ',
        'ROE_ExDiluted',
        'ROE_ExDilutedQ',
        # 'SUE',##################################
        # 'SUR',##################################
        'GGPOAQ',
        'GGrossProfitMarginQ',
        'GROAQ',
        'GROEQ',
        'NetOperateCashFlowQYOY',
        'NetProfitQYOY',
        'OperatingRevenueQYOY',
        'BLEV',
        'DTOA',
        'MLEV',
        'AmihudILLIQ',
        'TurnOver_1M',
        'TurnOver_1Y',
        'TurnOver_3M',
        'TurnOver_6M',
        'VSTD_1M',
        'VSTD_3M',
        'VSTD_6M',
        'MaxRet21',
        'MinRet21',
        'Ret21',
        'Ret63',
        'Ret126',
        'Ret252_21',
        # 'LnNegotiableMV',###############################
        'LnTotalMV',
        'NegotiableMV',
        # 'NegotiableMVNL',################################
        'TotalMV',
        'TotalMVNL',
        'IMFFFactorNoAlpha',
        'APBFactor_1M',
        'APBFactor_5D',
        'AssetsTurn',
        'CFO',
        'CurrentRatio',
        'NetProfitCashCover',
        'QualityFactor',
        'QualityIncrease',
        'BP',
        'DividendRatioTTM',
        'EPTTM',
        'NCFPTTM',
        'OCFPTTM',
        ######################### 缺少这个因子的数据 'EPCut',
        'SPTTM',
        'HighLow_1M',
        'HighLow_3M',
        'HighLow_6M',
        'IVFF3_1M',
        'IVFF3_3M',
        'RSquare_1M',
        'RSquare_3M',
        'ResVol',
        'STD_1M',
        'STD_1M_Excess',
        'STD_1Y',
        'STD_1Y_Excess',
        'STD_3M',
        'STD_3M_Excess',
        'STD_6M',
        'STD_6M_Excess'
    ]
    pass
para = Para()

class Synthesis():
    def __init__(self):
        self.tradingDateList = getTradingDateFromJY(para.startDate,
                                               para.endDate,
                                               ifTrade=True, Period='M')
        # get basid data from function basic_data
        self.Price, \
        self.LimitStatus, \
        self.Status, \
        self.listDateNum, \
        self.Industry, \
        self.Size = basic_data(para)

        pass

    def every_month(self,para,synthesis_Method):
        Factor = pd.DataFrame()
        WIC = []
        IC_list = []
        for i, currentDate in enumerate(tqdm(self.tradingDateList[:-1])):
            # get lastDate for corresponding time frequancy(for return calculation)
            lastDate = self.tradingDateList[self.tradingDateList.index(currentDate) - 1]

            # use different method to calculate the return
            # logreturn for short time period and simple return calculation for long time period
            if para.ret_calMethod == '对数':
                self.ret = np.log(self.Price.loc[currentDate, :] / self.Price.loc[lastDate, :])
            elif para.ret_calMethod == '简单':
                self.ret = self.Price.loc[currentDate, :] / self.Price.loc[lastDate, :] - 1

            # set the basid dataFrame for each cross-section
            # index is the totle stock list
            self.dataFrame = pd.concat([self.ret,
                                   self.LimitStatus.loc[currentDate, :],
                                   self.Status.loc[currentDate, :],
                                   self.listDateNum.loc[currentDate, :],
                                   self.Industry.loc[currentDate, :],
                                   self.Size.loc[currentDate, :]],
                                  axis=1, sort=True)
            self.dataFrame.columns = ['RET',
                                 'LimitStatus',
                                 'Status',
                                 'listDateNum',
                                 'Industry',
                                 'Size']

            # get all of the factor of corresponding date into the basic dataFrame
            for i, factor_name in enumerate(para.factorlist):
                factor_i = loadData(factor_name)
                factor_ii = factor_i.BasicDailyFactorAlpha.loc[para.startDate:para.endDate, :]
                factor_ii = (factor_ii - np.min(factor_ii))/(np.max(factor_ii) - np.min(factor_ii))
                self.dataFrame.loc[:, factor_name] = factor_ii.loc[currentDate,:]

            # copy the basic dataFrame before getting rid of unwantted stocks
            dataFrame_o = self.dataFrame.copy()
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

            # calculate the spearimanr rank IC for factors and return
            IC_matrix, _ = spearmanr(self.dataFrame.iloc[:,-len(para.factorlist):],
                                     self.dataFrame.loc[:,'RET'])
            # get the exact rank IC between factors and return
            IC = IC_matrix[:-1,-1]
            # get IC list from the beginning of the time
            IC_list.append(IC)

            # get all of the IC with the same weights
            if synthesis_Method == '等权重':
                weight = np.array([1/len(para.factorlist)]*len(para.factorlist))
                Factor = Factor.append(pd.DataFrame(dataFrame_o.iloc[:,-len(para.factorlist):].
                                                    dot(weight).values.reshape(1,-1),
                                                    columns = dataFrame_o.index,
                                                    index=[currentDate]))

            # consider the average of the IC list from the beginning of the time
            elif synthesis_Method == 'IC均值加权':
                if len(WIC) == 0:
                    WIC = IC
                else:
                    WIC = 1/len(IC_list) * IC + (1 - 1/len(IC_list)) * np.sum(IC_list)
                Factor = Factor.append(pd.DataFrame((dataFrame_o.iloc[:, -len(para.factorlist):].
                                                     dot(WIC)).values.reshape(1,-1),
                                                    columns=dataFrame_o.index,
                                                    index=[currentDate]))

            # IC IR method is to weight according to the IR
            # IR = mean(IC)/std(IC)
            # considering the volatility of IC
            elif synthesis_Method == 'ICIR加权':
                if len(WIC) == 0:
                    WIC = IC
                else:
                    WIC = 1/len(IC_list) * IC + (1 - 1/len(IC_list)) * np.sum(IC_list)
                if len(IC_list) < para.backtestwindow:
                    demoninator = np.std(pd.DataFrame(IC_list), axis = 0)
                else:
                    demoninator = np.std(pd.DataFrame(IC_list).iloc[-para.backtestwindow:,:], axis = 0)
                weight = np.array(WIC) / np.array(demoninator)
                Factor = Factor.append(pd.DataFrame((dataFrame_o.iloc[:, -len(para.factorlist):].
                                                     dot(weight)).values.reshape(1, -1),
                                                    columns=dataFrame_o.index,
                                                    index=[currentDate]))

            # maximum IR to get the weights
            # use sample martix for covariance estimation
            # sklearn LedoitWolf
            # https://scikit-learn.org/stable/modules/generated/sklearn.covariance.LedoitWolf.html#sklearn.covariance.LedoitWolf
            # IR = weight * mean(IC) / sqrt(weight * cov_matrix * weight)
            # max IR is equal to the solution of the FOS
            # weight = mean(IC) / cov_matrix
            elif synthesis_Method == '最大化IR加权':
                if len(WIC) == 0:
                    WIC = IC
                else:
                    WIC = 1/len(IC_list) * IC + (1 - 1/len(IC_list)) * np.sum(IC_list)
                cov = LedoitWolf().fit(self.dataFrame.iloc[:, -len(para.factorlist):])
                cov_shrink = cov.covariance_[0,:]
                weight = np.array(WIC) / cov_shrink
                Factor = Factor.append(pd.DataFrame((dataFrame_o.iloc[:, -len(para.factorlist):].
                                                     dot(weight)).values.reshape(1, -1),
                                                    columns=dataFrame_o.index,
                                                    index=[currentDate]))

            # shrinking the time-series weights of IC
            elif synthesis_Method == '半衰IC加权':
                if len(WIC) == 0:
                    WIC = IC
                else:
                    WIC = para.shrink_weight * IC + (1 - para.shrink_weight) * WIC
                Factor = Factor.append(pd.DataFrame((dataFrame_o.iloc[:,-len(para.factorlist):].\
                                                     dot(WIC)).values.reshape(1,-1),
                                                    columns=dataFrame_o.index,
                                                    index=[currentDate]))
        return Factor

if __name__ == "__main__":
    para = Para()
    for i in range(len(para.synthesis_Method)):
        method = para.synthesis_Method[i]
        factor = Synthesis().every_month(para = para,
                                         synthesis_Method = method)
        print(factor)
        factor.to_csv(para.result_path+method+'_Factor.csv')