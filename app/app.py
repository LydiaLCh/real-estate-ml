import streamlit as st
import pandas as pd
import joblib

def add_time_features(df, date_column='Date'):
    df = df.copy()
    df[date_column] = pd.to_datetime(df[date_column], errors='coerce')
    df = df.dropna(subset=[date_column])
    df['Year'] = df[date_column].dt.year
    df['Month'] = df[date_column].dt.month
    df['DayOfYear'] = df[date_column].dt.dayofyear
    df['DayOfWeek'] = df[date_column].dt.dayofweek
    df['Quarter'] = df[date_column].dt.quarter
    return df.drop(columns=[date_column])

# Load the preprocessing pipeline and model once at app start
preprocessor = joblib.load('models/preprocessor.pkl')
model = joblib.load('models/model.pkl')

st.title("Real Estate Price Prediction")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    input_df = pd.read_csv(uploaded_file)
    st.write("### Uploaded Data Preview", input_df.head())

    if 'Date' not in input_df.columns:
        st.error("CSV must contain a 'Date' column for feature extraction.")
    else:
        try:
            # Add date/time features expected by your model
            processed_df = add_time_features(input_df, 'Date')

            # Apply preprocessing pipeline
            X_processed = preprocessor.transform(processed_df)

            # Predict with your trained model
            predictions = model.predict(X_processed)

            # Attach predictions to original data for display/download
            input_df['PredictedPrice'] = predictions

            st.subheader("Predicted Prices")
            st.write(input_df[['PredictedPrice']])

            csv = input_df.to_csv(index=False)
            st.download_button("Download Predictions CSV", csv, "predictions.csv")
        except Exception as e:
            st.error(f"Error during prediction: {e}")

            