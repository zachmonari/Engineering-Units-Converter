import streamlit as st
import logging

# --------------------------------
# ⚙️ Configure Logging
# --------------------------------
logging.basicConfig(
    filename="unit_converter.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

# --------------------------------
# 🧩 Conversion Data
# --------------------------------
CONVERSIONS = {
    "Length": {"m": 1, "cm": 0.01, "mm": 0.001, "km": 1000, "in": 0.0254, "ft": 0.3048},
    "Mass": {"kg": 1, "g": 0.001, "lb": 0.453592, "tonne": 1000},
    "Force": {"n": 1, "kn": 1000, "lbf": 4.44822},
    "Pressure": {"pa": 1, "kpa": 1000, "bar": 1e5, "psi": 6894.76},
    "Volume": {"m3": 1, "l": 0.001, "cm3": 1e-6, "in3": 1.6387e-5},
    "Energy": {"j": 1, "kj": 1000, "mj": 1e6, "wh": 3600, "kwh": 3.6e6},
    "Power": {"w": 1, "kw": 1000, "mw": 1e6, "hp": 745.7},
    "Temperature": {"c": "Celsius", "f": "Fahrenheit", "k": "Kelvin"}
}

# --------------------------------
# 🔄 Conversion Functions
# --------------------------------
def convert_value(value, from_unit, to_unit, category):
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    if category == "Temperature":
        return convert_temperature(value, from_unit, to_unit)

    units = CONVERSIONS[category]
    if from_unit not in units or to_unit not in units:
        raise ValueError("Invalid unit entered.")
    return value * (units[from_unit] / units[to_unit])

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value

    # Convert to Celsius first
    if from_unit == "f":
        value = (value - 32) * 5 / 9
    elif from_unit == "k":
        value = value - 273.15

    # Convert from Celsius to target
    if to_unit == "f":
        return (value * 9 / 5) + 32
    elif to_unit == "k":
        return value + 273.15
    else:
        return value

# --------------------------------
# 🌐 Streamlit UI
# --------------------------------
st.set_page_config(page_title="Engineering Unit Converter", page_icon="🧮", layout="centered")

st.title("🧮 Engineering Unit Converter")
st.write("Convert between different engineering units — length, mass, force, pressure, temperature, and more!")

category = st.selectbox("Select a category:", list(CONVERSIONS.keys()))

units = list(CONVERSIONS[category].keys())
col1, col2 = st.columns(2)
with col1:
    from_unit = st.selectbox("From unit:", units)
with col2:
    to_unit = st.selectbox("To unit:", units)

value = st.number_input(f"Enter value to convert ({category}):", min_value=0.0, format="%.6f")

if st.button("🔁 Convert"):
    try:
        result = convert_value(value, from_unit, to_unit, category)
        st.success(f"✅ {value} {from_unit} = {result:.6f} {to_unit}")
        logging.info(f"{category}: {value} {from_unit} → {result:.6f} {to_unit}")
    except Exception as e:
        st.error(f"⚠️ Error: {e}")
        logging.warning(f"Conversion error: {e}")

# --------------------------------
# 📜 Optional Log Viewer
# --------------------------------
with st.expander("📜 View Recent Conversion Logs"):
    try:
        with open("unit_converter.log", "r", encoding="utf-8") as log_file:
            logs = log_file.readlines()[-10:]  # show last 10 logs
            for entry in logs:
                st.text(entry.strip())
    except FileNotFoundError:
        st.info("No logs available yet.")
# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align:center; color:black;'>© 2025 Zach Techs | Made with ❤️ in Streamlit</div>",
    unsafe_allow_html=True
)