import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder


def main():
    data = pd.read_csv(f"data\Temperature_Celsius_5Col-2025.csv")

    # scale complete DATA using MinMaxScaler, maybe we should scale on X and Y separately
    # need to preserve negative values ? MinMaxScaler(feature_range=(-1, 1)).
    scaler = MinMaxScaler()
    scaler.fit(data)

    data_scaled = scaler.transform(data)
    data_scaled = pd.DataFrame(data_scaled, columns=data.columns)
    print(data_scaled)

    # split the data into training and testing data
    x = data_scaled.drop(columns=["label"])
    y = data_scaled["label"]

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
    print("###")
    print(x_train)
    print("###")
    print(y_train)

    # plt.plot(y)
    # plt.show()


if __name__ == "__main__":
    main()
