import streamlit as st

# Define conversion factors
conversion_factors = {
    'Length': {
        'meter': 1,
        'kilometer': 1000,
        'centimeter': 0.01,
        'millimeter': 0.001,
        'mile': 1609.34,
        'yard': 0.9144,
        'foot': 0.3048,
        'inch': 0.0254
    },
    'Weight': {
        'kilogram': 1,
        'gram': 0.001,
        'milligram': 0.000001,
        'pound': 0.453592,
        'ounce': 0.0283495,
        'tonne': 1000
    },
    'Temperature': {
        'celsius': 1,
        'fahrenheit': 1,  # Special case
        'kelvin': 1       # Special case
    },
    'Volume': {
        'liter': 1,
        'milliliter': 0.001,
        'gallon': 3.78541,
        'quart': 0.946353,
        'pint': 0.473176,
        'cup': 0.24,
        'tablespoon': 0.0147868,
        'teaspoon': 0.00492892,
        'cubic meter': 1000,
        'cubic foot': 28.3168,
        'cubic inch': 0.0163871
    },
    'Area': {
        'square meter': 1,
        'square kilometer': 1000000,
        'square mile': 2589988.11,
        'square yard': 0.836127,
        'square foot': 0.092903,
        'square inch': 0.00064516,
        'hectare': 10000,
        'acre': 4046.86
    }
}

def convert_temperature(value, from_unit, to_unit):
    if from_unit == 'celsius':
        if to_unit == 'fahrenheit':
            return value * 9/5 + 32
        elif to_unit == 'kelvin':
            return value + 273.15
        else:
            return value
    elif from_unit == 'fahrenheit':
        if to_unit == 'celsius':
            return (value - 32) * 5/9
        elif to_unit == 'kelvin':
            return (value - 32) * 5/9 + 273.15
        else:
            return value
    elif from_unit == 'kelvin':
        if to_unit == 'celsius':
            return value - 273.15
        elif to_unit == 'fahrenheit':
            return (value - 273.15) * 9/5 + 32
        else:
            return value
    return value

def main():
    st.title("📐 Unit Converter")
    st.write("Convert between different units easily!")
    
    # Category selection
    category = st.selectbox("Select category", list(conversion_factors.keys()))
    
    # Unit selection
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From", list(conversion_factors[category].keys()))
    with col2:
        to_unit = st.selectbox("To", list(conversion_factors[category].keys()))
    
    # Value input
    value = st.number_input("Enter value to convert", min_value=0.0, value=1.0, step=0.1)
    
    # Conversion and output
    if st.button("Convert"):
        if category == 'Temperature':
            result = convert_temperature(value, from_unit, to_unit)
        else:
            result = value * conversion_factors[category][from_unit] / conversion_factors[category][to_unit]
        
        st.success(f"**{value} {from_unit} = {result:.4f} {to_unit}**")
    
    st.markdown("---")
    st.markdown("### Common Conversions")
    
    # Quick conversion buttons
    if category == 'Length':
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("Meters to Feet"):
                st.write(f"{value} meters = {value * 3.28084:.2f} feet")
        with col2:
            if st.button("Kilometers to Miles"):
                st.write(f"{value} kilometers = {value * 0.621371:.2f} miles")
        with col3:
            if st.button("Centimeters to Inches"):
                st.write(f"{value} centimeters = {value * 0.393701:.2f} inches")
    
    elif category == 'Weight':
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("Kilograms to Pounds"):
                st.write(f"{value} kg = {value * 2.20462:.2f} lbs")
        with col2:
            if st.button("Grams to Ounces"):
                st.write(f"{value} grams = {value * 0.035274:.2f} oz")
        with col3:
            if st.button("Pounds to Kilograms"):
                st.write(f"{value} lbs = {value * 0.453592:.2f} kg")
    
    st.markdown("---")
    st.write("Made with ❤️ using Streamlit")

if __name__ == "__main__":
    main()