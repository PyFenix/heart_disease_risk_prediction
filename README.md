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

- Use `curl` to download the script and execute it with `sh`:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Alternatively

- Install `uv` globally using `pip install uv`.

```bash
pip install uv
```

[See documentation](https://docs.astral.sh/uv/getting-started/installation/)

#### c. Verify Installation

- Check that `uv` is installed by running `uv --version`. You should see the version number printed.

```bash
uv --version
```

  You should see the version number printed.

---

### 3. Install dependencies and create Virtual Environment

Use `uv` to install dependencies and create a virtual environment based on `pyproject.toml`:

- Run `uv sync` to initialize the project.

```bash
uv sync
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

Note: this part is optional, by running main.py there is a function that checks for the data to load it into a dataframe, else download it from the source

Fetch and prepare the dataset by running the `make_dataset.py` script:

- Run `python src/data/make_dataset.py [output_file_path]`, where `[output_file_path]` is the desired location for the saved dataset, such as `data/raw/heart_disease_original_data.csv`.

```bash
python src/data/make_dataset.py data/raw/heart_disease_original_data.csv
```

This command will:

- Fetch the Heart Disease dataset from the UCI repository.
- Save the dataset to the specified path (e.g., `data/raw/heart_disease_original_data.csv`).
- Create the directory for the dataset if it doesn’t already exist.

### Run the Main Pipeline

Execute the entire machine learning pipeline using main.py:

```bash
python main.py
```

This script performs:

1. Data Loading: Checks if the dataset exists locally; if not, downloads it from the source.
1. Data Preprocessing: Cleans and preprocesses the data, including handling missing values and encoding.
1. Model Training: Trains multiple machine learning models.
1. Hyperparameter Tuning: Optimizes model parameters for better performance.
1. Model Evaluation: Evaluates models on test data.
1. Model Saving: Saves the best-performing model to models/trained_model.pkl.

### Explore the Notebooks

Two Jupyter notebooks are provided for detailed analysis:

1. Exploratory Data Analysis (EDA): notebooks/eda.ipynb

- Visualizes data distributions.
- Examines correlations between features.
- Identifies potential data issues.

1. Preprocessing and Modeling: notebooks/preprocessing_and_modelling.ipynb

- Demonstrates data preprocessing steps.
- Trains and evaluates machine learning models.
- Includes hyperparameter tuning examples.

To run the notebooks:

Ensure the virtual environment is activated.

Launch Jupyter Notebook or Jupyter Lab:

```bash
jupyter notebook
# or
jupyter lab
```

Navigate to the notebooks/ directory and open the desired notebook.

## Project Structure

```plaintext
├── data
│   ├── processed
│   └── raw
├── models
│   └── trained_model.pkl
├── notebooks
│   ├── eda.ipynb
│   └── preprocessing_and_modelling.ipynb
├── src
│   ├── data
│   │   └── make_dataset.py
│   ├── features
│   │   └── preprocess_data.py
│   ├── models
│   │   ├── train_model.py
│   │   └── hyperparameter_tuner.py
│   └── utils.py
├── main.py
├── requirements.txt
├── pyproject.toml
├── README.md
└── .gitignore
```

## Data

The dataset used in this project is the Heart Disease dataset from the UCI Machine Learning Repository.

- Features:
  - age: Age of the patient.
  - sex: Sex of the patient.
  - cp: Chest pain type.
  - trestbps: Resting blood pressure.
  - chol: Serum cholesterol in mg/dl.
  - fbs: Fasting blood sugar > 120 mg/dl.
  - restecg: Resting electrocardiographic results.
  - thalach: Maximum heart rate achieved.
  - exang: Exercise-induced angina.
  - oldpeak: ST depression induced by exercise relative to rest.
  - slope: Slope of the peak exercise ST segment.
  - ca: Number of major vessels colored by fluoroscopy.
  - thal: Thalassemia status.
- Target:
  - num: Diagnosis of heart disease (0 = no disease, 1 = disease).

## Models and Evaluation

The following machine learning models are trained and evaluated:

- Logistic Regression
- Support Vector Classifier
- XGBoost Classifier
- Decision Tree Classifier

### Hyperparameter Tuning

Hyperparameters for each model are tuned using grid search to optimize performance.

### Evaluation Metrics

Models are evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC Score

Results are printed to the console and detailed in the notebooks.

## Running the API Locally

You can run the FastAPI application locally for development and testing purposes. Follow the steps below to set up and run the API on your local machine.

---

### Prerequisites

- **Python 3.12**: Ensure that you have the correct Python version installed.
- **Virtual Environment**: It's recommended to use a virtual environment to manage dependencies.
- **Docker (Optional)**: If you prefer to run the API in a Docker container.

---

### Steps to Run Locally

#### 1. Activate the Virtual Environment

Ensure that your virtual environment is activated. If you followed the installation steps earlier, you should have a `.venv` directory.

```bash
source .venv/bin/activate
```

#### 2. Install Required Packages

Install the necessary packages, including FastAPI and Uvicorn.

If you haven't installed the dependencies yet, run:

```bash
uv sync
```

This will install all packages specified in your `pyproject.toml`.

Alternatively, install them directly:

```bash
pip install fastapi uvicorn
```

#### 3. Navigate to the API Directory

Change your directory to where the `app.py` file is located. The `app.py` is located in the root directory.

#### 4. Run the API with Uvicorn

Start the FastAPI application using Uvicorn:

```bash
uvicorn app:app --host 0.0.0.0 --port 8000
```

- **`app:app`** refers to the Python file `app.py` and the FastAPI instance `app` inside that file.
- **`--host 0.0.0.0`** makes the server accessible externally (useful if needed).
- **`--port 8000`** sets the port number.

#### 5. Access the API Documentation

Open your web browser and navigate to:

bash

Copy code

`http://localhost:8000/docs`

You will see the interactive API documentation provided by Swagger UI.

#### 6. Test the API

You can test the API endpoints directly from the Swagger UI interface or use tools like `curl` or Postman.

**Example using `curl`:**

```bash
curl -X POST "http://localhost:8000/predict/" \ -H "Content-Type: application/json" \ -d '{     "features": {         "age": 63,         "sex": 1,         "cp": 3,         "trestbps": 145,         "chol": 233,         "fbs": 1,         "restecg": 0,         "thalach": 150,         "exang": 0,         "oldpeak": 2.3,         "slope": 0,         "ca": 0,         "thal": 1     } }'
```

**Expected Response:**

json

Copy code

`{   "prediction": 1 }`

---

### Running the API with Docker (Optional)

If you prefer to use Docker, you can containerize the API application.

- **Docker**: Ensure that Docker is installed and running on your machine.

#### Steps

##### 1. Build the Docker Image

From the root directory of the project (where the `Dockerfile` is located), build the Docker image:

```bash
docker build -t heart-disease-api .
```

- The `-t heart-disease-api` tags the image with the name `heart-disease-api`.
- The `.` tells Docker to use the `Dockerfile` in the current directory.

##### 2. Run the Docker Container

Run the Docker container and map the container's port to your local machine:

```bash
docker run -d -p 8000:8000 heart-disease-api
```

- `-d` runs the container in detached mode.
- `-p 8000:8000` maps port 8000 in the container to port 8000 on your local machine.

##### 3. Access the API

Just like before, navigate to:

```bash
http://localhost:8000/docs
```

You should see the API documentation and be able to interact with the API.

---

### Notes

- **Model File**: Ensure that the trained model file `trained_model.pkl` is present in the correct directory so that the API can load it. It should be located in a directory named `models` in the project root.
- **Environment Variables**: If your application uses environment variables (e.g., for configuration), make sure to set them appropriately when running the API.
- **Dependencies**: All Python dependencies for the Docker image are specified in `requirements.txt`.
- **Testing**: You can write additional tests or use the provided notebooks to validate the API's functionality.

---

### Troubleshooting

- **Module Not Found Errors**: If you encounter import errors, ensure that your Python path includes the project directory or that you're running the script from the project's root directory.
- **Port Already in Use**: If port 8000 is already in use, specify a different port when running Uvicorn or Docker, e.g., `--port 8001` and `-p 8001:8000`.
- **Docker Permission Issues**: On some systems, you might need to run Docker commands with `sudo`. Alternatively, add your user to the `docker` group.

---

### Stopping the API

- **Uvicorn**: Press `Ctrl+C` in the terminal where the server is running.
- **Docker**: List running containers and stop the desired one.

```bash
docker ps docker stop `CONTAINER_ID`
```

Replace `CONTAINER_ID` with the actual ID of the running container.

## Deploying the API with AWS CDK

This project includes an AWS CDK (Cloud Development Kit) setup for deploying the FastAPI application to AWS. The CDK stack provisions the necessary AWS resources, including an EC2 instance, and deploys the Dockerized application.

---

### Prerequisites

Before deploying using AWS CDK, ensure you have the following:

- **AWS Account**: An active AWS account with permissions to create resources.
- **AWS CLI**: Installed and configured on your machine.
- **AWS CDK**: Installed globally.
- **Docker**: Installed and running on your machine.
- **Node.js**: Required for AWS CDK.
- **Python 3.10 or higher**: For running the CDK app.

---

### Setup Instructions

#### 1. Configure AWS Credentials

The AWS CLI needs to be configured with your AWS credentials. You can configure it manually or use the provided `cdk_init.sh` script.

##### Using `cdk_init.sh`

A script `cdk_init.sh` is provided to automate the initial setup:

- **What `cdk_init.sh` Does**:
  - Configures AWS CLI with credentials from a `.env` file.
  - Creates an EC2 key pair for SSH access.
  - Bootstraps AWS CDK in your AWS account.

**Note**: Ensure your `.env` file contains your AWS credentials in the following format:

```plaintext
AWS_ACCESS_KEY_ID=your-aws-access-key-id
AWS_SECRET_ACCESS_KEY=your-aws-secret-access-key
AWS_DEFAULT_REGION=your-aws-region
```

**Important**: Do not commit your `.env` file to version control. Keep your AWS credentials secure.

**Running the Script**:

bash

Copy code

`chmod +x cdk_init.sh ./cdk_init.sh`

#### 2. Install CDK Dependencies

If you have the project's venv active, you should deactivate it, navigate into the `cdk_container_deploy_app` folder, create a new venv there, activate it and install the dependencies in that folder's requirements.txt.
These are the dependencies needed to deploy cdk.

#### 3. Deploy the CDK Stack

In the `cdk_container_deploy_app` directory, deploy the CDK stack:

```bash
cdk deploy
```

During deployment, you may be prompted to approve the creation of AWS resources, including IAM roles. Type `y` when prompted.

---

### Accessing the Deployed API

After the deployment completes, you can access the API:

1. **Retrieve the EC2 Instance Public IP**:

- In the AWS Management Console, navigate to **EC2** > **Instances**.
- Find the instance created by the CDK stack.
- Note the **Public IPv4 address**.

2. **Access the API**:

- Open a web browser and navigate to `http://PUBLIC-IP-ADDRESS/docs` (replace `PUBLIC-IP-ADDRESS` with the actual IP).
- You should see the Swagger UI documentation for the API.

---

### Cleaning Up

To avoid incurring charges for AWS resources you're no longer using, destroy the CDK stack when you're done:

```bash
cdk destroy
```

Confirm the deletion when prompted.

---

### Additional Notes

- **Security Groups**: The CDK stack sets up security groups to allow inbound traffic on port 80 (HTTP). Ensure this aligns with your security policies.
- **AWS Costs**: Deploying resources on AWS may incur costs. Monitor your AWS usage and billing.
- **Customization**: You can modify the CDK stack by editing the files in the `cdk_app` directory to fit your needs.
