# converter_v2.py

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
        return value * 9/5 + 32 if to_unit == 'F' else value + 273.15
    if from_unit == 'F':
        return (value - 32) * 5/9 if to_unit == 'C' else (value - 32) * 5/9 + 273.15
    if from_unit == 'K':
        return value - 273.15 if to_unit == 'C' else (value - 273.15) * 9/5 + 32

def convert_torque(value, from_unit, to_unit):
    torque_units = {
        'N·m': 1,
        'kgf·m': 9.80665,
        'lbf·ft': 1.35582
    }
    return value * (torque_units[from_unit] / torque_units[to_unit])

def convert_mass(value, from_unit, to_unit):
    mass_units = {
        'kg': 1,
        'g': 0.001,
        'lb': 0.453592,
        'tonne': 1000
    }
    return value * (mass_units[from_unit] / mass_units[to_unit])

def convert_volume(value, from_unit, to_unit):
    volume_units = {
        'm3': 1,
        'L': 0.001,
        'cm3': 1e-6,
        'in3': 1.6387e-5
    }
    return value * (volume_units[from_unit] / volume_units[to_unit])

def convert_power(value, from_unit, to_unit):
    power_units = {
        'W': 1,
        'kW': 1000,
        'hp': 745.7
    }
    return value * (power_units[from_unit] / power_units[to_unit])

def convert_energy(value, from_unit, to_unit):
    energy_units = {
        'J': 1,
        'kJ': 1000,
        'cal': 4.184,
        'kWh': 3.6e6
    }
    return value * (energy_units[from_unit] / energy_units[to_unit])


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
    print("⚙️ ENGINEERING UNIT CONVERTER v2 ⚙️")

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

        try:
            value = float(input(f"\nEnter value to convert ({cat_name}): "))
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
