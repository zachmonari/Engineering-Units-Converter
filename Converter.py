import logging

# ------------------------------
# 🔧 Configure Logging (UTF-8 Safe)
# ------------------------------
logging.basicConfig(
    filename="unit_converter.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"  # ensures Unicode like → works
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
    # Case-insensitive units
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

# ------------------------------
# 🧠 Main Program
# ------------------------------
def main():
    print("🧮 ENGINEERING UNIT CONVERTER")
    print("------------------------------------------------")

    while True:
        print("\nAvailable Categories:")
        for i, cat in enumerate(CONVERSIONS.keys(), 1):
            print(f"{i}. {cat.capitalize()}")
        print("0. Exit")

        try:
            choice = int(input("\nSelect a category number (0 to exit): "))
        except ValueError:
            print("⚠️ Please enter a valid number.")
            continue

        if choice == 0:
            print("👋 Goodbye!")
            break

        categories = list(CONVERSIONS.keys())
        if choice < 1 or choice > len(categories):
            print("⚠️ Invalid category. Try again.")
            continue

        category = categories[choice - 1]
        available_units = ", ".join(CONVERSIONS[category].keys())
        print(f"\nAvailable units for {category}: {available_units}")

        try:
            value = float(input(f"Enter value to convert ({category}): "))
            from_unit = input("From unit: ").strip()
            to_unit = input("To unit: ").strip()

            result = convert_value(value, from_unit, to_unit, category)

            print(f"✅ {value} {from_unit} = {result:.6f} {to_unit}")
            logging.info(f"{category.capitalize()}: {value} {from_unit} → {result:.6f} {to_unit}")

        except ValueError as e:
            print(f"⚠️ Error: {e}")
            logging.warning(f"Conversion error in {category}: {e}")
        except Exception as e:
            print(f"⚠️ Unexpected error: {e}")
            logging.error(f"Unexpected error: {e}")

# ------------------------------
# 🚀 Run
# ------------------------------
if __name__ == "__main__":
    main()
