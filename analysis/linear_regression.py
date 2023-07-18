from DATA_ANALYSIS.analysis.preprocessor import paths
# (PATH_TO_CONSUMER_1,
#                                 PATH_TO_CONSUMER_2,
#                                 PATH_TO_CONSUMER_3,
#                                 PATH_TO_CONSUMER_4,
#                                 PATH_TO_CONSUMER_5,
#                                 PATH_TO_CONSUMER_6,
#                                 PATH_TO_CONSUMER_7,
#                                 PATH_TO_CONSUMER_8,
#                                 PATH_TO_CONSUMER_9)
# from preprocessor.data_merger import DataMerger
import statsmodels.formula.api as smf

consumer1_weather = DataMerger(PATH_TO_CONSUMER_1)
consumer1_weather = consumer1_weather.merged_data

mod = smf.ols(formula='leistung_kw ~ C(month) + C(weekday) + C(hour) + temperature',
              data=consumer1_weather)
res = mod.fit()
print(res.summary())

