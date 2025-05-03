import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder


def main():
    data = pd.read_csv(r"data\Temperature_Celsius_5Col-2025.csv")

    # scale the whole dataset
    scaler = MinMaxScaler().fit(data)
    data_scaled = pd.DataFrame(scaler.transform(data), columns=data.columns)

    print(f"scaler min: {scaler.data_min_}")
    print(f"scaler max: {scaler.data_max_}")
    print(data.describe())
    print("###")
    print(data_scaled)

    # split the data into training and testing data
    X = data_scaled.drop(columns=["label"])
    y = data_scaled["label"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    print(X_train)
    print(y_train)
    # plt.plot(X_test_scaled)
    # plt.show()


if __name__ == "__main__":
    main()
