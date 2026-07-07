"""
app.py
------
Main Flask application for the Credit Card Approval Prediction System.

Routes:
    /         → Home page (landing)
    /about    → About page (project overview)
    /predict  → Prediction form (GET & POST)
    /result   → Prediction result page
"""

import os
import pickle
import logging
import numpy as np
from flask import Flask, render_template, request, redirect, url_for, session

# ---------------------------------------------------------------------------
# App initialisation
# ---------------------------------------------------------------------------
app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "cc-approval-secret-2026")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Model loading
# ---------------------------------------------------------------------------
MODEL_PATH = os.path.join(os.path.dirname(__file__), "model.pkl")

def load_model():
    """Load the pickled ML model, or return None if not found."""
    if os.path.exists(MODEL_PATH):
        try:
            with open(MODEL_PATH, "rb") as f:
                model = pickle.load(f)
            logger.info("✅ Model loaded successfully from %s", MODEL_PATH)
            return model
        except Exception as exc:
            logger.warning("⚠️  Failed to load model: %s", exc)
    else:
        logger.warning("⚠️  model.pkl not found – using placeholder prediction logic.")
    return None

model = load_model()

# ---------------------------------------------------------------------------
# Feature encoding maps
# ---------------------------------------------------------------------------

GENDER_MAP          = {"M": 1, "F": 0}
FLAG_MAP            = {"Y": 1, "N": 0}
INCOME_TYPE_MAP     = {
    "Working": 0, "Commercial associate": 1, "Pensioner": 2,
    "State servant": 3, "Student": 4
}
EDUCATION_TYPE_MAP  = {
    "Secondary / secondary special": 0,
    "Higher education": 1,
    "Incomplete higher": 2,
    "Lower secondary": 3,
    "Academic degree": 4
}
FAMILY_STATUS_MAP   = {
    "Married": 0, "Single / not married": 1, "Civil marriage": 2,
    "Separated": 3, "Widow": 4
}
HOUSING_TYPE_MAP    = {
    "House / apartment": 0, "With parents": 1, "Municipal apartment": 2,
    "Rented apartment": 3, "Office apartment": 4, "Co-op apartment": 5
}
OCCUPATION_MAP      = {
    "Laborers": 0, "Core staff": 1, "Accountants": 2, "Managers": 3,
    "Drivers": 4, "Sales staff": 5, "Cleaning staff": 6,
    "Cooking staff": 7, "Private service staff": 8, "Medicine staff": 9,
    "Security staff": 10, "High skill tech staff": 11, "Waiters/barmen staff": 12,
    "Low-skill Laborers": 13, "Realty agents": 14, "Secretaries": 15,
    "IT staff": 16, "HR staff": 17
}

def build_feature_vector(form: dict) -> np.ndarray:
    """
    Convert raw form data into a numerical NumPy array
    expected by model.predict().

    Feature order (13 features):
        0  gender
        1  own_car
        2  own_realty
        3  income_type
        4  education_type
        5  family_status
        6  housing_type
        7  occupation
        8  annual_income      (float)
        9  employment_days    (int, negative = employed)
        10 days_birth         (int, negative)
        11 family_members     (int)
        12 children           (int)
    """
    gender          = GENDER_MAP.get(form.get("gender", "M"), 1)
    own_car         = FLAG_MAP.get(form.get("own_car", "N"), 0)
    own_realty      = FLAG_MAP.get(form.get("own_realty", "N"), 0)
    income_type     = INCOME_TYPE_MAP.get(form.get("income_type", "Working"), 0)
    education_type  = EDUCATION_TYPE_MAP.get(
                          form.get("education_type", "Secondary / secondary special"), 0)
    family_status   = FAMILY_STATUS_MAP.get(form.get("family_status", "Married"), 0)
    housing_type    = HOUSING_TYPE_MAP.get(
                          form.get("housing_type", "House / apartment"), 0)
    occupation      = OCCUPATION_MAP.get(form.get("occupation", "Laborers"), 0)

    try:
        annual_income   = float(form.get("annual_income", 0))
    except ValueError:
        annual_income   = 0.0

    try:
        employment_days = int(form.get("employment_days", 0))
    except ValueError:
        employment_days = 0

    try:
        days_birth      = int(form.get("days_birth", -10000))
    except ValueError:
        days_birth      = -10000

    try:
        family_members  = int(form.get("family_members", 1))
    except ValueError:
        family_members  = 1

    try:
        children        = int(form.get("children", 0))
    except ValueError:
        children        = 0

    features = np.array([[
        gender, own_car, own_realty, income_type, education_type,
        family_status, housing_type, occupation,
        annual_income, employment_days, days_birth,
        family_members, children
    ]])

    return features


def placeholder_predict(features: np.ndarray) -> int:
    """
    Simple rule-based placeholder when model.pkl is unavailable.
    Replace with model.predict() once you have a trained model.
    """
    annual_income   = features[0][8]
    employment_days = features[0][9]
    children        = features[0][12]

    score = 0
    if annual_income >= 150000:
        score += 2
    elif annual_income >= 80000:
        score += 1

    if employment_days <= -365:   # employed for at least 1 year
        score += 1

    if children <= 2:
        score += 1

    return 1 if score >= 2 else 0


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------

@app.route("/")
def home():
    """Landing / home page."""
    return render_template("home.html")


@app.route("/about")
def about():
    """About page – project overview, workflow, timeline."""
    return render_template("about.html")


@app.route("/predict", methods=["GET", "POST"])
def predict():
    """
    GET  → Show the prediction form.
    POST → Collect form data, run inference, redirect to /result.
    """
    if request.method == "POST":
        form_data = request.form.to_dict()
        logger.info("Form data received: %s", form_data)

        features = build_feature_vector(form_data)

        if model is not None:
            prediction = int(model.predict(features)[0])
        else:
            prediction = placeholder_predict(features)

        # Store both result and form data in session for the result page
        session["prediction"]  = prediction
        session["form_data"]   = form_data
        return redirect(url_for("result"))

    return render_template("index.html")


@app.route("/result")
def result():
    """Display the prediction result stored in the session."""
    prediction = session.get("prediction")
    form_data  = session.get("form_data", {})

    if prediction is None:
        return redirect(url_for("predict"))

    return render_template(
        "result.html",
        prediction=prediction,
        form_data=form_data
    )


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    debug = os.environ.get("FLASK_DEBUG", "true").lower() == "true"
    app.run(host="0.0.0.0", port=port, debug=debug)
