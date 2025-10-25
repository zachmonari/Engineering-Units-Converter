import streamlit as st
import logging

# ------------------------------
# 🔧 Configure Logging (UTF-8 Safe)
# ------------------------------
logging.basicConfig(
    filename="unit_converter.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

# ------------------------------
# ⚙️ Conversion Dictionaries
# ------------------------------
CONVERSIONS = {
    "length": {"m": 1, "cm": 0.01, "mm": 0.001, "km": 1000, "in": 0.0254, "ft": 0.3048},
    "mass": {"kg": 1, "g": 0.001, "lb": 0.453592, "tonne": 1000},
    "force": {"n": 1, "kn": 1000, "lbf": 4.44822},
    "pressure": {"pa": 1, "kpa": 1000, "bar": 1e5, "psi": 6894.76},
    "volume": {"m3": 1, "l": 0.001, "cm3": 1e-6, "in3": 1.6387e-5},
    "energy": {"j": 1, "kj": 1000, "mj": 1e6, "wh": 3600, "kwh": 3.6e6},
    "power": {"w": 1, "kw": 1000, "mw": 1e6, "hp": 745.7},
    "temperature": {"c": "Celsius", "f": "Fahrenheit", "k": "Kelvin"}
}

# ------------------------------
# 🔄 Conversion Functions
# ------------------------------
def convert_value(value, from_unit, to_unit, category):
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    if category == "temperature":
        return convert_temperature(value, from_unit, to_unit)

    units = CONVERSIONS[category]
    if from_unit not in units or to_unit not in units:
        raise ValueError("Invalid unit entered.")
    return value * (units[from_unit] / units[to_unit])

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == "f":
        value = (value - 32) * 5 / 9
    elif from_unit == "k":
        value = value - 273.15
    if to_unit == "f":
        return (value * 9 / 5) + 32
    elif to_unit == "k":
        return value + 273.15
    else:
        return value

# ------------------------------
# 🌈 Streamlit UI Setup
# ------------------------------
st.set_page_config(page_title="⚙️ Engineering Unit Converter", page_icon="🌡️", layout="centered")

st.markdown("""
<style>
body {
    background: linear-gradient(to right, #89f7fe, #66a6ff);
    color: #003366;
}
.stButton>button {
    background-color: #0066cc;
    color: white;
    font-weight: bold;
    border-radius: 10px;
    padding: 10px 24px;
    font-size: 16px;
    border: none;
}
.stButton>button:hover {
    background-color: #004999;
}
.footer {
    text-align:center;
    font-size:14px;
    color:#333;
    margin-top:40px;
}
</style>
""", unsafe_allow_html=True)

# ------------------------------
# 🔐 Session State
# ------------------------------
if "users" not in st.session_state:
    st.session_state.users = {}
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "current_user" not in st.session_state:
    st.session_state.current_user = None

# ------------------------------
# 🔑 Authentication Pages
# ------------------------------
def sign_up():
    st.image("https://cdn-icons-png.flaticon.com/512/747/747376.png", width=80)
    st.title("📝 Create Your Account")
    username = st.text_input("Choose a username:")
    password = st.text_input("Choose a password:", type="password")

    if st.button("Sign Up"):
        if username in st.session_state.users:
            st.error("⚠️ Username already exists!")
        elif not username or not password:
            st.warning("Please fill all fields.")
        else:
            st.session_state.users[username] = password
            st.success("✅ Account created successfully!")
            st.balloons()
            logging.info(f"New user registered: {username}")

def login():
    st.image("https://cdn-icons-png.flaticon.com/512/5087/5087579.png", width=80)
    st.title("🔑 Log In")
    username = st.text_input("Username:")
    password = st.text_input("Password:", type="password")

    if st.button("Log In"):
        if username in st.session_state.users and st.session_state.users[username] == password:
            st.session_state.logged_in = True
            st.session_state.current_user = username
            st.success(f"✅ Welcome back, {username}!")
            st.balloons()
            logging.info(f"{username} logged in.")
        else:
            st.error("❌ Invalid username or password.")
            logging.warning(f"Failed login attempt for {username}")

# ------------------------------
# 🧮 Converter Page
# ------------------------------
def unit_converter():
    st.image("https://cdn-icons-png.flaticon.com/512/4781/4781517.png", width=100)
    st.title("⚙️ Engineering Unit Converter")
    st.write(f"👋 Hello, **{st.session_state.current_user}**! Ready to convert?")

    category = st.selectbox("Select Category:", list(CONVERSIONS.keys()))
    available_units = list(CONVERSIONS[category].keys())

    from_unit = st.selectbox("From Unit:", available_units)
    to_unit = st.selectbox("To Unit:", available_units)
    value = st.number_input("Enter Value:", value=0.0)

    if st.button("Convert"):
        try:
            result = convert_value(value, from_unit, to_unit, category)
            st.success(f"✅ {value} {from_unit} = {result:.6f} {to_unit}")
            logging.info(f"{category.capitalize()}: {value} {from_unit} → {result:.6f} {to_unit} by {st.session_state.current_user}")
        except ValueError as e:
            st.error(f"⚠️ Error: {e}")
            logging.warning(f"Conversion error by {st.session_state.current_user}: {e}")
        except Exception as e:
            st.error(f"⚠️ Unexpected error: {e}")
            logging.error(f"Unexpected error: {e}")

    if st.button("Log Out"):
        st.session_state.logged_in = False
        st.session_state.current_user = None
        st.success("👋 Logged out successfully.")
        logging.info("User logged out.")


# ------------------------------
# 🚀 App Flow
# ------------------------------
if not st.session_state.logged_in:
    choice = st.sidebar.radio("Navigation", ["Login", "Sign Up"])
    if choice == "Login":
        login()
    else:
        sign_up()
else:
    unit_converter()

# ------------------------------
# 🏁 Footer
# ------------------------------
st.markdown(
    """
    <div class='footer'>
        © 2025 <b>ZachTechs™</b> | Made with ❤️ for Engineers | All rights reserved.
    </div>
    """,
    unsafe_allow_html=True
)
