import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Page configuration
st.set_page_config(page_title="🎯 Ball Mill Parameter Predictor", page_icon="⚙️")
st.title("⚙️ Ball Mill Parameter Prediction")
st.markdown("Enter the percentage of each input material below. The total must be exactly **100%**.")

# Load the trained model
model = joblib.load("ball_mill_model.pkl")  # Ensure this file exists in the same directory

# Input fields
st.subheader("🧪 Input Materials")
rh = st.number_input("RH", min_value=0.0, max_value=100.0, value=0.0)
oxide = st.number_input("Oxide ", min_value=0.0, max_value=100.0, value=0.0)
crushed_odisha = st.number_input("Crushed Odisha", min_value=0.0, max_value=100.0, value=0.0)
nmdc = st.number_input("NMDC", min_value=0.0, max_value=100.0, value=0.0)
odisha = st.number_input("Odisha", min_value=0.0, max_value=100.0, value=0.0)
vale_brbf = st.number_input("VALE BRBF", min_value=0.0, max_value=100.0, value=0.0)
vale_iocj = st.number_input("Vale IOCJ", min_value=0.0, max_value=100.0, value=0.0)
mel = st.number_input("MEL", min_value=0.0, max_value=100.0, value=0.0)

# Total sum validation
total = rh + oxide + crushed_odisha + nmdc + odisha + vale_brbf + vale_iocj + mel
st.markdown(f"**🔢 Total Input: {total:.2f}%**")

if total != 100.0:
    st.error("🚫 Total input must be exactly 100%. Please adjust the values.")
else:
    if st.button("🎯 Predict Mill Parameters"):
        # Prepare input data
        input_data = pd.DataFrame([[
            rh, oxide, crushed_odisha, nmdc, odisha, vale_brbf, vale_iocj, mel
        ]], columns=[
            "RH", "Oxide ", "Crushed odisha", "NMDC", "Odisha",
            "VALE BRBF", "Vale IOCJ", "MEL"
        ])

        # Make prediction
        prediction = model.predict(input_data)[0]

        # Display results
        st.success("✅ Prediction Complete!")
        st.markdown(f"""
        ### 📊 Predicted Parameters:
        - **Feed (TPH):** {prediction[0]:.2f}
        - **Feed Water:** {prediction[1]:.2f}
        - **Cyclone Pressure:** {prediction[2]:.2f}
        """)
