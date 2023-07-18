from preprocessor.paths import (PATH_TO_WEATHER)
from preprocessor.preprocessor_cunsumer import ConsumerPreprocessor
from preprocessor.preprocessor_weather import WeatherPreprocessor
import pandas as pd


class DataMerger:
    def __init__(self, path_to_consumer):
        consumer_preprocessor = ConsumerPreprocessor(path_to_consumer)
        self.consumer_data_all = consumer_preprocessor.data_prepared
        self.consumer_data = self.consumer_data_all["leistung_kw"]

        weather_preprocessor = WeatherPreprocessor(path_to_weather=PATH_TO_WEATHER)
        self.weather_data = weather_preprocessor.data_prepared

        consumer_weather = pd.merge(left=self.consumer_data, right=self.weather_data,
                                    left_index=True, right_index=True)
        self.merged_data = consumer_weather