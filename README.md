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

### Set up Python environment using `conda` for Jupyter notebooks

If you have [anaconda](https://www.anaconda.com/products/individual) installed, you can set up an environment with all required packages as follows:

1. Install Jupyter notebook and the `nb_conda_kernels` package in the base environment
```
    conda install -c conda-forge notebook
    conda install -c conda-forge nb_conda_kernels
```
2. Create a new environment
```
    conda create --name <insert_name_here> python=3.8 pip ipykernel ipywidgets matplotlib
```
3. Activate the new environment
```
    conda activate <insert_name_here>
```
4. Install Netket (and thereby the dependencies JAX and Flax)
```
    pip install --pre netket
```
5. Leave the new environment
```
    conda deactivate
```

Now you can open Jupyter notebook from the command line (with your `base` environment active) by entering
```
    jupyter notebook
```
In the notebook you should be able to choose a kernel named `Python [conda env:<insert_name_here>]`. When running this kernel, the libraries you just installed should be known.

Source: How to set up jupyter notebook to work with anaconda environments: https://towardsdatascience.com/how-to-set-up-anaconda-and-jupyter-notebook-the-right-way-de3b7623ea4a
