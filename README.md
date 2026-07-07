# 💳 Credit Card Approval System

A Machine Learning-based Credit Card Approval System developed using **Python, Flask, and multiple Classification Models (Logistic Regression, Random Forest, XGBoost, Decision Tree)** to help banks predict whether an applicant should be approved for a credit card.

> Developed as part of the **SmartBridge AI/ML Internship Program**.

---

## 📖 Overview

Credit Card Approval System is an intelligent web application that predicts whether a credit card application should be approved or rejected, based on the applicant's financial and demographic details. The system leverages Machine Learning to analyze income, employment, family status, and credit history, helping banks make faster, more consistent approval decisions.

The application combines **Exploratory Data Analysis (EDA), Machine Learning, and Flask** to provide an easy-to-use interface for generating instant credit card approval predictions.

---

## 🎯 Problem Statement

Banks and financial institutions receive thousands of credit card applications every day. A significant portion are rejected due to factors such as high existing loan balances, insufficient income levels, or excessive credit inquiries.

Manually reviewing each application is time-consuming and prone to human error, leading to delays and inconsistent decisions. Credit Card Approval System addresses this challenge by using Machine Learning to automate the approval decision based on historical applicant data.

---

## 🎯 Project Objectives

- Develop an intelligent credit card approval prediction system using Machine Learning.
- Analyze applicant data using Exploratory Data Analysis (EDA).
- Train and evaluate multiple classification models (Logistic Regression, Random Forest, XGBoost, Decision Tree).
- Build an interactive Flask web application with a custom FinTech design system.
- Provide real-time, sub-second approval/rejection predictions.
- Demonstrate the practical application of Artificial Intelligence in banking.

---

## ✨ Features

- 💳 Credit Card Approval Prediction using Machine Learning
- 📊 Exploratory Data Analysis (EDA)
- 🌳 Multiple Classification Models (Logistic Regression, Random Forest, XGBoost, Decision Tree)
- 🌐 Flask Web Application
- 🎨 Custom FinTech Design System (Responsive UI)
- ⚡ Instant Prediction (~100ms average response time)
- ✔ 16-Field Applicant Input Form with Validation
- 🔒 Privacy-First — no applicant data stored or transmitted to third parties
- 📈 Model Comparison Dashboard (Accuracy &amp; AUC per model)

---

## 🛠️ Technology Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Machine Learning | Scikit-Learn, XGBoost, Logistic Regression, Random Forest, Decision Tree |
| Backend | Flask |
| Frontend | HTML, CSS, JavaScript |
| Data Analysis | Pandas, NumPy, Matplotlib, Seaborn |
| Development Tools | Jupyter Notebook, Visual Studio Code, Git, GitHub |

---

## 📁 Source Code Structure

```
Credit-Card-Approval-Prediction/
│
├── app.py                    # Flask application (routes, model loading, feature encoding)
├── model.pkl                 # Trained ML model (replace with your trained model)
├── model_placeholder.py      # Script to generate a dummy model.pkl for testing
├── requirements.txt          # Python dependencies
├── README.md                 # This file
│
├── static/
│   ├── css/
│   │   └── style.css         # Custom FinTech design system (900+ lines)
│   ├── js/
│   │   └── script.js         # Client-side animations, counters, validation
│   └── images/                # Static image assets
│
└── templates/
    ├── base.html              # Jinja2 base template (navbar + footer)
    ├── home.html               # Landing page (hero, features, statistics)
    ├── about.html              # About page (objectives, workflow, tech stack)
    ├── index.html              # Prediction form (16 input fields)
    └── result.html             # Result page (approved/rejected card)
```

---

## 🖼️ Application Screenshots

### 🏠 Home Page

/home/zaamir/Downloads/WhatsApp Unknown 2026-07-07 at 10.56.53 AM/

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Zaamir05/Credit-Card-Approval-System.git
```

### 2. Navigate to the Project Folder

```bash
cd Credit-Card-Approval-System
```

### 3. Create a Virtual Environment (Recommended)

**Windows**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. (Optional) Generate a Placeholder Model

If you don't have a trained `model.pkl` yet, use the included script to generate a dummy one for testing:

```bash
python model_placeholder.py
```

### 6. Run the Application

```bash
python app.py
```

### 7. Open in Browser

```
http://127.0.0.1:5000
```

---

## 🔄 Application Workflow

1. Launch the Flask application.
2. Navigate to the **Prediction** page.
3. Enter the applicant's details across 16 fields, including:
   - Gender, Own Car, Own Realty
   - Number of Children
   - Annual Income &amp; Income Type
   - Education Type &amp; Family Status
   - Housing Type
   - Age &amp; Employment Days
   - Mobile Phone, Work Phone, Phone, Email flags
   - Occupation Type
   - Credit History details
4. Click **Predict**.
5. The best-performing trained model processes the input.
6. The approval or rejection decision is displayed instantly, styled as an approved/rejected card.

---

## 🤖 Machine Learning Model

### Algorithms Used

- Logistic Regression
- Random Forest Classifier ⭐ (Best Performer)
- XGBoost (Gradient Boosting)
- Decision Tree Classifier

### Model Performance

| Metric | Value |
|---|---|
| Best Model | Random Forest |
| Accuracy | 93.4% |
| AUC | 0.97 |
| Input Features | 16 |
| Avg Response Time | ~100ms |

### Purpose

Credit Card Approval Prediction — classifying applicants as likely to be **approved** or **rejected** based on their financial and demographic profile.

The best-performing model was selected after comparing all four algorithms and exported as **model.pkl**, which is loaded directly by the Flask backend (`app.py`) for real-time inference.

---

## 📊 Dataset Information

| Attribute | Details |
|---|---|
| Dataset | Credit Card Approval Prediction Dataset |
| Records | 690+ |
| Classes | 2 (Approved, Rejected) |
| Format | CSV |

### Input Features (16)

- Gender
- Own Car
- Own Realty
- Number of Children
- Annual Income
- Income Type
- Education Type
- Family Status
- Housing Type
- Age
- Employment Days
- Mobile Phone
- Work Phone
- Phone
- Email
- Occupation Type

### Output

- Approval Status (Approved / Rejected)

---

## 🧪 Testing

The application has been tested for:

- Functional Testing
- Prediction Accuracy
- User Input Validation (all 16 fields)
- End-to-End Workflow
- Local Deployment

All core functionalities were successfully verified.

---

## ⚠️ Current Limitations

- Runs on the Flask Development Server.
- Trained using a single public dataset.
- No user authentication.
- No live credit bureau API integration.
- No cloud deployment yet.

---

## 🚀 Future Enhancements

- Cloud Deployment (IBM Watson ML / AWS / Azure)
- Live Credit Bureau API Integration
- Risk Score Explainability (SHAP/LIME)
- Database Integration for Application History
- User Authentication for Analysts &amp; Admins
- Mobile Application
- Multilingual Support

---

## 🎥 Project Demonstration

**Demo Video**

[Add your demo video link here]

---

## 👥 Team Members

- Zaamir Hanan Mujeeb (Team Lead)
- Deepak Bellam
- Mohana Krishna Reddy
- Rushikesh Kasthuri
- Shaik Asliman Thaslimaan

---

## 📜 License

This project was developed for academic purposes as part of the **SmartBridge AI/ML Internship Program**.
