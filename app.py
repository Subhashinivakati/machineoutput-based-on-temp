import pickle
import streamlit as st
import numpy as np
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

# Load the saved ML model
with open("machineoutput_model.pkl", "rb") as file:
    model = pickle.load(file)

# Take input from the user
st.subheader("🌡️ Enter Machine Temperature")

temperature = st.number_input(
"Temperature",
min_value=10.0, 
max_value=40.0, 
value=30.0, 
step=1.0
)
st.info(
f"Selected temperature: {temperature:.1f}" 
)
# Predict when the button is click
if st.button("Predict Machine Output", use_container_width=True):
    # Prepare input data
    input_data = np.array([[temperature]])
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
