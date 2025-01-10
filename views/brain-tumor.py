import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from sklearn.preprocessing import StandardScaler
import joblib
from PIL import Image
import pandas as pd
from utils import get_img_as_base64, preprocess_image


backgroundImg = get_img_as_base64("assets/2.png")
modelImage = get_img_as_base64("assets/brain_tumor_icon.png")

# Load Models
brain_tumor_model = load_model('models/brain_tumor_model.h5', compile=False)

brain_tumor_classes = ['Benign Tumor', 'Malignant Tumor']

st.markdown("""
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css" rel="stylesheet">
""", unsafe_allow_html=True)


custom_css = f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background-image: url('data:image/png;base64,{backgroundImg}');
        background-size: cover;
        background-repeat: repeat;
    }}

    [data-testid="stImage"] > img {{
        width: 300px;
        height: auto;
        border-radius: 12px;
    }}

    .model-box {{
        background-color: #fff;
        padding: 16px;
        text-align: center;
        border-radius: 12px;
    }}

    .prediction-box {{
        background-color: #fff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        margin: 20px 0;
        text-align: center;
    }}
    .prediction-box h4 {{
        font-size: 1.2rem;
        color: #000;
    }}
    .prediction-box span {{
        color: #1976D2;
    }}
    .highlights {{
        background-color: #fff;
        padding: 16px;
        border-radius: 10px;
        margin-bottom: 32px;
    }}
    .highlights ul {{
        margin: 0;
        padding-left: 20px;
    }}
    .highlights li {{
        font-size: 1rem;
        color: #000;
    }}
    </style>
    """

st.markdown(custom_css, unsafe_allow_html=True)

# Add highlights section
st.markdown(
    """
    <div class="highlights">
        <div style="display: flex; align-items: center; margin-bottom: 15px; gap: 8px;">
            <i class="fas fa-brain" style="font-size: 1.5rem; color: #000; margin-right: 10px;"></i>
            <p style="font-size: 1.1rem; line-height: 1.8; margin: 0; color: #555;">
                Early detection of brain cancer, including tumors such as meningiomas and other types, is made possible through AI-powered analysis of CT and MRI scans. This enables timely diagnosis, allowing for treatment to begin before the tumor progresses.
            </p>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# Initialize session state
if "prediction" not in st.session_state:
    st.session_state.prediction = None

# Create two columns for layout
col1, col2 = st.columns([2,3], gap="large", vertical_alignment="top")

# Column 1: Display model image and prediction text
with col1:
    st.markdown(
    f"""
    <div class='model-box'">
        <div style="font-size: 24px; font-weight: bold; margin-bottom: 10px; color: #000">Brain Tumor Detection</div>
        <img src="data:image/png;base64,{modelImage}" alt="Brain Tumor Icon" style="width: 100%; height: auto; border-radius: 12px">
    </div>
    """,
    unsafe_allow_html=True
)
    
    # Prediction text will be added after the image is uploaded
    prediction_text = st.session_state.prediction or "No prediction yet"
    st.markdown(
        f"""
        <div class="prediction-box">
            <h4>Prediction: <span>{prediction_text}</span></h4>
        </div>
        """,
        unsafe_allow_html=True
    )

# Column 2: Image upload and preview
with col2:
    image_file = st.file_uploader("Upload MRI Image", type=["jpg", "png", "jpeg"])
    
    if image_file:
        image = Image.open(image_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        
        # Process the image for prediction
        img_array = preprocess_image(image)
        prediction = brain_tumor_model.predict(img_array)
        predicted_class = brain_tumor_classes[np.argmax(prediction)]
        
        # Store the prediction in session_state to display in column 1
        if st.session_state.prediction != predicted_class:
            st.session_state.prediction = predicted_class
            st.experimental_rerun()
