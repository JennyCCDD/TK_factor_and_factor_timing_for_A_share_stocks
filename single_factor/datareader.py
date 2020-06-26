# -*- coding: utf-8 -*-

__author__ = "Mengxuan Chen"
__email__  = "chenmx19@mails.tsinghua.edu.cn"
__date__   = "20200521"

import pandas as pd
# In[] load data
dataPathPrefix = 'D:\caitong_security'# 修改储存数据的路径

class loadData():
    def __init__(self,para):

        #######################读取各类因子数据
        #######################Beta
        if para == 'Beta252':
            self.BasicDailyFactorAlpha = pd.read_hdf(
            dataPathPrefix + '\DataBase\Data_AlphaFactor\Beta\BasicDailyFactorAlpha_Beta252.h5')

        #######################EarningYield
        elif para == 'GPOA':
            self.BasicDailyFactorAlpha = pd.read_hdf(
            dataPathPrefix + '\DataBase\Data_AlphaFactor\EarningYield\BasicDailyFactorAlpha_GPOA.h5')
        elif para == 'GPOAQ':
            self.BasicDailyFactorAlpha = pd.read_hdf(
            dataPathPrefix + '\DataBase\Data_AlphaFactor\EarningYield\BasicDailyFactorAlpha_GPOAQ.h5')
        elif para == 'GrossProfitMargin':
            self.BasicDailyFactorAlpha = pd.read_hdf(
            dataPathPrefix + '\DataBase\Data_AlphaFactor\EarningYield\BasicDailyFactorAlpha_GrossProfitMargin.h5')
        elif para == 'GrossProfitMarginQ':
            self.BasicDailyFactorAlpha = pd.read_hdf(
            dataPathPrefix + '\DataBase\Data_AlphaFactor\EarningYield\BasicDailyFactorAlpha_GrossProfitMarginQ.h5')
        elif para == 'NetProfitMargin':
            self.BasicDailyFactorAlpha = pd.read_hdf(
            dataPathPrefix + '\DataBase\Data_AlphaFactor\EarningYield\BasicDailyFactorAlpha_NetProfitMargin.h5')
        elif para == 'NetProfitMarginQ':
            self.BasicDailyFactorAlpha = pd.read_hdf(
            dataPathPrefix + '\DataBase\Data_AlphaFactor\EarningYield\BasicDailyFactorAlpha_NetProfitMarginQ.h5')
        elif para == 'ROA':
            self.BasicDailyFactorAlpha = pd.read_hdf(
            dataPathPrefix + '\DataBase\Data_AlphaFactor\EarningYield\BasicDailyFactorAlpha_ROA.h5')
        elif para == 'ROAQ':
            self.BasicDailyFactorAlpha = pd.read_hdf(
            dataPathPrefix + '\DataBase\Data_AlphaFactor\EarningYield\BasicDailyFactorAlpha_ROAQ.h5')
        elif para == 'ROE_Diluted':
            self.BasicDailyFactorAlpha = pd.read_hdf(
            dataPathPrefix + '\DataBase\Data_AlphaFactor\EarningYield\BasicDailyFactorAlpha_ROE_Diluted.h5')
        elif para == 'ROE_DilutedQ':
            self.BasicDailyFactorAlpha = pd.read_hdf(
            dataPathPrefix + '\DataBase\Data_AlphaFactor\EarningYield\BasicDailyFactorAlpha_ROE_DilutedQ.h5')
        elif para == 'ROE_ExDiluted':
            self.BasicDailyFactorAlpha = pd.read_hdf(
            dataPathPrefix + '\DataBase\Data_AlphaFactor\EarningYield\BasicDailyFactorAlpha_ROE_ExDiluted.h5')
        elif para == 'ROE_ExDilutedQ':
            self.BasicDailyFactorAlpha = pd.read_hdf(
            dataPathPrefix + '\DataBase\Data_AlphaFactor\EarningYield\BasicDailyFactorAlpha_ROE_ExDilutedQ.h5')

        #######################\Financial
        elif para == 'SUE':
            self.BasicDailyFactorAlpha = pd.read_hdf(
            dataPathPrefix + '\DataBase\Data_AlphaFactor\Financial\BasicDailyFactorAlpha_SUE.h5')
        elif para == 'SUR':
            self.BasicDailyFactorAlpha = pd.read_hdf(
            dataPathPrefix + '\DataBase\Data_AlphaFactor\Financial\BasicDailyFactorAlpha_SUR.h5')

        #######################\Growth
        elif para == 'GGPOAQ':
            self.BasicDailyFactorAlpha = pd.read_hdf(
            dataPathPrefix + '\DataBase\Data_AlphaFactor\Growth\BasicDailyFactorAlpha_GGPOAQ.h5')
        elif para == 'GGrossProfitMarginQ':
            self.BasicDailyFactorAlpha = pd.read_hdf(
            dataPathPrefix + '\DataBase\Data_AlphaFactor\Growth\BasicDailyFactorAlpha_GGrossProfitMarginQ.h5')
        elif para == 'GROAQ':
            self.BasicDailyFactorAlpha = pd.read_hdf(
            dataPathPrefix + '\DataBase\Data_AlphaFactor\Growth\BasicDailyFactorAlpha_GROAQ.h5')
        elif para == 'GROEQ':
            self.BasicDailyFactorAlpha = pd.read_hdf(
            dataPathPrefix + '\DataBase\Data_AlphaFactor\Growth\BasicDailyFactorAlpha_GROEQ.h5')
        elif para == 'NetOperateCashFlowQYOY':
            self.BasicDailyFactorAlpha = pd.read_hdf(
            dataPathPrefix + '\DataBase\Data_AlphaFactor\Growth\BasicDailyFactorAlpha_NetOperateCashFlowQYOY.h5')
        elif para == 'NetProfitQYOY':
            self.BasicDailyFactorAlpha = pd.read_hdf(
            dataPathPrefix + '\DataBase\Data_AlphaFactor\Growth\BasicDailyFactorAlpha_NetProfitQYOY.h5')
        elif para == 'OperatingRevenueQYOY':
            self.BasicDailyFactorAlpha = pd.read_hdf(
            dataPathPrefix + '\DataBase\Data_AlphaFactor\Growth\BasicDailyFactorAlpha_OperatingRevenueQYOY.h5')

        ####################### Leverage
        elif para == 'BLEV':
            self.BasicDailyFactorAlpha = pd.read_hdf(
            dataPathPrefix + '\DataBase\Data_AlphaFactor\Leverage\BasicDailyFactorAlpha_BLEV.h5')
        elif para == 'DTOA':
            self.BasicDailyFactorAlpha = pd.read_hdf(
            dataPathPrefix + '\DataBase\Data_AlphaFactor\Leverage\BasicDailyFactorAlpha_DTOA.h5')
        elif para == 'MLEV':
            self.BasicDailyFactorAlpha = pd.read_hdf(
            dataPathPrefix + '\DataBase\Data_AlphaFactor\Leverage\BasicDailyFactorAlpha_MLEV.h5')

        ####################### Liquidity
        elif para == 'AmihudILLIQ':
            self.BasicDailyFactorAlpha = pd.read_hdf(
            dataPathPrefix + '\DataBase\Data_AlphaFactor\Liquidity\BasicDailyFactorAlpha_AmihudILLIQ.h5')
        elif para == 'TurnOver_1M':
            self.BasicDailyFactorAlpha = pd.read_hdf(
            dataPathPrefix + '\DataBase\Data_AlphaFactor\Liquidity\BasicDailyFactorAlpha_TurnOver_1M.h5')
        elif para == 'TurnOver_1Y':
            self.BasicDailyFactorAlpha = pd.read_hdf(
            dataPathPrefix + '\DataBase\Data_AlphaFactor\Liquidity\BasicDailyFactorAlpha_TurnOver_1Y.h5')
        elif para == 'TurnOver_3M':
            self.BasicDailyFactorAlpha = pd.read_hdf(
            dataPathPrefix + '\DataBase\Data_AlphaFactor\Liquidity\BasicDailyFactorAlpha_TurnOver_3M.h5')
        elif para == 'TurnOver_6M':
            self.BasicDailyFactorAlpha = pd.read_hdf(
            dataPathPrefix + '\DataBase\Data_AlphaFactor\Liquidity\BasicDailyFactorAlpha_TurnOver_6M.h5')
        elif para == 'VSTD_1M':
            self.BasicDailyFactorAlpha = pd.read_hdf(
            dataPathPrefix + '\DataBase\Data_AlphaFactor\Liquidity\BasicDailyFactorAlpha_VSTD_1M.h5')
        elif para == 'VSTD_3M':
            self.BasicDailyFactorAlpha = pd.read_hdf(
            dataPathPrefix + '\DataBase\Data_AlphaFactor\Liquidity\BasicDailyFactorAlpha_VSTD_3M.h5')
        elif para == 'VSTD_6M':
            self.BasicDailyFactorAlpha = pd.read_hdf(
            dataPathPrefix + '\DataBase\Data_AlphaFactor\Liquidity\BasicDailyFactorAlpha_VSTD_6M.h5')


        #######################\Momentum
        elif para == 'MaxRet21':
            self.BasicDailyFactorAlpha = pd.read_hdf(
            dataPathPrefix + '\DataBase\Data_AlphaFactor\Momentum\BasicDailyFactorAlpha_MaxRet21.h5')
        elif para == 'MinRet21':
            self.BasicDailyFactorAlpha = pd.read_hdf(
            dataPathPrefix + '\DataBase\Data_AlphaFactor\Momentum\BasicDailyFactorAlpha_MinRet21.h5')
        elif para == 'Ret21':
            self.BasicDailyFactorAlpha = pd.read_hdf(
            dataPathPrefix + '\DataBase\Data_AlphaFactor\Momentum\BasicDailyFactorAlpha_Ret21.h5')
        elif para == 'Ret63':
            self.BasicDailyFactorAlpha = pd.read_hdf(
            dataPathPrefix + '\DataBase\Data_AlphaFactor\Momentum\BasicDailyFactorAlpha_Ret63.h5')
        elif para == 'Ret126':
            self.BasicDailyFactorAlpha = pd.read_hdf(
            dataPathPrefix + '\DataBase\Data_AlphaFactor\Momentum\BasicDailyFactorAlpha_Ret126.h5')
        elif para == 'Ret252_21':
            self.BasicDailyFactorAlpha = pd.read_hdf(
            dataPathPrefix + '\DataBase\Data_AlphaFactor\Momentum\BasicDailyFactorAlpha_Ret252_21.h5')

        #######################\MV
        elif para == 'LnNegotiableMV':
            self.BasicDailyFactorAlpha = pd.read_hdf(
            dataPathPrefix + '\DataBase\Data_AlphaFactor\MV\BasicDailyFactorAlpha_LnNegotiableMV.h5')
        elif para == 'LnTotalMV':
            self.BasicDailyFactorAlpha = pd.read_hdf(
            dataPathPrefix + '\DataBase\Data_AlphaFactor\MV\BasicDailyFactorAlpha_LnTotalMV.h5')
        elif para == 'NegotiableMV':
            self.BasicDailyFactorAlpha = pd.read_hdf(
            dataPathPrefix + '\DataBase\Data_AlphaFactor\MV\BasicDailyFactorAlpha_NegotiableMV.h5')
        elif para == 'NegotiableMVNL':
            self.BasicDailyFactorAlpha = pd.read_hdf(
            dataPathPrefix + '\DataBase\Data_AlphaFactor\MV\BasicDailyFactorAlpha_NegotiableMVNL.h5')
        elif para == 'TotalMV':
            self.BasicDailyFactorAlpha = pd.read_hdf(
            dataPathPrefix + '\DataBase\Data_AlphaFactor\MV\BasicDailyFactorAlpha_TotalMV.h5')
        elif para == 'TotalMVNL':
            self.BasicDailyFactorAlpha = pd.read_hdf(
            dataPathPrefix + '\DataBase\Data_AlphaFactor\MV\BasicDailyFactorAlpha_TotalMVNL.h5')

        #######################Others
        elif para == 'IMFFFactorNoAlpha':
            self.BasicDailyFactorAlpha = pd.read_hdf(
            dataPathPrefix + '\DataBase\Data_AlphaFactor\Others\BasicDailyFactorAlpha_IMFFFactorNoAlpha.h5')

        #######################\PriceVolume
        elif para == 'APBFactor_1M':
            self.BasicDailyFactorAlpha = pd.read_hdf(
            dataPathPrefix + '\DataBase\Data_AlphaFactor\PriceVolume\BasicDailyFactorAlpha_APBFactor_1M.h5')
        elif para == 'APBFactor_5D':
            self.BasicDailyFactorAlpha = pd.read_hdf(
            dataPathPrefix + '\DataBase\Data_AlphaFactor\PriceVolume\BasicDailyFactorAlpha_APBFactor_5D.h5')

        #######################\Quality
        elif para == 'AssetsTurn':
            self.BasicDailyFactorAlpha = pd.read_hdf(
            dataPathPrefix + '\DataBase\Data_AlphaFactor\Quality\BasicDailyFactorAlpha_AssetsTurn.h5')
        elif para == 'CFO':
            self.BasicDailyFactorAlpha = pd.read_hdf(
            dataPathPrefix + '\DataBase\Data_AlphaFactor\Quality\BasicDailyFactorAlpha_CFO.h5')
        elif para == 'CurrentRatio':
            self.BasicDailyFactorAlpha = pd.read_hdf(
            dataPathPrefix + '\DataBase\Data_AlphaFactor\Quality\BasicDailyFactorAlpha_CurrentRatio.h5')
        elif para == 'NetProfitCashCover':
            self.BasicDailyFactorAlpha = pd.read_hdf(
            dataPathPrefix + '\DataBase\Data_AlphaFactor\Quality\BasicDailyFactorAlpha_NetProfitCashCover.h5')
        elif para == 'QualityFactor':
            self.BasicDailyFactorAlpha = pd.read_hdf(
            dataPathPrefix + '\DataBase\Data_AlphaFactor\Quality\BasicDailyFactorAlpha_QualityFactor.h5')
        elif para == 'QualityIncrease':
            self.BasicDailyFactorAlpha = pd.read_hdf(
            dataPathPrefix + '\DataBase\Data_AlphaFactor\Quality\BasicDailyFactorAlpha_QualityIncrease.h5')

        #######################\Value
        elif para == 'BP':
            self.BasicDailyFactorAlpha = pd.read_hdf(
            dataPathPrefix + '\DataBase\Data_AlphaFactor\Value\BasicDailyFactorAlpha_BP.h5')
        elif para == 'DividendRatioTTM':
            self.BasicDailyFactorAlpha = pd.read_hdf(
            dataPathPrefix + '\DataBase\Data_AlphaFactor\Value\BasicDailyFactorAlpha_DividendRatioTTM.h5')
        elif para == 'EPTTM':
            self.BasicDailyFactorAlpha = pd.read_hdf(
            dataPathPrefix + '\DataBase\Data_AlphaFactor\Value\BasicDailyFactorAlpha_EPTTM.h5')
        elif para == 'NCFPTTM':
            self.BasicDailyFactorAlpha = pd.read_hdf(
            dataPathPrefix + '\DataBase\Data_AlphaFactor\Value\BasicDailyFactorAlpha_NCFPTTM.h5')
        elif para == 'OCFPTTM':
            self.BasicDailyFactorAlpha = pd.read_hdf(
            dataPathPrefix + '\DataBase\Data_AlphaFactor\Value\BasicDailyFactorAlpha_OCFPTTM.h5')
        elif para == 'SPTTM':
            self.BasicDailyFactorAlpha = pd.read_hdf(
            dataPathPrefix + '\DataBase\Data_AlphaFactor\Value\BasicDailyFactorAlpha_SPTTM.h5')

        #######################\Volatility
        elif para == 'HighLow_1M':
            self.BasicDailyFactorAlpha = pd.read_hdf(
            dataPathPrefix + '\DataBase\Data_AlphaFactor\Volatility\BasicDailyFactorAlpha_HighLow_1M.h5')
        elif para == 'HighLow_3M':
            self.BasicDailyFactorAlpha = pd.read_hdf(
            dataPathPrefix + '\DataBase\Data_AlphaFactor\Volatility\BasicDailyFactorAlpha_HighLow_3M.h5')
        elif para == 'HighLow_6M':
            self.BasicDailyFactorAlpha = pd.read_hdf(
            dataPathPrefix + '\DataBase\Data_AlphaFactor\Volatility\BasicDailyFactorAlpha_HighLow_6M.h5')
        elif para == 'IVFF3_1M':
            self.BasicDailyFactorAlpha = pd.read_hdf(
            dataPathPrefix + '\DataBase\Data_AlphaFactor\Volatility\BasicDailyFactorAlpha_IVFF3_1M.h5')
        elif para == 'IVFF3_3M':
            self.BasicDailyFactorAlpha = pd.read_hdf(
            dataPathPrefix + '\DataBase\Data_AlphaFactor\Volatility\BasicDailyFactorAlpha_IVFF3_3M.h5')
        elif para == 'RSquare_1M':
            self.BasicDailyFactorAlpha = pd.read_hdf(
            dataPathPrefix + '\DataBase\Data_AlphaFactor\Volatility\BasicDailyFactorAlpha_IVFF3_RSquare_1M.h5')
        elif para == 'RSquare_3M':
            self.BasicDailyFactorAlpha = pd.read_hdf(
            dataPathPrefix + '\DataBase\Data_AlphaFactor\Volatility\BasicDailyFactorAlpha_IVFF3_RSquare_3M.h5')
        elif para == 'ResVol':
            self.BasicDailyFactorAlpha = pd.read_hdf(
            dataPathPrefix + '\DataBase\Data_AlphaFactor\Volatility\BasicDailyFactorAlpha_ResVol.h5')
        elif para == 'STD_1M':
            self.BasicDailyFactorAlpha = pd.read_hdf(
            dataPathPrefix + '\DataBase\Data_AlphaFactor\Volatility\BasicDailyFactorAlpha_STD_1M.h5')
        elif para == 'STD_1M_Excess':
            self.BasicDailyFactorAlpha = pd.read_hdf(
            dataPathPrefix + '\DataBase\Data_AlphaFactor\Volatility\BasicDailyFactorAlpha_STD_1M_Excess.h5')
        elif para == 'STD_1Y':
            self.BasicDailyFactorAlpha = pd.read_hdf(
            dataPathPrefix + '\DataBase\Data_AlphaFactor\Volatility\BasicDailyFactorAlpha_STD_1Y.h5')
        elif para == 'STD_1Y_Excess':
            self.BasicDailyFactorAlpha = pd.read_hdf(
            dataPathPrefix + '\DataBase\Data_AlphaFactor\Volatility\BasicDailyFactorAlpha_STD_1Y_Excess.h5')
        elif para == 'STD_3M':
            self.BasicDailyFactorAlpha = pd.read_hdf(
            dataPathPrefix + '\DataBase\Data_AlphaFactor\Volatility\BasicDailyFactorAlpha_STD_3M.h5')
        elif para == 'STD_3M_Excess':
            self.BasicDailyFactorAlpha = pd.read_hdf(
            dataPathPrefix + '\DataBase\Data_AlphaFactor\Volatility\BasicDailyFactorAlpha_STD_3M_Excess.h5')
        elif para == 'STD_6M':
            self.BasicDailyFactorAlpha = pd.read_hdf(
            dataPathPrefix + '\DataBase\Data_AlphaFactor\Volatility\BasicDailyFactorAlpha_STD_6M.h5')
        elif para == 'STD_6M_Excess':
            self.BasicDailyFactorAlpha = pd.read_hdf(
            dataPathPrefix + '\DataBase\Data_AlphaFactor\Volatility\BasicDailyFactorAlpha_STD_6M_Excess.h5')

        else:
            print('No such factor in our list! Please check!')
        ######################## closeprice 后复权价格，用于计算收益率
        # self.stockClosePrice = pd.read_hdf(
        #     dataPathPrefix + '\DataBase\Data_AShareEODPrices\BasicDailyFactor_StockForwardClosePrice.h5')
