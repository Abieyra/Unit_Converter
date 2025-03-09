import streamlit as st

st.title("Unit Converter")

# Distance Conversion Function
def distance_converter(from_unit, to_unit, value):
    units = {
        "Meters": 1,
        "Kilometers": 1000,
        "Miles": 1609.34,
        "Feet": 0.3048,
    }
    return value * units[from_unit] / units[to_unit]

# Temperature Conversion Function
def temperature_converter(from_unit, to_unit, value):
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        result = (value * 9/5) + 32
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        result = (value - 32) * 5/9
    else:
        result = value
    return result

# Weight Conversion Function
def weight_converter(from_unit, to_unit, value):
    units = {
        "Grams": 1,
        "Kilograms": 0.001,
        "Pounds": 0.453592,
        "Ounces": 0.0283495
    }
    return value * units[from_unit] / units[to_unit]

# Pressure Conversion Function
def pressure_converter(from_unit, to_unit, value):
    units = {
        "Pascals": 1,
        "Hectopascals": 100, 
        "Kilopascals": 1000,
        "Bars": 100000,
    }
    return value * units[from_unit] / units[to_unit]

# Main App Logic
category = st.selectbox("Select category", ["Distance", "Weight", "Temperature", "Pressure"])

if category == "Distance":
    from_unit = st.selectbox("From", ["Meters", "Kilometers", "Miles", "Feet"])
    to_unit = st.selectbox("To", ["Meters", "Kilometers", "Miles", "Feet"])
    value = st.number_input("Enter value")
    if st.button("Convert"):
        result = distance_converter(from_unit, to_unit, value)
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")

elif category == "Temperature":
    from_unit = st.selectbox("From", ["Celsius", "Fahrenheit"])
    to_unit = st.selectbox("To", ["Celsius", "Fahrenheit"])
    value = st.number_input("Enter value")
    if st.button("Convert"):
        result = temperature_converter(from_unit, to_unit, value)
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")

elif category == "Weight":
    from_unit = st.selectbox("From", ["Grams", "Kilograms", "Pounds", "Ounces"])
    to_unit = st.selectbox("To", ["Grams", "Kilograms", "Pounds", "Ounces"])
    value = st.number_input("Enter value")
    if st.button("Convert"):
        result = weight_converter(from_unit, to_unit, value)
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")

elif category == "Pressure":
    from_unit = st.selectbox("From", ["Pascals", "Hectopascals", "Kilopascals", "Bars"])
    to_unit = st.selectbox("To", ["Pascals", "Hectopascals", "Kilopascals", "Bars"])
    value = st.number_input("Enter value")
    if st.button("Convert"):
        result = pressure_converter(from_unit, to_unit, value)
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")