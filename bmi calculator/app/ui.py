import streamlit as st
from logic import calculate_bmi
from storage import save_to_csv

def run():
    st.title("BMI CALCULATOR")
    weight = st.number_input("Enter your wight (kg): ",min_value=1.0)
    height = st.number_input("Enter your height (cm): ",min_value=1.0)

    if st.button("Calculate"):
        bmi = calculate_bmi(weight, height)
        st.success(f"Your BMI is {bmi}")
        save_to_csv(weight, height, bmi)


run()
