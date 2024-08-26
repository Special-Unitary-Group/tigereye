import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Plotting:
    import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Plotting:
    def __init__(self, grouped_df):
        self.grouped_df = grouped_df

    def apodaca(self):
        df_apodaca = self.grouped_df[self.grouped_df["City"] == "Apodaca"]
        df_apodaca = df_apodaca.drop(["City"], axis=1)
        return df_apodaca

    def escobedo(self):
        df_escobedo = self.grouped_df[self.grouped_df["City"] == "Escobedo"]
        df_escobedo = df_escobedo.drop(["City"], axis=1)
        return df_escobedo

    def garcia(self):
        df_garcia = self.grouped_df[self.grouped_df["City"] == "García"]
        df_garcia = df_garcia.drop(["City"], axis=1)
        return df_garcia

    def guadalupe(self):
        df_guadalupe = self.grouped_df[self.grouped_df["City"] == "Guadalupe"]
        df_guadalupe = df_guadalupe.drop(["City"], axis=1)
        return df_guadalupe

    def juarez(self):
        df_juarez = self.grouped_df[self.grouped_df["City"] == "Juarez"]
        df_juarez = df_juarez.drop(["City"], axis=1)
        return df_juarez

    def monterrey(self):
        df_monterrey = self.grouped_df[self.grouped_df["City"] == "Monterrey"]
        df_monterrey = df_monterrey.drop(["City"], axis=1)
        return df_monterrey

    def san_nico(self):
        df_san_nico = self.grouped_df[self.grouped_df["City"] == "San Nicolás de los Garza"]
        df_san_nico = df_san_nico.drop(["City"], axis=1)
        return df_san_nico

    def santa(self):
        df_santa = self.grouped_df[self.grouped_df["City"] == "Santa Catarina"]
        df_santa = df_santa.drop(["City"], axis=1)
        return df_santa

    def santiago(self):
        df_santiago = self.grouped_df[self.grouped_df["City"] == "Santiago"]
        df_santiago = df_santiago.drop(["City"], axis=1)
        return df_santiago