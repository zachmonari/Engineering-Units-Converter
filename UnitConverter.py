# converter.py

def convert_length(value, from_unit, to_unit):
    length_units = {
        'm': 1,
        'cm': 0.01,
        'mm': 0.001,
        'inch': 0.0254,
        'ft': 0.3048
    }
    return value * (length_units[from_unit] / length_units[to_unit])


def convert_force(value, from_unit, to_unit):
    force_units = {
        'N': 1,
        'kN': 1000,
        'lbf': 4.44822
    }
    return value * (force_units[from_unit] / force_units[to_unit])


def convert_pressure(value, from_unit, to_unit):
    pressure_units = {
        'Pa': 1,
        'kPa': 1000,
        'bar': 100000,
        'psi': 6894.76
    }
    return value * (pressure_units[from_unit] / pressure_units[to_unit])


def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == 'C':
        return value * 9 / 5 + 32 if to_unit == 'F' else value + 273.15
    if from_unit == 'F':
        return (value - 32) * 5 / 9 if to_unit == 'C' else (value - 32) * 5 / 9 + 273.15
    if from_unit == 'K':
        return value - 273.15 if to_unit == 'C' else (value - 273.15) * 9 / 5 + 32


def convert_torque(value, from_unit, to_unit):
    torque_units = {
        'N·m': 1,
        'kgf·m': 9.80665,
        'lbf·ft': 1.35582
    }
    return value * (torque_units[from_unit] / torque_units[to_unit])


def main():
    print("⚙️ Engineering Unit Converter ⚙️")
    print("Available categories: length, force, pressure, temperature, torque")

    category = input("Enter category: ").lower()
    value = float(input("Enter value to convert: "))
    from_unit = input("From unit: ")
    to_unit = input("To unit: ")

    try:
        if category == 'length':
            result = convert_length(value, from_unit, to_unit)
        elif category == 'force':
            result = convert_force(value, from_unit, to_unit)
        elif category == 'pressure':
            result = convert_pressure(value, from_unit, to_unit)
        elif category == 'temperature':
            result = convert_temperature(value, from_unit, to_unit)
        elif category == 'torque':
            result = convert_torque(value, from_unit, to_unit)
        else:
            print("❌ Unknown category.")
            return

        print(f"\n✅ {value} {from_unit} = {result:.4f} {to_unit}")
    except KeyError:
        print("⚠️ Invalid unit entered. Please check your input.")


if __name__ == "__main__":
    main()
