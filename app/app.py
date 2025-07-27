import streamlit as st 
import pandas as pd 
import joblib 

# Title 
st.title("Real Estate Price Predictor")

# File upload
uploaded_file = st.file_uploader("Upload your CSV file", type = ["csv"])

if uploaded_file is not None: 
    #Load the data 
    input_df = pd.read_csv(uploaded_file)
    st.write("### Preview of uploaded data", input_df.head())

    try:
        # Load the trained pipeline 
        pipeline = joblib.load("pipeline.pkl")

        # Predict 
        predictions = pipeline.predict(input_df)

        # Output 
        input_df["Predicted Price"] = predictions
        st.write("### Predictions", input_df)

        # Download
        csv = input_df.to_csv(index = False).encode('utf-8')
        st.download_button("Download predictions as CSV", csv, "predictions.csv", "text/csv")
    
    except Exception as e: 
        st.error(f"Error: {e}")
