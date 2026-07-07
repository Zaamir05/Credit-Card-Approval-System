"""
model_placeholder.py
--------------------
Run this script once to generate a placeholder model.pkl so the Flask app
can start even before you have a real trained model.

Usage:
    python model_placeholder.py
"""

import pickle
import numpy as np
from sklearn.linear_model import LogisticRegression

# Create a tiny dummy dataset (13 features matching the prediction form)
X_dummy = np.random.rand(50, 13)
y_dummy = np.random.randint(0, 2, 50)

# Train a simple logistic regression placeholder
model = LogisticRegression()
model.fit(X_dummy, y_dummy)

# Save to disk
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Placeholder model.pkl created successfully!")
print("   Replace it with your real trained model before production use.")
