import streamlit as st

# Custom CSS for better UI styling
st.markdown("""
    <style>
    .stSelectbox, .stNumberInput { 
         background: linear-gradient(45deg, #0ce39a, #69007f, #fc0987); !important; 
        padding: 10px; 
        border-radius: 5px;
    }
    .stButton>button { 
     background: yellow; !important; 
        color: black; 
        font-size: 18px;
        border-radius: 5px;
        padding: 10px 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Title and description
st.markdown("<h1 style='text-align: center;   background: linear-gradient(115deg,#4fcf70,#fad648,#a767e5,#12bcfe,#44ce7b);'>Unit Converter 🔄📏⚖️🌡️</h1>", unsafe_allow_html=True)

st.markdown("""
    <p style='text-align: center; font-size: 18px; color: white;'>
    This is a simple unit converter app built using Streamlit.<br>
    It allows you to convert between different units of measurement, such as length, mass, and time.
    </p>
""", unsafe_allow_html=True)

st.write(" ###  Welcome! Please select the units you want to convert.")


category = st.selectbox("Choose a category", ["Length", "Weight", "Time"])


def convert_units(category, value, unit):
    if category == "Length":
        if unit == "Kilometers to Meters":
            return value * 1000
        elif unit == "Meters to Kilometers":
            return value / 1000
    elif category == "Weight":
        if unit == "Kilogram to Lbs":
            return value * 2.20462
        elif unit == "Lbs to Kilograms":
            return value / 2.20462
    elif category == "Time":
        if unit == "Seconds to Minutes":
            return value / 60
        elif unit == "Minutes to Seconds":
            return value * 60
        elif unit == "Hours to Minutes":
            return value * 60
        elif unit == "Minutes to Hours":
            return value / 60
        elif unit == "Days to Hours":
            return value * 24
        elif unit == "Hours to Days":
            return value / 24


if category == "Length":
    unit = st.selectbox("Choose a unit", ["Kilometers to Meters", "Meters to Kilometers"])
elif category == "Weight":
    unit = st.selectbox("Choose a unit", ["Kilogram to Lbs", "Lbs to Kilograms"])
elif category == "Time":
    unit = st.selectbox("Choose a unit", ["Seconds to Minutes", "Minutes to Seconds", "Hours to Minutes", "Minutes to Hours", "Days to Hours", "Hours to Days"])

value = st.number_input("Enter the value to convert", min_value=0.0, format="%.2f")


if st.button("Convert"):
    result = convert_units(category, value, unit)
    st.success(f"The result is {result:.2f}")
