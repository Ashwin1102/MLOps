# Diabetes OLS Regression - Dockerized

This project trains an **Ordinary Least Squares (OLS)** regression model on the **Diabetes dataset** using **Python** and **statsmodels**, and is packaged inside a **Docker container** for reproducibility.

---

## 📦 Project Structure

```
Lab3/
├── source/
│   ├── main.py         # Main script: trains OLS model and saves it
│   └── requirements.txt # Python dependencies (scikit-learn, statsmodels, joblib, etc.)
├── Dockerfile          # Docker build instructions
└── README.md           # Project documentation
```

---

## 🧪 Features

- Trains an **OLS regression model** using the **Diabetes dataset** from scikit-learn
- Prints a **model summary** (R², coefficients, p-values)
- Saves the trained model as a **`.pkl`** file
- Fully **Dockerized** for reproducibility and portability

---

## 🛠 Prerequisites

- Docker installed ([Get Docker](https://www.docker.com/get-started))
- Python 3.11 (for local runs, optional if using Docker)
- Basic familiarity with command line / terminal

---

## 🚀 Build and Run with Docker

### 1️⃣ Build the Docker Image

From the project root directory:

```bash
docker build -t diabetes-ols:latest .
```

### 2️⃣ Run the Container

```bash
docker run --rm diabetes-ols:latest
```

### 3️⃣ View Results

After running, you should see:
- Model summary printed to console
- `diabetes_ols_model.pkl` saved in your project directory

---

## 💻 Run Locally (Without Docker)

If you prefer to run without Docker:

### 1️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 2️⃣ Run the Script

```bash
python app.py
```

---

## 📊 Expected Output

The script will display an OLS regression summary similar to:

```
                            OLS Regression Results
==============================================================================
Dep. Variable:                      y   R-squared:                       0.534
Model:                            OLS   Adj. R-squared:                  0.519
Method:                 Least Squares   F-statistic:                     34.17
Date:                Sun, 19 Oct 2025   Prob (F-statistic):           6.72e-44
Time:                        16:20:44   Log-Likelihood:                -1659.2
No. Observations:                 309   AIC:                             3340.
Df Residuals:                     298   BIC:                             3381.
Df Model:                          10
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const        153.7203      3.017     50.952      0.000     147.783     159.658
x1            -8.0236     71.662     -0.112      0.911    -149.051     133.004
x2          -308.8394     72.252     -4.274      0.000    -451.028    -166.651
x3           583.6374     79.604      7.332      0.000     426.980     740.295
x4           299.9907     77.612      3.865      0.000     147.254     452.728
x5          -360.6645    482.466     -0.748      0.455   -1310.137     588.808
x6            95.1169    394.050      0.241      0.809    -680.357     870.591
x7           -93.0359    249.428     -0.373      0.709    -583.898     397.827
x8           118.1598    195.108      0.606      0.545    -265.803     502.123
x9           662.1131    196.528      3.369      0.001     275.354    1048.873
x10           26.0781     77.721      0.336      0.737    -126.873     179.029
==============================================================================
Omnibus:                        3.423   Durbin-Watson:                   2.085
Prob(Omnibus):                  0.181   Jarque-Bera (JB):                2.906
Skew:                           0.140   Prob(JB):                        0.234
Kurtosis:                       2.616   Cond. No.                         225.
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
```

And a saved model file: `diabetes_ols_model.pkl`

---

## 📝 Requirements

See `requirements.txt` for all dependencies:

```txt
scikit-learn>=1.3.0
statsmodels>=0.14.0
pandas>=2.0.0
numpy>=1.24.0
joblib>=1.3.0
```

---

## 🐳 Dockerfile Overview

The Dockerfile uses:
- **Base Image**: `python:3.11`
- **Working Directory**: `/app`
- **Entry Point**: Runs `python app.py` automatically

---
