import tkinter as tk
from tkinter import ttk

def convert_units():
    try:
        value = float(entry_value.get())
        from_unit = combo_from.get().lower()
        to_unit = combo_to.get().lower()

        if conversion_type.get() == "Temperature":
            result = convert_temperature(value, from_unit, to_unit)
        elif conversion_type.get() == "Length":
            result = convert_length(value, from_unit, to_unit)
        elif conversion_type.get() == "Weight":
            result = convert_weight(value, from_unit, to_unit)

        label_result.config(text=f"{value} {from_unit} is equal to {result:.2f} {to_unit}")

    except ValueError:
        label_result.config(text="Invalid input. Please enter a valid number for the value.")

def convert_temperature(value, from_unit, to_unit):
    if from_unit == "c" and to_unit == "f":
        return (value * 9/5) + 32
    elif from_unit == "f" and to_unit == "c":
        return (value - 32) * 5/9
    else:
        return value

def convert_length(value, from_unit, to_unit):
    length_units = {"m": 1, "cm": 100, "mm": 1000, "km": 0.001, "mi": 0.000621371, "yd": 1.09361, "ft": 3.28084, "in": 39.3701}
    converted_value = value * length_units[from_unit] / length_units[to_unit]
    return converted_value

def convert_weight(value, from_unit, to_unit):
    weight_units = {"kg": 1, "g": 1000, "mg": 1_000_000, "lb": 2.20462, "oz": 35.274}
    converted_value = value * weight_units[from_unit] / weight_units[to_unit]
    return converted_value

# Create the main window
root = tk.Tk()
root.title("Unit Converter")

# Create and place widgets
label_conversion_type = ttk.Label(root, text="Select Conversion Type:")
label_conversion_type.grid(row=0, column=0, padx=10, pady=10, sticky="W")

conversion_type = tk.StringVar()
combo_conversion_type = ttk.Combobox(root, values=["Temperature", "Length", "Weight"], textvariable=conversion_type)
combo_conversion_type.grid(row=0, column=1, padx=10, pady=10)
combo_conversion_type.set("Temperature")

label_value = ttk.Label(root, text="Enter the value:")
label_value.grid(row=1, column=0, padx=10, pady=10, sticky="W")

entry_value = ttk.Entry(root)
entry_value.grid(row=1, column=1, padx=10, pady=10)

label_from = ttk.Label(root, text="From unit:")
label_from.grid(row=2, column=0, padx=10, pady=10, sticky="W")

combo_from = ttk.Combobox(root, values=["C", "F", "M", "CM", "MM", "KM", "MI", "YD", "FT", "IN", "KG", "G", "MG", "LB", "OZ"])
combo_from.grid(row=2, column=1, padx=10, pady=10)
combo_from.set("C")

label_to = ttk.Label(root, text="To unit:")
label_to.grid(row=3, column=0, padx=10, pady=10, sticky="W")

combo_to = ttk.Combobox(root, values=["C", "F", "M", "CM", "MM", "KM", "MI", "YD", "FT", "IN", "KG", "G", "MG", "LB", "OZ"])
combo_to.grid(row=3, column=1, padx=10, pady=10)
combo_to.set("C")

button_convert = ttk.Button(root, text="Convert", command=convert_units)
button_convert.grid(row=4, column=0, columnspan=2, pady=10)

label_result = ttk.Label(root, text="")
label_result.grid(row=5, column=0, columnspan=2, pady=10)

# Start the main loop
root.mainloop()



