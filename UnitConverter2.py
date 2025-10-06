# converter_v3.py

def convert_length(value, from_unit, to_unit):
    units = {'m': 1, 'cm': 0.01, 'mm': 0.001, 'inch': 0.0254, 'ft': 0.3048}
    return value * (units[from_unit] / units[to_unit])

def convert_force(value, from_unit, to_unit):
    units = {'N': 1, 'kN': 1000, 'lbf': 4.44822}
    return value * (units[from_unit] / units[to_unit])

def convert_pressure(value, from_unit, to_unit):
    units = {'Pa': 1, 'kPa': 1000, 'bar': 100000, 'psi': 6894.76}
    return value * (units[from_unit] / units[to_unit])

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == 'C':
        return value * 9/5 + 32 if to_unit == 'F' else value + 273.15
    if from_unit == 'F':
        return (value - 32) * 5/9 if to_unit == 'C' else (value - 32) * 5/9 + 273.15
    if from_unit == 'K':
        return value - 273.15 if to_unit == 'C' else (value - 273.15) * 9/5 + 32

def convert_torque(value, from_unit, to_unit):
    units = {'N·m': 1, 'kgf·m': 9.80665, 'lbf·ft': 1.35582}
    return value * (units[from_unit] / units[to_unit])

def convert_mass(value, from_unit, to_unit):
    units = {'kg': 1, 'g': 0.001, 'lb': 0.453592, 'tonne': 1000}
    return value * (units[from_unit] / units[to_unit])

def convert_volume(value, from_unit, to_unit):
    units = {'m3': 1, 'L': 0.001, 'cm3': 1e-6, 'in3': 1.6387e-5}
    return value * (units[from_unit] / units[to_unit])

def convert_power(value, from_unit, to_unit):
    units = {'W': 1, 'kW': 1000, 'hp': 745.7}
    return value * (units[from_unit] / units[to_unit])

def convert_energy(value, from_unit, to_unit):
    units = {'J': 1, 'kJ': 1000, 'cal': 4.184, 'kWh': 3.6e6}
    return value * (units[from_unit] / units[to_unit])


# Hints dictionary
UNIT_HINTS = {
    'length': ['m', 'cm', 'mm', 'inch', 'ft'],
    'force': ['N', 'kN', 'lbf'],
    'pressure': ['Pa', 'kPa', 'bar', 'psi'],
    'temperature': ['C', 'F', 'K'],
    'torque': ['N·m', 'kgf·m', 'lbf·ft'],
    'mass': ['kg', 'g', 'lb', 'tonne'],
    'volume': ['m3', 'L', 'cm3', 'in3'],
    'power': ['W', 'kW', 'hp'],
    'energy': ['J', 'kJ', 'cal', 'kWh']
}


def show_categories():
    print("\nAvailable categories:")
    print("1. Length")
    print("2. Force")
    print("3. Pressure")
    print("4. Temperature")
    print("5. Torque")
    print("6. Mass")
    print("7. Volume")
    print("8. Power")
    print("9. Energy")
    print("0. Exit")


def main():
    print("⚙️ ENGINEERING UNIT CONVERTER v3 ⚙️")

    while True:
        show_categories()
        choice = input("\nSelect a category number (0 to exit): ").strip()

        if choice == '0':
            print("\n👋 Exiting... Goodbye!")
            break

        categories = {
            '1': ('length', convert_length),
            '2': ('force', convert_force),
            '3': ('pressure', convert_pressure),
            '4': ('temperature', convert_temperature),
            '5': ('torque', convert_torque),
            '6': ('mass', convert_mass),
            '7': ('volume', convert_volume),
            '8': ('power', convert_power),
            '9': ('energy', convert_energy),
        }

        if choice not in categories:
            print("❌ Invalid choice. Try again.")
            continue

        cat_name, func = categories[choice]
        available_units = ', '.join(UNIT_HINTS[cat_name])
        print(f"\nAvailable units for {cat_name}: {available_units}")

        try:
            value = float(input(f"Enter value to convert ({cat_name}): "))
            from_unit = input("From unit: ").strip()
            to_unit = input("To unit: ").strip()
            result = func(value, from_unit, to_unit)
            print(f"✅ {value} {from_unit} = {result:.6f} {to_unit}\n")
        except KeyError:
            print("⚠️ Invalid unit. Check spelling or case.\n")
        except ValueError:
            print("⚠️ Please enter a numeric value.\n")
        except Exception as e:
            print(f"⚠️ Error: {e}\n")


if __name__ == "__main__":
    main()
