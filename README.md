# CRC 183 summer school "Machine Learning in Condensed Matter Physics"
This is the repository for the CRC 183 summer school ["Machine Learning in Condensed Matter Physics"](https://www.crc183.uni-koeln.de/summer-school-machine-learning/).

## Running the notebooks on remote servers
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/CRC183-summer-school/school_2021/)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/markusschmitt/crc183_summer_school_2021/HEAD)

The badges above take you to servers of google colab or mybinder.org, where you can run the tutorial notebooks remotely.

## Installing required packages

In the hands-on sessions we will use [JAX](https://github.com/google/jax) and the [Netket](https://www.netket.org/) library. Installing NetKet is relatively straightforward and it will automatically install JAX as a dependency. 

For this Tutorial, **if you are running it locally on your machine**, we recommend that you create a clean virtual environment and install NetKet within: 

```bash
python3 -m venv netket
source netket/bin/activate
pip install --pre netket
```

If you are wondering why we use the flag ```--pre``` it is because today we will be working on a pre (beta) release of version 3.0. 

**If you are on Google Colab**, run the following command in the first cell in order to install the required packages:

```bash
!pip install --pre -U netket
```

For the second session you will also have to clone this repository to the Colab directory:

```bash
!git clone https://github.com/CRC183-summer-school/school_2021.git
```
