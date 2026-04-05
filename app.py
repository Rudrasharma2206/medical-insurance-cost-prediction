import streamlit as st
import pandas as pd
import pickle
import os
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder

st.set_page_config(page_title="Medical Insurance Cost Predictor", page_icon="🏥")

st.title("🏥 Medical Insurance Cost Predictor")
st.write("Fill in the details below to predict your insurance charges.")

MODEL_PATH = "model.pkl"

@st.cache_resource
def load_or_train_model():
    if os.path.exists(MODEL_PATH):
        with open(MODEL_PATH, "rb") as f:
            return pickle.load(f)

    # Train from CSV if model not saved yet
    DATA_PATH = "data/insurance.csv"
    if not os.path.exists(DATA_PATH):
        st.error("Model file not found and data/insurance.csv is missing. "
                 "Please place insurance.csv in the data/ folder.")
        st.stop()

    df = pd.read_csv(DATA_PATH)
    df["sex"]    = LabelEncoder().fit_transform(df["sex"])
    df["smoker"] = LabelEncoder().fit_transform(df["smoker"])
    df["region"] = LabelEncoder().fit_transform(df["region"])

    X = df.drop("charges", axis=1)
    y = df["charges"]

    model = LinearRegression()
    model.fit(X, y)

    with open(MODEL_PATH, "wb") as f:
        pickle.dump(model, f)
    return model

model = load_or_train_model()
st.subheader("Enter Your Details")

col1, col2 = st.columns(2)

with col1:
    age      = st.slider("Age",            min_value=18, max_value=100, value=30)
    bmi      = st.slider("BMI",            min_value=10.0, max_value=60.0, value=25.0, step=0.1)
    children = st.slider("No. of Children", min_value=0, max_value=10, value=0)

with col2:
    sex    = st.selectbox("Sex",    ["male", "female"])
    smoker = st.selectbox("Smoker", ["no", "yes"])
    region = st.selectbox("Region", ["southwest", "southeast", "northwest", "northeast"])

sex_enc    = 1 if sex    == "male"      else 0
smoker_enc = 1 if smoker == "yes"       else 0
region_map = {"southwest": 3, "southeast": 2, "northwest": 1, "northeast": 0}
region_enc = region_map[region]

input_data = pd.DataFrame([[age, sex_enc, bmi, children, smoker_enc, region_enc]],
                           columns=["age", "sex", "bmi", "children", "smoker", "region"])

if st.button("Predict Insurance Cost", use_container_width=True):
    prediction = model.predict(input_data)[0]
    st.success(f"### Estimated Insurance Cost: **${prediction:,.2f}**")

    st.subheader("Your Input Summary")
    summary = {
        "Age": age, "Sex": sex, "BMI": bmi,
        "Children": children, "Smoker": smoker, "Region": region
    }
    st.table(pd.DataFrame(summary, index=["Value"]).T)