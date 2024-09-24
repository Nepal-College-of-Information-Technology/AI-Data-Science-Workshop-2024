# Import necessary libraries
import streamlit as st
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load the breast cancer dataset
data = load_breast_cancer()

# Select only the 5 features for simplicity
X = data.data[:, [0, 1, 2, 3, 4]]  # mean_radius, mean_texture, mean_perimeter, mean_area, mean_smoothness
y = data.target

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a RandomForestClassifier
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Get accuracy on test data
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

# Streamlit app interface
st.title("Breast Cancer Detection App")

st.write("This app predicts whether the tumor is benign or malignant based on user input.")

# Function to get user input
def get_user_input():
    mean_radius = st.slider('Mean Radius', float(X[:, 0].min()), float(X[:, 0].max()), float(X[:, 0].mean()))
    mean_texture = st.slider('Mean Texture', float(X[:, 1].min()), float(X[:, 1].max()), float(X[:, 1].mean()))
    mean_perimeter = st.slider('Mean Perimeter', float(X[:, 2].min()), float(X[:, 2].max()), float(X[:, 2].mean()))
    mean_area = st.slider('Mean Area', float(X[:, 3].min()), float(X[:, 3].max()), float(X[:, 3].mean()))
    mean_smoothness = st.slider('Mean Smoothness', float(X[:, 4].min()), float(X[:, 4].max()), float(X[:, 4].mean()))

    # Create a dictionary for user inputs
    user_data = {
        'mean_radius': mean_radius,
        'mean_texture': mean_texture,
        'mean_perimeter': mean_perimeter,
        'mean_area': mean_area,
        'mean_smoothness': mean_smoothness
    }
    
    # Convert the dictionary to a dataframe
    features = pd.DataFrame(user_data, index=[0])
    return features

# Get the user input
user_input = get_user_input()

# Display the user input
st.subheader("User Input:")
st.write(user_input)

# Make prediction
prediction = model.predict(user_input)

# Output the result
if prediction[0] == 0:
    st.write("### The prediction is: **Benign**")
else:
    st.write("### The prediction is: **Malignant**")

# Show the accuracy of the model
st.write(f"Model Accuracy: {accuracy * 100:.2f}%")
