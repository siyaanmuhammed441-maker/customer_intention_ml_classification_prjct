import streamlit as st

st.write("APP STARTED")

import joblib

try:
    model = joblib.load("online_shopper_model.pkl")
    st.success("Model loaded")
except Exception as e:
    st.error(f"Model Error: {e}")
    st.stop()
import streamlit as st
import pandas as pd
import joblib

# ==========================
# Load Saved Model & Encoders
# ==========================
model = joblib.load("online_shopper_model.pkl")
month_encoder = joblib.load("month_encoder.pkl")
visitor_encoder = joblib.load("visitor_encoder.pkl")

# ==========================
# Page Configuration
# ==========================
st.set_page_config(
    page_title="Online Shopper Purchase Prediction",
    page_icon="🛒",
    layout="wide"
)

# ==========================
# Business Analytics CSS
# ==========================
st.markdown("""
<style>

/* =========================
   BUSINESS ANALYTICS THEME
========================= */

/* Main Background */
.stApp {
    background: linear-gradient(
        135deg,
        #f8fafc 0%,
        #dbeafe 50%,
        #bfdbfe 100%
    );
}

/* Main Container */
.main-box {
    background-color: rgba(255,255,255,0.96);
    padding: 30px;
    border-radius: 15px;
    box-shadow: 0px 5px 20px rgba(0,0,0,0.1);
}

/* Global Text */
html, body, p, div, label {
    color: black !important;
}

/* Titles */
h1{
    color:#0f172a !important;
    text-align:center;
    font-weight:700;
}

h2,h3{
    color:#1e293b !important;
}

/* =========================
   SIDEBAR
========================= */

section[data-testid="stSidebar"]{
    background-color:white !important;
    border-right:2px solid #dbeafe;
}

/* Sidebar text */
section[data-testid="stSidebar"] *{
    color:black !important;
}

/* =========================
   SELECTBOX
========================= */

/* Main selectbox */
div[data-baseweb="select"] > div{
    background-color:white !important;
    color:black !important;
    border:1px solid #cbd5e1 !important;
}

/* Selected value */
div[data-baseweb="select"] span{
    color:black !important;
}

/* Dropdown menu */
ul[role="listbox"]{
    background-color:white !important;
}

/* Dropdown options */
li[role="option"]{
    background-color:white !important;
    color:black !important;
}

/* Hover option */
li[role="option"]:hover{
    background-color:#dbeafe !important;
}

/* =========================
   RADIO BUTTON
========================= */

div[role="radiogroup"] label{
    color:black !important;
}

/* =========================
   INPUT BOXES
========================= */

input{
    background-color:white !important;
    color:black !important;
}

/* =========================
   SLIDER
========================= */

.stSlider label{
    color:black !important;
}

/* =========================
   DATAFRAME
========================= */

[data-testid="stDataFrame"]{
    background-color:white !important;
}

/* =========================
   METRIC
========================= */

[data-testid="stMetricValue"]{
    color:black !important;
    font-weight:bold;
}

/* =========================
   BUTTON
========================= */

.stButton > button{
    background-color:#2563eb;
    color:white !important;
    border:none;
    border-radius:10px;
    font-size:16px;
    font-weight:bold;
    padding:10px 25px;
}

.stButton > button:hover{
    background-color:#1d4ed8;
    color:white !important;
}

/* =========================
   TABLE
========================= */

table{
    color:black !important;
}

</style>
""", unsafe_allow_html=True)
# ==========================
# Main Container
# ==========================
st.markdown('<div class="main-box">', unsafe_allow_html=True)

# ==========================
# Header
# ==========================
st.title("🛒 Online Shopper Purchase Prediction")

st.markdown("""
### Predict Customer Purchase Intention

This machine learning application predicts whether an online visitor is likely to make a purchase based on browsing behavior.
""")

# ==========================
# Sidebar Inputs
# ==========================
st.sidebar.header("Customer Browsing Information")

ProductRelated = st.sidebar.slider(
    "Product Pages Visited",
    0, 800, 50
)

ProductRelated_Duration = st.sidebar.slider(
    "Time Spent on Product Pages",
    0.0, 6000.0, 1500.0
)

PageValues = st.sidebar.slider(
    "Page Value",
    0.0, 400.0, 20.0
)

BounceRates = st.sidebar.slider(
    "Bounce Rate",
    0.0, 0.20, 0.02
)

ExitRates = st.sidebar.slider(
    "Exit Rate",
    0.0, 0.20, 0.04
)

VisitorType = st.sidebar.selectbox(
    "Visitor Type",
    visitor_encoder.classes_
)

Month = st.sidebar.selectbox(
    "Month",
    month_encoder.classes_
)

Weekend = st.sidebar.radio(
    "Weekend Visit",
    ["No", "Yes"]
)

# ==========================
# Encoding
# ==========================
VisitorType_encoded = visitor_encoder.transform([VisitorType])[0]
Month_encoded = month_encoder.transform([Month])[0]
Weekend_encoded = 1 if Weekend == "Yes" else 0

# ==========================
# Input Data
# ==========================
input_data = pd.DataFrame({
    "ProductRelated": [ProductRelated],
    "ProductRelated_Duration": [ProductRelated_Duration],
    "PageValues": [PageValues],
    "BounceRates": [BounceRates],
    "ExitRates": [ExitRates],
    "VisitorType": [VisitorType_encoded],
    "Weekend": [Weekend_encoded],
    "Month": [Month_encoded]
})

# ==========================
# Display Inputs
# ==========================
col1, col2 = st.columns(2)

with col1:
    st.subheader("📋 Input Summary")
    st.dataframe(input_data)

with col2:
    st.subheader("📊 Visitor Information")

    st.write(f"**Visitor Type:** {VisitorType}")
    st.write(f"**Month:** {Month}")
    st.write(f"**Weekend Visit:** {Weekend}")
    st.write(f"**Product Pages Visited:** {ProductRelated}")

st.divider()

# ==========================
# Prediction Button
# ==========================
if st.button("🔮 Predict Purchase Intention"):

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1] * 100

    st.subheader("Prediction Result")

    # Prediction Message
    if prediction == 1:
        st.success("✅ Customer is likely to make a purchase.")
    else:
        st.error("❌ Customer is unlikely to make a purchase.")

    # Probability Metric
    st.metric(
        label="Purchase Probability",
        value=f"{probability:.2f}%"
    )

    # Risk Analysis
    st.subheader("📈 Customer Analysis")

    if probability >= 70:
        st.success(
            "High Purchase Potential: Recommend personalized offers and premium products."
        )

    elif probability >= 40:
        st.warning(
            "Medium Purchase Potential: Retargeting campaigns may improve conversions."
        )

    else:
        st.info(
            "Low Purchase Potential: Increase engagement through discounts and promotions."
        )

    # Final Output Table
    result_df = pd.DataFrame({
        "Prediction": [
            "Purchase" if prediction == 1 else "No Purchase"
        ],
        "Probability": [
            f"{probability:.2f}%"
        ]
    })

    st.subheader("📌 Final Prediction")
    st.table(result_df)

# ==========================
# Footer
# ==========================
st.markdown("---")
st.markdown(
    '<p class="footer">Developed using Machine Learning, Random Forest & Streamlit</p>',
    unsafe_allow_html=True
)

st.markdown('</div>', unsafe_allow_html=True)