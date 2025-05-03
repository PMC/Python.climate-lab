import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder


def main():
    data = pd.read_csv(f"data\Temperature_Celsius_5Col-2025.csv")

    # split the data into training and testing data
    X = data.drop(columns=["label"])
    y = data["label"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    # scale inputs (X)
    # use X since there can be a difference in train and test
    # need to preserve negative values ? MinMaxScaler(feature_range=(-1, 1)).
    x_scaler = MinMaxScaler().fit(X)
    X_train_scaled = x_scaler.transform(X_train)
    X_test_scaled = x_scaler.transform(X_test)

    print(f"x_scaler min: {x_scaler.data_min_}")
    print(f"x_scaler max: {x_scaler.data_max_}")
    print(X.describe())

    # Optionally, scale outputs (y)
    y_scaler = MinMaxScaler().fit(y.values.reshape(-1, 1))
    y_train_scaled = y_scaler.transform(y_train.values.reshape(-1, 1))
    y_test_scaled = y_scaler.transform(y_test.values.reshape(-1, 1))

    print("###")
    print(f"y_scaler min: {y_scaler.data_min_}")
    print(f"y_scaler max: {y_scaler.data_max_}")
    print(y.describe())
    # if keras need a dataframe then use:
    # X_train_scaled_df = pd.DataFrame(X_train_scaled, columns=X.columns)

    # plt.plot(X_test_scaled)
    # plt.show()


if __name__ == "__main__":
    main()
