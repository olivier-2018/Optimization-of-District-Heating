from preprocessor.paths import (PATH_TO_CONSUMER_1,
                                PATH_TO_CONSUMER_2,
                                PATH_TO_CONSUMER_3,
                                PATH_TO_CONSUMER_4,
                                PATH_TO_CONSUMER_5,
                                PATH_TO_CONSUMER_6,
                                PATH_TO_CONSUMER_7,
                                PATH_TO_CONSUMER_8,
                                PATH_TO_CONSUMER_9)
from preprocessor.data_merger import DataMerger
import matplotlib.pyplot as plt
import seaborn as sns

consumer1_weather = DataMerger(PATH_TO_CONSUMER_1)
consumer1_weather = consumer1_weather.merged_data

# distribution plots
for col in consumer1_weather.columns:
    print(col)
    sns.distplot(consumer1_weather[col])
    plt.show()

# scatter plots against leistung_kw
for col in consumer1_weather.columns:
    print(col)
    sns.scatterplot(data=consumer1_weather.reset_index(),
                    x=col, y="leistung_kw",
                    alpha=0.1)
    plt.show()

