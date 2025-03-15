import pandas as pd
import numpy as np
import pickle
import streamlit as st
import base64

# Function to read and encode the image file
def get_base64_image(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    return encoded_string

# Set the background image using CSS
def set_background(image_base64):
    page_bg_img = f"""
    <style>
    .stApp {{
        background: url("data:image/png;base64,{image_base64}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        color: white;  /* Default text color */
    }}
    /* Main content styling */
    .css-1g8v9l0 {{
        background: rgba(255, 255, 255, 0.8); /* Slightly transparent for better readability */
        padding: 20px; /* Padding for content */
        border-radius: 10px; /* Rounded corners */
    }}
    /* Set text color to black for all text elements */
    h1, h2, h3, h4, h5, h6, p, span, div, label {{
        color: white; /* Ensuring all text is white */
    }}
    .stButton > button {{
        background-color: #4C4C6D; /* Button color */
        color: white; /* Text color for button */
        border-radius: 10px;
        border: none;
        padding: 10px 20px;
        font-size: 16px;
    }}
    .stButton > button:hover {{
        background-color: #6A5ACD; /* Button hover color */
        color: white;
    }}
    .stSlider > div {{
        background-color: transparent;
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)

# Load dataset to verify feature names
data = pd.read_csv('USA_Housing.csv')

# Strip any whitespace from column names
data.columns = data.columns.str.strip()

# Features to use for prediction
numerical_features = [
    'Avg. Income',
    'Avg. House Age',
    'Avg. Number of Rooms',
    'Avg. Number of Bedrooms',
    'Area Population'
]

# Call the function with the uploaded background image
image_base64 = get_base64_image("image.jpg")  # Path to your uploaded image
set_background(image_base64)

# Streamlit Frontend
st.markdown("<h1 style='text-align: center;'>Housing Price Prediction</h1>", unsafe_allow_html=True)

# Predict using the selected model
selected_model = st.selectbox("Choose a model", ['LinearRegression', 'RidgeRegression', 'LassoRegression', 
                                                   'ElasticNet', 'SGDRegressor', 
                                                   'SVM', 'LGBM', 'XGBoost', 'KNN'])

# User input for features
user_inputs = {feature: st.number_input(f"Enter {feature}:") for feature in numerical_features}

if st.button("Predict"):
    input_data = np.array([[user_inputs[feature] for feature in numerical_features]])

    # Load the selected model
    with open(f'{selected_model}.pkl', 'rb') as f:
        model = pickle.load(f)
    
    # Predict price
    prediction = model.predict(input_data)

    # Display prediction
    st.success(f"The predicted price is: ${prediction[0]:,.2f}")

# Footer
st.markdown("---")
st.write("Created with ❤️ by Pratik")