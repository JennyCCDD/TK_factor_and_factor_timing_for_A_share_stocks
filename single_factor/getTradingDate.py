import numpy as np
import pandas as pd

def getTradingDateFromJY(startDate, endDate, ifTrade=True, Period='D'):
    """
    startDate：开始时间,int格式,如 20140101
    endDate:截止时间,格式同上
    if_trade：是否要交易日，默认交易日,取其他值为日历日
    Period: 日期频率'D','W','M','Q','Y')，默认'D'日度
    返回为list，其中日期是int格式
    """
    # 首先获取日期的表
    # 从数据库读取改为从本地读取##########################################################
    #sql = "select * from QT_TradingDayNew where SecuMarket in (83,90)"
    #df = pd.read_sql(sql, conn)


    df = pd.read_hdf('.\\data\\'+'df.h5')

    #日期改成int格式
    df['TradingDate']  = df['TradingDate'].apply(lambda x:int(str(x)[:4] + str(x)[5:7] + str(x)[8:10]))
    df = df[(df.TradingDate>=int(startDate))&(df.TradingDate<=int(endDate))]

    #判断是否工作日，以及频度
    if ifTrade == True:
        df2 = df[df.IfTradingDay==1]
        if Period =='D':
            data = df2['TradingDate']
        elif Period =='W':
            data = df2[df2.IfWeekEnd==1]['TradingDate']
        elif Period == 'M':
            data = df2[df2.IfMonthEnd ==1]['TradingDate']
        elif Period == 'Q':
            data = df2[df2.IfQuarterEnd == 1]['TradingDate']
        elif Period =='Y':
            data = df2[df2.IfYearEnd ==1]['TradingDate']
        else:
            raise RuntimeError('Period必须为指定的格式：D, W, M, Q, Y等')

    else:
        data = pd.Series(pd.date_range(str(startDate),str(endDate),freq=Period[0])).apply(lambda x:int(str(x)[:4] + str(x)[5:7] + str(x)[8:10]))

    # revise date:2019.10.16
    # 如果endDate不在data里面，那么就将它添加进去，反之不处理
    w_tdays = list(data)
    if(int(endDate) not in w_tdays):
        w_tdays.extend([int(endDate)])
    return w_tdays