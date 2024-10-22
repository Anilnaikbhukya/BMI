import streamlit as st

# Title
st.title("BMI Calculator")

# Description
st.write("""
### Calculate your Body Mass Index (BMI)
BMI is a measure of body fat based on height and weight that applies to adult men and women.
""")

# Input fields
weight = st.number_input("Enter your weight (in kg):", min_value=0.0, step=0.1)
height = st.number_input("Enter your height (in cm):", min_value=0.0, step=0.1)

# Button to calculate BMI
if st.button("Calculate BMI"):
    if height > 0 and weight > 0:
        # Convert height from cm to meters
        height_m = height / 100
        # Calculate BMI
        bmi = weight / (height_m ** 2)

        # Display BMI
        st.write(f"Your BMI is: {bmi:.2f}")

        # Interpretation of BMI
        if bmi < 18.5:
            st.write("You are underweight.")
        elif 18.5 <= bmi < 24.9:
            st.write("You have a normal weight.")
        elif 25 <= bmi < 29.9:
            st.write("You are overweight.")
        else:
            st.write("You are obese.")
    else:
        st.write("Please enter valid weight and height.")
