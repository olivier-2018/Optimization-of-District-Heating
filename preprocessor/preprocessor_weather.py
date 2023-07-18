import pandas as pd


class WeatherPreprocessor:
    """ input: the raw dataframe of weather,
        output: preprocessed dataframe with datetimeindex """

    def __init__(self, path_to_weather):
        self.df_raw = pd.read_csv(path_to_weather, encoding='latin1', delimiter=";", header=1, na_values="?")
        df_dropped_rows = self.df_raw.drop(0)
        df_renamed_columns = self._rename_columns(df_dropped_rows)
        df_datetimeindexed = self._set_datetimeindex(df_renamed_columns)
        df_numeric = self._convert_to_numeric(df_datetimeindexed)
        self.data_prepared = df_numeric.dropna(how="all")

    @classmethod
    def _rename_columns(cls, df):
        # Parameter	Temperatur mittel	Rel. Feuchte mittel	Niederschlag	Windgeschwindigkeit mittel	Globalstrahlung
        column_names = ["timestamp",
                        "temperature",
                        "relative_feuchtigkeit",
                        "niederschlag",
                        "windgeschwindigkeit",
                        "globalstrahlung"]
        df.columns = column_names
        return df

    @classmethod
    def _set_datetimeindex(cls, df):
        return df.set_index("timestamp")

    @classmethod
    def _convert_to_numeric(cls, df):
        return df.apply(pd.to_numeric, errors="ignore")
