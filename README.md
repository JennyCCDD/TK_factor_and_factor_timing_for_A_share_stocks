# TK_factor_and_factor_timing_for_A_share_stocks
This is the final project for course quantitative investment introduction.

本文的目标是对基于前景理论的行为金融学TK因子进行检验，结合因子择时模型中的五种合成因子的方式进行投资组合的构建，并利用马科维兹优化和风险平价优化通过给组合中标的赋予不同的权重来控制风险，并对TK时间窗口参数，交易手续费率等参数进行敏感性分析与检验，从策略的完整性的角度出发，我们达到了最初策略设计的初衷。

从回测分析角度上看，在参数设置γ = 0.53，δ = 0.62，α = 0.88，λ = 2.31下，仅依据TK因子单因子进行选股，在2014年12月31日至2020年2月28日进行回测，夏普率为0.066，年化收益为1.7%，表现不尽如人意。在相关性分析汇总， TK因子与最近6个月收益率因子、最近1个月的日收益率最小值因子具有一定的正相关性，而与一个月Fama French三因子回归残差波动率因子、一个月日超额收益率标准差因子具有一定的负相关性，认为TK因子的表现与长期动量效应，超额收益的波动性有关系，总体来说，波动性越大风险越大，受行为金融学偏差影响越大；TK与Beta因子、Value因子呈较强的负相关。可见市场风险越大、股票内在投资价值越优，受行为金融学的偏差影响越小。
   
就因子择时的角度，样本内外半衰IC加权因子最优，其他方法结果不相上下。半衰IC合成因子的平均夏普比率为0.69，平均年化收益率为17.6%，其中马科维兹优化下夏普比率为0.72，年化收益率为16.28%，风险平价优化下夏普比率为0.84，年化收益率为22.7%。我们还使用单因子有效性表现最优的十个因子合成因子，结果并没有体现出明显的不同。
  
就投资组合权重管理方面，马科维兹优化没有明显的优势，但是风险平价模型可以有效降低最大回撤，平均而言，风险平价优化在样本外的平均最大回撤为32%，而在简单加权下平均最大回撤为37%，市值加权下平均最大回撤为36%。

我们使用水木中量平台回测结果发现，半衰加权合成因子稳定性佳、计算效率高，且随回测时长的增加，策略收益表现最好。一年策略收益112.36%，两年策略收益573.60%，三年策略收益921.92%。 ICIR因子加权、最大化单期IR两种合成因子随时间的增加有效性逐渐减弱。IC均值加权、等权重因子近三年选股结果相近，表现也较为相近。
  
在未来的研究中，可以考虑根据行为金融学理论开发更多的因子，或者对文本数据进行分析处理进行策略的开发。就本文中的策略而言，可以针对不同行业进行测试比较行业之间是否存在不同等等。

