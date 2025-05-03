import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder


def main():
    data = pd.read_csv(f"data\Temperature_Celsius_5Col-2025.csv")

    # We should scale on X and Y separately
    # need to preserve negative values ? MinMaxScaler(feature_range=(-1, 1)).
    x_scaler = MinMaxScaler()
    y_scaler = MinMaxScaler()

    # split the data into training and testing data
    X = data.drop(columns=["label"])
    y = data["label"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    # scale inputs (X)
    X_train_scaled = x_scaler.fit_transform(X_train)
    X_test_scaled = x_scaler.transform(X_test)

    # Optionally, scale outputs (y)
    y_train_scaled = y_scaler.fit_transform(y_train.values.reshape(-1, 1))
    y_test_scaled = y_scaler.transform(y_test.values.reshape(-1, 1))

    # if keras need a dataframe then use:
    # X_train_scaled_df = pd.DataFrame(X_train_scaled, columns=X.columns)

    # print("###")
    print(X_train_scaled)
    print("###")
    print(y_train_scaled)
    # print("###")
    # print(y_train)

    plt.plot(X_test_scaled)
    plt.show()


if __name__ == "__main__":
    main()
