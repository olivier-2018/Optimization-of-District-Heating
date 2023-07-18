import pandas as pd


class ConsumerPreprocessor:
    """ input: the raw dataframe of energy,
        output: preprocessed dataframe with datetimeindex """

    def __init__(self, path_to_data):
        self.df_raw = pd.read_csv(path_to_data)
        df_renamed_columns = self._rename_columns(self.df_raw)
        self.data_prepared = self._set_datetimeindex(df_renamed_columns)

    @classmethod
    def _rename_columns(cls, df):
        columns_keys = ['Timestamp',
                        'T6 Aussentemp.(°C)',
                        'T7 RL Primär(°C)',
                        'T8 VL Sekundär(°C)',
                        'T11 RL Sekundär(°C)',
                        'Solltemp. VL Sekundär(°C)',
                        'Max.Rücklauftemp.primär(°C)',
                        'B-Solltemp.(°C)',
                        'B-Status Pumpe',
                        'B-Status Kreis',
                        'B-Status Mischer',
                        'Puffer EIN Oben(°C)',
                        'Puffer AUS Unten(°C)',
                        'Ventilstellung(%)',
                        'AT Mittel(°C)',
                        'AT Langzeit(°C)',
                        'WZ Wärmemenge(kWh)',
                        'WZ Leistung(kW)',
                        'WZ Duchfluss(l/h)',
                        'WZ Rücklauftemp.(°C)',
                        'WZ Vorlauftemp.(°C)',
                        'WZ Fehleranzeige',
                        'WZ Spreizung(°C)',
                        'Ventilstellung Gesamt(%)']

        columns_values = ["timestamp",
                          "aussentemperatur",
                          "primär_temperatur_rl",
                          "sekundär_temperatur_vl",
                          "sekundär_temperatur_rl",
                          "sekundär_temperatur_vl_soll",
                          "maximale_rücklauftemperature",
                          "temperatur_soll",
                          "status_pump",
                          "status_kreis",
                          "status_mischer",
                          "puffer_oben_ein",
                          "puffer_unten_aus",
                          "ventilstellung",
                          "aussentemperatur_mittel",
                          "aussentemperatur_langzeit",
                          "wärmemenge_kwh",
                          "leistung_kw",
                          "durchfluss_liter_per_hour",
                          "rücklauftemperatur",
                          "vorlauftemperatur",
                          "fehleranzeige",
                          "spreizung_celsius",
                          "ventilstellung_gesamt"]

        columns_dict = dict(zip(columns_keys, columns_values))

        return df.rename(columns_dict, axis=1)

    @classmethod
    def _set_datetimeindex(cls, df):
        df.set_index("timestamp", inplace=True)
        df.index = pd.to_datetime(df.index)
        df["hour"], df["month"], df["weekday"] = df.index.hour, df.index.month, df.index.weekday
        # weekday: monday 0, sunday 6
        return df

