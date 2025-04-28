<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>
<div align="center">
  <h1 align="center">Python.climate-lab</h3>

  <p align="center">
    A Python project for training model on temperature data
    <br />
    <br />
  </p>
</div>

<!-- ABOUT THE PROJECT -->
## About The Project

Formatted the jena_climate_2009_2016.csv data into 5 columns containing the "T (degC)" info.
We are supposed to create a model that predict the next temperature of sets of 5.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

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

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE -->
## Usage - prepare data

   ```sh
   uv run format_temperature_data_as_new_csv.py
   ```


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>
