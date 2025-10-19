# Diabetes OLS Regression - Dockerized

This project trains an **Ordinary Least Squares (OLS)** regression model on the **Diabetes dataset** using **Python** and **statsmodels**, and is packaged inside a **Docker container** for reproducibility.

---

## 📦 Project Structure

diabetes-ols-docker/
├── app.py # Main script: trains OLS model and saves it
├── requirements.txt # Python dependencies (scikit-learn, statsmodels, joblib, etc.)
├── Dockerfile # Docker build instructions
└── .dockerignore # Files/folders to ignore when building Docker image
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