![](https://github.com/JennyCCDD/TK_factor_and_factor_timing_for_A_share_stocks/blob/master/%E5%9F%BA%E4%BA%8E%E5%89%8D%E6%99%AF%E7%90%86%E8%AE%BATK%E5%9B%A0%E5%AD%90%E7%9A%84A%E8%82%A1%E5%B8%82%E5%9C%BA%E5%9B%A0%E5%AD%90%E6%8B%A9%E6%97%B6%E6%8A%95%E8%B5%84%E7%AD%96%E7%95%A5%E7%A0%94%E7%A9%B6/%E5%B9%BB%E7%81%AF%E7%89%871.PNG)

![](https://github.com/JennyCCDD/TK_factor_and_factor_timing_for_A_share_stocks/blob/master/%E5%9F%BA%E4%BA%8E%E5%89%8D%E6%99%AF%E7%90%86%E8%AE%BATK%E5%9B%A0%E5%AD%90%E7%9A%84A%E8%82%A1%E5%B8%82%E5%9C%BA%E5%9B%A0%E5%AD%90%E6%8B%A9%E6%97%B6%E6%8A%95%E8%B5%84%E7%AD%96%E7%95%A5%E7%A0%94%E7%A9%B6/%E5%B9%BB%E7%81%AF%E7%89%872.PNG)

![](https://github.com/JennyCCDD/TK_factor_and_factor_timing_for_A_share_stocks/blob/master/%E5%9F%BA%E4%BA%8E%E5%89%8D%E6%99%AF%E7%90%86%E8%AE%BATK%E5%9B%A0%E5%AD%90%E7%9A%84A%E8%82%A1%E5%B8%82%E5%9C%BA%E5%9B%A0%E5%AD%90%E6%8B%A9%E6%97%B6%E6%8A%95%E8%B5%84%E7%AD%96%E7%95%A5%E7%A0%94%E7%A9%B6/%E5%B9%BB%E7%81%AF%E7%89%873.PNG)

![](https://github.com/JennyCCDD/TK_factor_and_factor_timing_for_A_share_stocks/blob/master/%E5%9F%BA%E4%BA%8E%E5%89%8D%E6%99%AF%E7%90%86%E8%AE%BATK%E5%9B%A0%E5%AD%90%E7%9A%84A%E8%82%A1%E5%B8%82%E5%9C%BA%E5%9B%A0%E5%AD%90%E6%8B%A9%E6%97%B6%E6%8A%95%E8%B5%84%E7%AD%96%E7%95%A5%E7%A0%94%E7%A9%B6/%E5%B9%BB%E7%81%AF%E7%89%874.PNG)

![](https://github.com/JennyCCDD/TK_factor_and_factor_timing_for_A_share_stocks/blob/master/%E5%9F%BA%E4%BA%8E%E5%89%8D%E6%99%AF%E7%90%86%E8%AE%BATK%E5%9B%A0%E5%AD%90%E7%9A%84A%E8%82%A1%E5%B8%82%E5%9C%BA%E5%9B%A0%E5%AD%90%E6%8B%A9%E6%97%B6%E6%8A%95%E8%B5%84%E7%AD%96%E7%95%A5%E7%A0%94%E7%A9%B6/%E5%B9%BB%E7%81%AF%E7%89%875.PNG)

![](https://github.com/JennyCCDD/TK_factor_and_factor_timing_for_A_share_stocks/blob/master/%E5%9F%BA%E4%BA%8E%E5%89%8D%E6%99%AF%E7%90%86%E8%AE%BATK%E5%9B%A0%E5%AD%90%E7%9A%84A%E8%82%A1%E5%B8%82%E5%9C%BA%E5%9B%A0%E5%AD%90%E6%8B%A9%E6%97%B6%E6%8A%95%E8%B5%84%E7%AD%96%E7%95%A5%E7%A0%94%E7%A9%B6/%E5%B9%BB%E7%81%AF%E7%89%876.PNG)

![](https://github.com/JennyCCDD/TK_factor_and_factor_timing_for_A_share_stocks/blob/master/%E5%9F%BA%E4%BA%8E%E5%89%8D%E6%99%AF%E7%90%86%E8%AE%BATK%E5%9B%A0%E5%AD%90%E7%9A%84A%E8%82%A1%E5%B8%82%E5%9C%BA%E5%9B%A0%E5%AD%90%E6%8B%A9%E6%97%B6%E6%8A%95%E8%B5%84%E7%AD%96%E7%95%A5%E7%A0%94%E7%A9%B6/%E5%B9%BB%E7%81%AF%E7%89%877.PNG)

![](https://github.com/JennyCCDD/TK_factor_and_factor_timing_for_A_share_stocks/blob/master/%E5%9F%BA%E4%BA%8E%E5%89%8D%E6%99%AF%E7%90%86%E8%AE%BATK%E5%9B%A0%E5%AD%90%E7%9A%84A%E8%82%A1%E5%B8%82%E5%9C%BA%E5%9B%A0%E5%AD%90%E6%8B%A9%E6%97%B6%E6%8A%95%E8%B5%84%E7%AD%96%E7%95%A5%E7%A0%94%E7%A9%B6/%E5%B9%BB%E7%81%AF%E7%89%878.PNG)

![](https://github.com/JennyCCDD/TK_factor_and_factor_timing_for_A_share_stocks/blob/master/%E5%9F%BA%E4%BA%8E%E5%89%8D%E6%99%AF%E7%90%86%E8%AE%BATK%E5%9B%A0%E5%AD%90%E7%9A%84A%E8%82%A1%E5%B8%82%E5%9C%BA%E5%9B%A0%E5%AD%90%E6%8B%A9%E6%97%B6%E6%8A%95%E8%B5%84%E7%AD%96%E7%95%A5%E7%A0%94%E7%A9%B6/%E5%B9%BB%E7%81%AF%E7%89%879.PNG)

![](https://github.com/JennyCCDD/TK_factor_and_factor_timing_for_A_share_stocks/blob/master/%E5%9F%BA%E4%BA%8E%E5%89%8D%E6%99%AF%E7%90%86%E8%AE%BATK%E5%9B%A0%E5%AD%90%E7%9A%84A%E8%82%A1%E5%B8%82%E5%9C%BA%E5%9B%A0%E5%AD%90%E6%8B%A9%E6%97%B6%E6%8A%95%E8%B5%84%E7%AD%96%E7%95%A5%E7%A0%94%E7%A9%B6/%E5%B9%BB%E7%81%AF%E7%89%8710.PNG)

![](https://github.com/JennyCCDD/TK_factor_and_factor_timing_for_A_share_stocks/blob/master/%E5%9F%BA%E4%BA%8E%E5%89%8D%E6%99%AF%E7%90%86%E8%AE%BATK%E5%9B%A0%E5%AD%90%E7%9A%84A%E8%82%A1%E5%B8%82%E5%9C%BA%E5%9B%A0%E5%AD%90%E6%8B%A9%E6%97%B6%E6%8A%95%E8%B5%84%E7%AD%96%E7%95%A5%E7%A0%94%E7%A9%B6/%E5%B9%BB%E7%81%AF%E7%89%8711.PNG)

![](https://github.com/JennyCCDD/TK_factor_and_factor_timing_for_A_share_stocks/blob/master/%E5%9F%BA%E4%BA%8E%E5%89%8D%E6%99%AF%E7%90%86%E8%AE%BATK%E5%9B%A0%E5%AD%90%E7%9A%84A%E8%82%A1%E5%B8%82%E5%9C%BA%E5%9B%A0%E5%AD%90%E6%8B%A9%E6%97%B6%E6%8A%95%E8%B5%84%E7%AD%96%E7%95%A5%E7%A0%94%E7%A9%B6/%E5%B9%BB%E7%81%AF%E7%89%8712.PNG)

![](https://github.com/JennyCCDD/TK_factor_and_factor_timing_for_A_share_stocks/blob/master/%E5%9F%BA%E4%BA%8E%E5%89%8D%E6%99%AF%E7%90%86%E8%AE%BATK%E5%9B%A0%E5%AD%90%E7%9A%84A%E8%82%A1%E5%B8%82%E5%9C%BA%E5%9B%A0%E5%AD%90%E6%8B%A9%E6%97%B6%E6%8A%95%E8%B5%84%E7%AD%96%E7%95%A5%E7%A0%94%E7%A9%B6/%E5%B9%BB%E7%81%AF%E7%89%8713.PNG)

![](https://github.com/JennyCCDD/TK_factor_and_factor_timing_for_A_share_stocks/blob/master/%E5%9F%BA%E4%BA%8E%E5%89%8D%E6%99%AF%E7%90%86%E8%AE%BATK%E5%9B%A0%E5%AD%90%E7%9A%84A%E8%82%A1%E5%B8%82%E5%9C%BA%E5%9B%A0%E5%AD%90%E6%8B%A9%E6%97%B6%E6%8A%95%E8%B5%84%E7%AD%96%E7%95%A5%E7%A0%94%E7%A9%B6/%E5%B9%BB%E7%81%AF%E7%89%8714.PNG)

![](https://github.com/JennyCCDD/TK_factor_and_factor_timing_for_A_share_stocks/blob/master/%E5%9F%BA%E4%BA%8E%E5%89%8D%E6%99%AF%E7%90%86%E8%AE%BATK%E5%9B%A0%E5%AD%90%E7%9A%84A%E8%82%A1%E5%B8%82%E5%9C%BA%E5%9B%A0%E5%AD%90%E6%8B%A9%E6%97%B6%E6%8A%95%E8%B5%84%E7%AD%96%E7%95%A5%E7%A0%94%E7%A9%B6/%E5%B9%BB%E7%81%AF%E7%89%8715.PNG)

![](https://github.com/JennyCCDD/TK_factor_and_factor_timing_for_A_share_stocks/blob/master/%E5%9F%BA%E4%BA%8E%E5%89%8D%E6%99%AF%E7%90%86%E8%AE%BATK%E5%9B%A0%E5%AD%90%E7%9A%84A%E8%82%A1%E5%B8%82%E5%9C%BA%E5%9B%A0%E5%AD%90%E6%8B%A9%E6%97%B6%E6%8A%95%E8%B5%84%E7%AD%96%E7%95%A5%E7%A0%94%E7%A9%B6/%E5%B9%BB%E7%81%AF%E7%89%8716.PNG)

![](https://github.com/JennyCCDD/TK_factor_and_factor_timing_for_A_share_stocks/blob/master/%E5%9F%BA%E4%BA%8E%E5%89%8D%E6%99%AF%E7%90%86%E8%AE%BATK%E5%9B%A0%E5%AD%90%E7%9A%84A%E8%82%A1%E5%B8%82%E5%9C%BA%E5%9B%A0%E5%AD%90%E6%8B%A9%E6%97%B6%E6%8A%95%E8%B5%84%E7%AD%96%E7%95%A5%E7%A0%94%E7%A9%B6/%E5%B9%BB%E7%81%AF%E7%89%8717.PNG)

![](https://github.com/JennyCCDD/TK_factor_and_factor_timing_for_A_share_stocks/blob/master/%E5%9F%BA%E4%BA%8E%E5%89%8D%E6%99%AF%E7%90%86%E8%AE%BATK%E5%9B%A0%E5%AD%90%E7%9A%84A%E8%82%A1%E5%B8%82%E5%9C%BA%E5%9B%A0%E5%AD%90%E6%8B%A9%E6%97%B6%E6%8A%95%E8%B5%84%E7%AD%96%E7%95%A5%E7%A0%94%E7%A9%B6/%E5%B9%BB%E7%81%AF%E7%89%8718.PNG)

![](https://github.com/JennyCCDD/TK_factor_and_factor_timing_for_A_share_stocks/blob/master/%E5%9F%BA%E4%BA%8E%E5%89%8D%E6%99%AF%E7%90%86%E8%AE%BATK%E5%9B%A0%E5%AD%90%E7%9A%84A%E8%82%A1%E5%B8%82%E5%9C%BA%E5%9B%A0%E5%AD%90%E6%8B%A9%E6%97%B6%E6%8A%95%E8%B5%84%E7%AD%96%E7%95%A5%E7%A0%94%E7%A9%B6/%E5%B9%BB%E7%81%AF%E7%89%8719.PNG)

![](https://github.com/JennyCCDD/TK_factor_and_factor_timing_for_A_share_stocks/blob/master/%E5%9F%BA%E4%BA%8E%E5%89%8D%E6%99%AF%E7%90%86%E8%AE%BATK%E5%9B%A0%E5%AD%90%E7%9A%84A%E8%82%A1%E5%B8%82%E5%9C%BA%E5%9B%A0%E5%AD%90%E6%8B%A9%E6%97%B6%E6%8A%95%E8%B5%84%E7%AD%96%E7%95%A5%E7%A0%94%E7%A9%B6/%E5%B9%BB%E7%81%AF%E7%89%8720.PNG)

![](https://github.com/JennyCCDD/TK_factor_and_factor_timing_for_A_share_stocks/blob/master/%E5%9F%BA%E4%BA%8E%E5%89%8D%E6%99%AF%E7%90%86%E8%AE%BATK%E5%9B%A0%E5%AD%90%E7%9A%84A%E8%82%A1%E5%B8%82%E5%9C%BA%E5%9B%A0%E5%AD%90%E6%8B%A9%E6%97%B6%E6%8A%95%E8%B5%84%E7%AD%96%E7%95%A5%E7%A0%94%E7%A9%B6/%E5%B9%BB%E7%81%AF%E7%89%8721.PNG)
