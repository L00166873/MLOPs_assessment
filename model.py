"""
needed for pylint. trains the model.
"""

import pickle
import pandas as pd
#import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
#from sklearn.preprocessing import StandardScaler


# Load dataset (Example: Insurance Charges Dataset. Remove first column index)
df = pd.read_csv("student_scores.csv")

# Features (X) and Target (y)
X = df[["Hours"]]
y = df["Scores"]

# Split data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Linear Regression Model
model = LinearRegression()
model.fit(X_train, y_train)

# Save model to a .pkl file
with open("model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model trained and saved as model.pkl!")
