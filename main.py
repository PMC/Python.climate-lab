import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
import numpy as np


def main():
    data = pd.read_csv(f"data\Temperature_Celsius_5Col-2025.csv")

    plt.plot(data)
    plt.show()
    scaler = MinMaxScaler()
    print("did i plot")

    # data_array = np.array(datal "T (deach"1)
    # str(object='') -> str str(byt


if __name__ == "__main__":
    main()
