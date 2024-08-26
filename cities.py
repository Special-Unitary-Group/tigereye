import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Cities:
    def __init__(self, grouped_df):
        self.grouped_df = grouped_df

    def get_city_data(self, city_name):
        if city_name not in self.grouped_df["City"].unique():
            raise ValueError(f"City '{city_name}' not found in the dataset.")
        city_df = self.grouped_df[self.grouped_df["City"] == city_name]
        city_df = city_df.drop(["City"], axis=1)
        return city_df