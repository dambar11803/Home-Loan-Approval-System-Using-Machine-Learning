# Home Loan Prediction System using Machine Learning in Rastriya Banijya Bank Limited

## 🎓 Master's Thesis Project (Master in Information Technology)
**Author:** Dambar Rai
**Institution:** Purbanchal University (PUSAT) 
**Year:** 2025 
**Thesis Title:** Home Loan Prediction System Using Machine Learning in Rastriya Banijya Bank Limited (RBBL)

---

## 📌 Project Overview

This project is the implementation of my Master’s Thesis, aimed at automating the home loan eligibility and amount prediction system using Machine Learning. The primary objective was to analyze and model real-world loan application data from **Rastriya Banijya Bank Limited (RBBL)**, Nepal’s largest commercial bank, and develop an intelligent system that helps in predicting the suitable loan amount based on client information.

---

## 📊 Step 1: Machine Learning Model Development

### ✅ Dataset Preparation
- **Source:** Home loan applicant data collected from RBBL (real-world dataset).
- **Steps:**
  - Data Cleaning (handling nulls, formatting inconsistencies)
  - Data Encoding (categorical to numerical variables)
  - Data Normalization (feature scaling for uniformity)
  - Train-Test Split (typically 70%-30%)

### ⚙️ Supervised Machine Learning Models Used
- Linear Regression
- Decision Tree Regression
- Random Forest Regression
- K-Nearest Neighbors Regression (KNN)

### 🎯 Model Evaluation
- Performance evaluated using **R² Score** and **Mean Squared Error (MSE)**
- **Best Model:** Random Forest Regressor
- **Achieved Accuracy:** **96%**

---

## 🌐 Step 2: Full Stack Web Implementation

### 🎨 Frontend
- Built using:
  - **HTML**
  - **CSS**
  - **Bootstrap** (for responsive and clean UI)
- Features:
  - User-friendly form to input loan applicant data
  - Instant feedback on predicted loan eligibility and maximum loan amount

### 🛠️ Backend
- Framework: **Django (Python)**
- Responsibilities:
  - Handling user inputs from the frontend
  - Running the trained ML model in real-time
  - Displaying results dynamically
- ML Model Integration:
  - Trained model saved using `joblib`
  - Model loaded and used during each form submission to predict loan amount

---




