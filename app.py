import streamlit as st

st.set_page_config(page_title="Sydney Housing Price Predictor", layout="centered")

st.title("Sydney Housing Price Predictor")
st.write("Enter property details to get a predicted sale price.")
st.write("Default suburb is Blacktown and default property type is House.")

# Input fields
bedrooms = st.number_input("Bedrooms", min_value=1, max_value=6, value=3)
bathrooms = st.number_input("Bathrooms", min_value=1, max_value=5, value=2)
car_spaces = st.number_input("Car spaces", min_value=0, max_value=5, value=2)
land_size = st.number_input("Land size (sqm)", min_value=100, max_value=1000, value=400)
sale_year = st.number_input("Sale year", min_value=2020, max_value=2026, value=2025)

suburb = st.selectbox("Suburb", ["Blacktown", "Parramatta", "Bondi"])
prop_type = st.selectbox("Property Type", ["House", "Townhouse", "Unit"])

# Prediction button
if st.button("Predict Price"):
    # Simple price logic
    if suburb == "Bondi":
        base = 3500000
    elif suburb == "Parramatta":
        base = 1600000
    else:
        base = 1100000  # Blacktown

    price = base
    price += (bedrooms - 3) * 150000
    price += (bathrooms - 2) * 90000
    price += (car_spaces - 1) * 50000
    price += (land_size - 400) * 900

    if prop_type == "Townhouse":
        price = price * 0.88
    elif prop_type == "Unit":
        price = price * 0.68

    if price < 500000:
        price = 500000

    st.success(f"Predicted sale price: ${price:,.0f}")
