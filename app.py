import pickle
import streamlit as st
import numpy as np
from sklearn.pipeline import make_pipeline 
from sklearn.preprocessing import PolynomialFeatures 
from sklearn.linear_model import LinearRegression
# Set up the web page
st.set_page_config(
page_title="Machine Output Predictor",
page_icon="⚙️", 
layout="centered"
)
st.title(
"⚙️ Machine Output Predictor")
st.write("Predict machine output based on temperature "
"using Polynomial Regression."
)
X = np.array([ [10], [15], [20], [25], [30], [35], [40] ])
y = np.array([ 36, 64, 84, 96, 100, 96, 84 ])
# 4. Create and train the ML model
model = make_pipeline(
    PolynomialFeatures(degree=2),
    LinearRegression()
)
model.fit(X, y)
# 5. Display dataset
with st.expander("📊 View Training Dataset"):
    st.dataframe(
        { 
            "Temperature": X.flatten(),
            "Machine_Output": y
        },
        use_container_width=True
    )
# Take input from the user
st.subheader("🌡️ Enter Machine Temperature")

temperature = st.number_input(
"Temperature",
min_value=10.0, 
max_value=40.0, 
value=30.0, 
step=1.0
)
Temperature = st.number_input("Enter the Temperature value:", value=0.0)
# Predict when the button is click
if st.button("Predict Machine Output", use_container_width=True):
    # Prepare input data
    input_data = np.array([[Temperature]])
    prediction = model.predict(input_data)[0]
    st.success("Prediction completed successfully!")
    predicted_marks = max(0.0, min(100.0, prediction))
    #Display prediction results
    st.success("Prediction Completed!")
    st.metric(
        label="⚙️ Predicted Machine Output", 
        value=f"{predicted_output:.2f} / 100"
    )
    st.write(f"🌡️ Temperature: {temperature:.1f}")
    st.write( f"⚙️ Predicted Machine Output: {predicted_output:.2f}")
    # Display performance message
    if predicted_output >= 90: 
        st.info("Excellent machine output! 🌟")
    elif predicted_output >= 70: 
        st.info("Good machine output! 👍")
    elif predicted_output >= 40: 
        st.info("Moderate machine output. ⚙️")
    else: 
        st.warning("Low machine output. Check the operating conditions.")
st.divider()
st.caption("⚙️ Machine Output Prediction App")
