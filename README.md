# Heart Disease Risk Prediction

This project aims to predict heart disease risk using machine learning techniques. It fetches the Heart Disease dataset from the UCI Machine Learning Repository and processes it for analysis.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
  1. [Clone the Repository](#1-clone-the-repository)
  2. [Install `uv`](#2-install-uv)
  3. [Initialize the Project and Virtual Environment](#3-initialize-the-project-and-virtual-environment)
  4. [Install Dependencies](#4-install-dependencies)
- [Usage](#usage)
  - [Activate the Virtual Environment](#activate-the-virtual-environment)
  - [Run `make_dataset.py`](#run-make_datasetpy)

---

## Project Overview

This project:

- Fetches the Heart Disease dataset from the UCI Machine Learning Repository.
- Processes and prepares the data for analysis.
- Provides a foundation for building predictive models to assess heart disease risk.

---

## Prerequisites

Before you begin, ensure you have met the following requirements:

- **Operating System**: Linux, macOS, or Windows Subsystem for Linux (WSL).
- **Python Version**: Python 3.12 or higher.
- **Git**: Installed on your system.
- **`pip`**: Python package installer is available.

---

## Installation

Follow these steps to set up the project on your local machine.

### 1. Clone the Repository

Open your terminal and run:

```bash
git clone https://github.com/your_username/heart_disease_risk_prediction.git
cd heart_disease_risk_prediction
  ```

### 2. Install `uv`

[`uv`](https://github.com/astral-sh/uv) is a Python project management tool that simplifies environment and dependency management.

#### a. Upgrade `pip`

- Upgrade `pip` to the latest version using

```bash
pip install --upgrade pip
```

#### b. Install `uv`

- Install `uv` globally using `pip install uv`.

```bash
pip install uv
```

#### c. Verify Installation

- Check that `uv` is installed by running `uv --version`. You should see the version number printed.

```bash
uv --version
```

  You should see the version number printed.

---

### 3. Initialize the Project and Virtual Environment

Use `uv` to initialize the project, which will create a virtual environment and set up project configurations based on `pyproject.toml`:

- Run `uv init` to initialize the project.

```bash
uv init
```

### 4. Install Dependencies

Install all required dependencies specified in `pyproject.toml`:

- Use `uv install` to install dependencies.

```bash
uv install
```

## Usage

### Activate the Virtual Environment

Before running any scripts, activate the virtual environment:

- Activate the virtual environment by running `source .venv/bin/activate`.

```bash
source .venv/bin/activate
```

You should see the virtual environment's name in your terminal prompt.

### Run `make_dataset.py`

Fetch and prepare the dataset by running the `make_dataset.py` script:

- Run `python src/data/make_dataset.py [output_file_path]`, where `[output_file_path]` is the desired location for the saved dataset, such as `data/raw/heart_disease_original_data.csv`.

```bash
python src/data/make_dataset.py data/raw/heart_disease_original_data.csv
```

This command will:

- Fetch the Heart Disease dataset from the UCI repository.
- Save the dataset to the specified path (e.g., `data/raw/heart_disease_original_data.csv`).
- Create the directory for the dataset if it doesn’t already exist.

Note: this part is optional, further down the path, I wrote another function that checks for the data to load it into a dataframe, else dowload it from the source
