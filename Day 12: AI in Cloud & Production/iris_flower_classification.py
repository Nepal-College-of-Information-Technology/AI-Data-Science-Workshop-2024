# Import libraries
import streamlit as st
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

# Load the Iris dataset
iris = load_iris()
X, y = iris.data, iris.target
model = RandomForestClassifier()
model.fit(X, y)

# Streamlit app interface
st.title("Iris Flower Classifier")

# User input for flower measurements
sepal_length = st.slider('Sepal Length', min_value=1.0, max_value=8.0, step=0.1)
sepal_width = st.slider('Sepal Width', min_value=1.0, max_value=4.5, step=0.1)
petal_length = st.slider('Petal Length', min_value=1.0, max_value=7.0, step=0.1)
petal_width = st.slider('Petal Width', min_value=0.1, max_value=2.5, step=0.1)

# Make a prediction using the input values
prediction = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])

# Display the prediction
st.write(f"The predicted Iris species is: {iris.target_names[prediction][0]}")
