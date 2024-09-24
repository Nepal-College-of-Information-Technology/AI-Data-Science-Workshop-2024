# Import necessary libraries
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Generate synthetic house price data
np.random.seed(42)

# Create a dataset with 3 features: number of rooms, area (in square feet), and age of house
n_samples = 100
rooms = np.random.randint(1, 10, size=n_samples)
area = np.random.randint(500, 5000, size=n_samples)
age = np.random.randint(1, 100, size=n_samples)

# Generate house prices with some random noise
price = (rooms * 50000) + (area * 200) - (age * 300) + np.random.randint(-20000, 20000, size=n_samples)

# Combine into a DataFrame
data = pd.DataFrame({'Rooms': rooms, 'Area': area, 'Age': age, 'Price': price})

# Split the data into training and testing sets
X = data[['Rooms', 'Area', 'Age']]
y = data['Price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Get model coefficients and intercept
coefficients = model.coef_
intercept = model.intercept_

# Streamlit app interface
st.title("House Price Prediction App")

st.write("""
This app predicts the price of a house based on:
- Number of Rooms
- Area of the house (in square feet)
- Age of the house
""")

# Function to get user input
def get_user_input():
    rooms = st.slider('Number of Rooms', min_value=1, max_value=10, value=3)
    area = st.slider('Area of the House (sq ft)', min_value=500, max_value=5000, value=1500)
    age = st.slider('Age of the House (years)', min_value=1, max_value=100, value=10)
    
    # Create a DataFrame for the input
    user_data = {
        'Rooms': rooms,
        'Area': area,
        'Age': age
    }
    
    features = pd.DataFrame(user_data, index=[0])
    return features

# Get user input
user_input = get_user_input()

# Display user input
st.subheader("User Input:")
st.write(user_input)

# Make prediction based on user input
prediction = model.predict(user_input)

# Display the prediction
st.write(f"### Predicted House Price: ${prediction[0]:,.2f}")

# Show the model details
st.subheader("Linear Regression Model Details")
st.write(f"Model Coefficients: {coefficients}")
st.write(f"Intercept: {intercept:.2f}")


