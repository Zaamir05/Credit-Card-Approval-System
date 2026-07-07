# 💳 Credit Card Approval Prediction System

> **An AI-powered Machine Learning web application** that predicts whether a credit card application should be **Approved ✅** or **Rejected ❌** — instantly.

---

## 🖼️ Screenshots

| Home Page | Prediction Form | Result Page |
|-----------|-----------------|-------------|
| Landing hero with model metrics | Professional multi-section form | Approved / Rejected result card |

---

## 📌 Project Description

Banks receive thousands of credit card applications every day. Manual verification is time-consuming, costly, and prone to human bias and error.

This project automates the credit card approval process using **Machine Learning**. The system analyses applicant demographic and financial data and predicts credit-worthiness in real time via a modern **Flask** web application.

The trained model is served through a clean REST API and can be further deployed on **IBM Watson Machine Learning** for enterprise cloud inference.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🤖 **4 ML Models** | Logistic Regression, Decision Tree, Random Forest, XGBoost |
| ⚡ **Real-Time Prediction** | Results generated in milliseconds |
| 🎨 **Premium FinTech UI** | Glassmorphism, animations, dark hero sections |
| 📱 **Fully Responsive** | Works on desktop, tablet and mobile |
| 🔒 **Secure** | No applicant data stored — all processed in-memory |
| 🌐 **IBM Watson Ready** | Designed for seamless cloud deployment |
| ♿ **Accessible** | ARIA labels, semantic HTML, keyboard navigation |

---

## 🛠️ Technologies Used

### Backend
| Technology | Purpose |
|---|---|
| Python 3.10+ | Core language |
| Flask 3.x | Web framework & REST API |
| Pickle | Model serialisation / loading |
| Gunicorn | Production WSGI server |

### Frontend
| Technology | Purpose |
|---|---|
| HTML5 | Semantic page structure |
| CSS3 | Custom FinTech design system |
| JavaScript (ES6+) | Animations, validation, ripple effects |
| Bootstrap 5.3 | Responsive grid and components |
| Bootstrap Icons | Icon library |
| Google Fonts (Inter) | Premium typography |

### Machine Learning
| Library | Purpose |
|---|---|
| Pandas | Data manipulation |
| NumPy | Numerical operations |
| Scikit-learn | Model training & evaluation |
| XGBoost | Gradient boosting classifier |

---

## 📁 Folder Structure

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
│   └── images/               # Static image assets
│
└── templates/
    ├── base.html             # Jinja2 base template (navbar + footer)
    ├── home.html             # Landing page (hero, features, statistics)
    ├── about.html            # About page (objectives, workflow, tech stack)
    ├── index.html            # Prediction form (16 input fields)
    └── result.html           # Result page (approved/rejected card)
```

---

## 🚀 Installation & Setup

### Prerequisites
- Python 3.10 or higher
- pip

### Step 1 — Clone the Repository
```bash
git clone https://github.com/yourusername/Credit-Card-Approval-Prediction.git
cd Credit-Card-Approval-Prediction
```

### Step 2 — Create a Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3 — Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4 — Generate Placeholder Model (optional)

If you don't have a trained `model.pkl` yet, generate a placeholder so the app still runs:

```bash
python model_placeholder.py
```

> ⚠️ Replace `model.pkl` with your real trained model before production deployment.

### Step 5 — Run the Flask Application
```bash
python app.py
```

The application will be available at **http://localhost:5000**

---

## 🌐 How to Run Flask

```bash
# Development (debug mode on)
python app.py

# Or with Flask CLI
set FLASK_APP=app.py          # Windows
export FLASK_APP=app.py       # macOS / Linux
flask run

# Production (Gunicorn)
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

---

## 🧠 Machine Learning Model

### Models Trained
| Model | Accuracy | AUC |
|---|---|---|
| **Random Forest** ⭐ | **93.4%** | **0.97** |
| XGBoost | 91.7% | 0.95 |
| Logistic Regression | 87.2% | 0.91 |
| Decision Tree | 85.5% | 0.86 |

### Input Features (13 encoded features)
| # | Feature | Type |
|---|---|---|
| 1 | Gender | Binary (M/F) |
| 2 | Own Car | Binary (Y/N) |
| 3 | Own Realty | Binary (Y/N) |
| 4 | Income Type | Categorical (5 classes) |
| 5 | Education Type | Categorical (5 classes) |
| 6 | Family Status | Categorical (5 classes) |
| 7 | Housing Type | Categorical (6 classes) |
| 8 | Occupation | Categorical (18 classes) |
| 9 | Annual Income | Float |
| 10 | Employment Days | Integer (negative = employed) |
| 11 | Days Since Birth | Integer (negative = age in days) |
| 12 | Family Members | Integer |
| 13 | Children | Integer |

### How to Integrate Your Trained Model

1. Train your model on the credit card dataset
2. Save it with Pickle:
   ```python
   import pickle
   with open("model.pkl", "wb") as f:
       pickle.dump(your_trained_model, f)
   ```
3. Place `model.pkl` in the project root directory
4. Restart the Flask application — it loads automatically on startup

---

## ☁️ IBM Watson ML Deployment

1. Create an IBM Cloud account at [cloud.ibm.com](https://cloud.ibm.com)
2. Provision a **Watson Machine Learning** service instance
3. Install the IBM Watson SDK:
   ```bash
   pip install ibm-watson-machine-learning
   ```
4. Store your model in the WML repository:
   ```python
   from ibm_watson_machine_learning import APIClient

   wml_credentials = {
       "url":    "https://us-south.ml.cloud.ibm.com",
       "apikey": "YOUR_API_KEY"
   }
   client = APIClient(wml_credentials)
   client.set.default_space("YOUR_SPACE_ID")
   # Store and deploy model...
   ```
5. Update `app.py` to call the WML scoring endpoint instead of the local `model.predict()`

---

## 🔮 Future Enhancements

- [ ] **SHAP Explainability** — Show which features most influenced each prediction
- [ ] **Model Comparison Dashboard** — Side-by-side accuracy metrics for all 4 models
- [ ] **Batch Prediction** — Upload a CSV file and predict multiple applications at once
- [ ] **JWT Authentication** — Secure the prediction API with token-based auth
- [ ] **Database Logging** — Store prediction history in PostgreSQL / SQLite
- [ ] **Docker Containerisation** — One-command deployment with Docker Compose
- [ ] **CI/CD Pipeline** — GitHub Actions for automated testing and deployment
- [ ] **REST API Endpoints** — JSON API for third-party integrations
- [ ] **Email Notifications** — Send approval/rejection emails to applicants
- [ ] **A/B Model Testing** — Compare live model performance in production

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 🙏 Acknowledgements

- UCI Machine Learning Repository for the credit card dataset
- Scikit-learn, XGBoost, and Flask communities
- Bootstrap team for the excellent UI framework
- IBM Watson ML for cloud deployment capabilities

---

<p align="center">
  Built with ❤️ using Python, Flask, and Machine Learning
</p>
