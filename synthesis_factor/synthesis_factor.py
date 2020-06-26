# -*- coding: utf-8 -*-
__author__ = "Mengxuan Chen"
__email__  = "chenmx19@mails.tsinghua.edu.cn"
__date__   = "20200527-20200623"


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
    synthesis_Method = '等权重' # 等权重、 IC均值加权、 ICIR加权、 最大化IR加权、 半衰IC加权
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


tradingDateList = getTradingDateFromJY(para.startDate,
                                       para.endDate,
                                       ifTrade=True, Period='M')
Price, LimitStatus, Status, listDateNum, Industry, Size = basic_data(para)


Factor = pd.DataFrame()
WIC = []
IC = []
IC_list = []
for i, currentDate in enumerate(tqdm(tradingDateList[:-1])):
    lastDate = tradingDateList[tradingDateList.index(currentDate) - 1]
    if para.ret_calMethod == '对数':
        ret = np.log(Price.loc[currentDate, :] / Price.loc[lastDate, :])
    elif para.ret_calMethod == '简单':
        ret = Price.loc[currentDate, :] / Price.loc[lastDate, :] - 1

    dataFrame = pd.concat([ret,
                           LimitStatus.loc[currentDate, :],
                           Status.loc[currentDate, :],
                           listDateNum.loc[currentDate, :],
                           Industry.loc[currentDate, :],
                           Size.loc[currentDate, :]],
                          axis=1, sort=True)
    dataFrame.columns = ['RET',
                         'LimitStatus',
                         'Status',
                         'listDateNum',
                         'Industry',
                         'Size']

    for i, factor_name in enumerate(para.factorlist):
        factor_i = loadData(factor_name)
        factor_ii = factor_i.BasicDailyFactorAlpha.loc[para.startDate:para.endDate, :]
        factor_ii = (factor_ii - np.min(factor_ii))/(np.max(factor_ii) - np.min(factor_ii))
        dataFrame.loc[:, factor_name] = factor_ii.loc[currentDate,:]


    dataFrame_o = dataFrame.copy()
    dataFrame = dataFrame.dropna()
    dataFrame = dataFrame.loc[dataFrame['LimitStatus'] == 0]  # 提取非涨跌停的正常交易的数据
    dataFrame = dataFrame.loc[dataFrame['Status'] == 1]  # 提取非ST/ST*/退市的正常交易的数据
    dataFrame = dataFrame.loc[dataFrame['listDateNum'] >= para.listnum]  # 提取上市天数超过listnum的股票
    if para.fin_stock == 'no':  # 非银行金融代号41
        dataFrame = dataFrame.loc[dataFrame['Industry'] != 41]


    # IC_l = []
    # if len(WIC) == 0:
    #     IC_matrix, _ = spearmanr(dataFrame.iloc[:,-len(para.factorlist):],
    #                              dataFrame.loc[:,'RET'])
    #     IC = IC_matrix[:-1,-1]
    # else:
    #     for i, factor_name in enumerate(para.factorlist):
    #         IC_i, _ = spearmanr(dataFrame.loc[:, factor_name], dataFrame.loc[:, 'RET'])
    #         IC_l.append(IC_i)
    #     IC.append(IC_l)

    IC_matrix, _ = spearmanr(dataFrame.iloc[:,-len(para.factorlist):],
                             dataFrame.loc[:,'RET'])
    IC = IC_matrix[:-1,-1]
    IC_list.append(IC)

    if para.synthesis_Method == '等权重':
        weight = np.array([1/len(para.factorlist)]*len(para.factorlist))
        Factor = Factor.append(pd.DataFrame(dataFrame_o.iloc[:,-len(para.factorlist):].
                                            dot(weight).values.reshape(1,-1),
                                            columns = dataFrame_o.index,
                                            index=[currentDate]))

    elif para.synthesis_Method == 'IC均值加权':
        if len(WIC) == 0:
            WIC = IC
        else:
            WIC = 1/len(IC_list) * IC + (1 - 1/len(IC_list)) * np.sum(IC_list)
        Factor = Factor.append(pd.DataFrame((dataFrame_o.iloc[:, -len(para.factorlist):].
                                             dot(WIC)).values.reshape(1,-1),
                                            columns=dataFrame_o.index,
                                            index=[currentDate]))

    elif para.synthesis_Method == 'ICIR加权':
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

    elif para.synthesis_Method == '最大化IR加权':
        if len(WIC) == 0:
            WIC = IC
        else:
            WIC = 1/len(IC_list) * IC + (1 - 1/len(IC_list)) * np.sum(IC_list)
        ####### 使用样本协方差矩阵估计
        cov = LedoitWolf().fit(dataFrame.iloc[:, -len(para.factorlist):])
        cov_shrink = cov.covariance_[0,:]
        weight = np.array(WIC) / cov_shrink
        Factor = Factor.append(pd.DataFrame((dataFrame_o.iloc[:, -len(para.factorlist):].
                                             dot(weight)).values.reshape(1, -1),
                                            columns=dataFrame_o.index,
                                            index=[currentDate]))

    elif para.synthesis_Method == '半衰IC加权':
        if len(WIC) == 0:
            WIC = IC
        else:
            WIC = para.shrink_weight * IC + (1 - para.shrink_weight) * WIC
        Factor = Factor.append(pd.DataFrame((dataFrame_o.iloc[:,-len(para.factorlist):].\
                                             dot(WIC)).values.reshape(1,-1),
                                            columns=dataFrame_o.index,
                                            index=[currentDate]))

print(Factor)
Factor.to_csv(para.result_path+para.synthesis_Method+'_Factor.csv')