<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->

<a id="readme-top"></a>

<div align="center">
  <h1  align="center">Python.climate-lab</h1>

  <p align="center">
    A Python project for training a model on temperature data
    <br />
    <br />
  </p>
</div>

<!-- ABOUT THE PROJECT -->

## About The Project

Formatted the jena_climate_2009_2016.csv data into 5 columns containing the "T (degC)" info.
We are supposed to create a model that predict the next temperature of sets of 5.

**last update, hopefully**</br>
Output file will contain 5 columns:</br>
Row 1: 1, 2, 3, 4, 5</br>
Row 2: 5, 6, 7, 8, 9 (note the overlapping value 5)</br>
Row 3: 9, 10, 11, 12, 13 (again overlapping on 9)</br>

**Actuall output example**</br>
First few rows of the output file:

| sensor_1 | sensor_2 | sensor_3 | sensor_4 | label |
| -------: | -------: | -------: | -------: | ----: |
|    -8.02 |    -8.41 |    -8.51 |    -8.31 | -8.27 |
|    -8.27 |    -8.05 |    -7.62 |    -7.62 | -7.91 |
|    -7.91 |    -8.43 |    -8.76 |    -8.88 | -8.85 |
|    -8.85 |    -8.83 |    -8.66 |    -8.66 |  -8.7 |
|     -8.7 |    -8.81 |    -8.84 |    -8.94 | -8.94 |

Last few rows of the output file:

| sensor_1 | sensor_2 | sensor_3 | sensor_4 | label |
| -------: | -------: | -------: | -------: | ----: |
|    -2.15 |    -3.19 |     -3.3 |    -3.46 | -3.09 |
|    -3.09 |    -2.75 |    -2.61 |    -2.51 | -2.48 |
|    -2.48 |    -2.48 |    -2.59 |    -2.89 | -3.22 |
|    -3.22 |    -4.08 |    -4.45 |    -4.09 | -3.76 |
|    -3.76 |    -3.93 |    -4.05 |    -3.35 | -3.16 |

<!-- GETTING STARTED -->

## Getting Started

### Prerequisites

- Python 3.10
- TensorFlow (uses `tensorflow_intel-2.18.0-cp310-cp310-win_amd64.whl`)
- uv (https://astral.sh/)

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/PMC/Python.climate-lab.git
   ```
2. Install dependencies:
   ```sh
   pip install tensorflow_intel-2.18.0-cp310-cp310-win_amd64.whl
   uv sync
   ```

<!-- USAGE -->

## Usage - prepare data

```sh
 uv run .\data\extract_temperature_data.py
```

to create the formated csv file needed for this project:
Temperature_Celsius_5Col-2025.csv

<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE` for more information.
