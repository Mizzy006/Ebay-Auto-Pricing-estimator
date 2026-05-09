import streamlit as st
import pandas as pd
import joblib
import plotly.express as px

# 1. Page Configuration
st.set_page_config(page_title="Auto Pricing Estimator", page_icon="🚗", layout="wide")

@st.cache_resource
def load_model():
    return joblib.load('car_price_model.pkl')

model = load_model()

# --- UI LAYOUT ---
st.sidebar.title("🚗 Vehicle Specs")
st.sidebar.markdown("Adjust parameters to update the real-time valuation.")

# We capitalize these for the UI, but will convert them to lowercase for the model
ui_brand = st.sidebar.selectbox("Brand", ['Volkswagen', 'BMW', 'Mercedes_Benz', 'Audi', 'Opel', 'Ford', 'Renault', 'Toyota', 'Porsche', 'Sonstige_autos'])
ui_type = st.sidebar.selectbox("Vehicle Type", ['Limousine', 'Kombi', 'Kleinwagen', 'SUV', 'Cabrio', 'Coupe', 'Bus']) # Assuming you kept German types or update if you translated these too!
ui_gearbox = st.sidebar.selectbox("Transmission", ['Automatic', 'Manual'])
ui_fuel = st.sidebar.selectbox("Fuel Type", ['Petrol', 'Diesel', 'Hybrid', 'Electric'])
ui_damage = st.sidebar.radio("Unrepaired Damage?", ['No', 'Yes'])

vehicle_age = st.sidebar.slider("Vehicle Age (Years)", 0, 20, 5)
odometer_km = st.sidebar.slider("Mileage (km)", 0, 300000, 75000, step=5000)
power_ps = st.sidebar.number_input("Horsepower (PS)", 0, 600, 150, step=10)

# --- BACKEND PREPARATION ---
# The model expects lowercase English strings based on your training data
model_brand = ui_brand.lower()
model_type = ui_type.lower()
model_gearbox = ui_gearbox.lower()
model_fuel = ui_fuel.lower()
model_damage = ui_damage.lower()

# --- MAIN DASHBOARD ---
st.title(f"Market Valuation: {ui_brand} {ui_type}")

# Package input exactly how your updated model expects it
current_input = pd.DataFrame({
    'brand': [model_brand], 
    'vehicle_age': [vehicle_age], 
    'odometer_km': [odometer_km],
    'power_ps': [power_ps], 
    'vehicle_type': [model_type], 
    'gearbox': [model_gearbox],
    'fuel_type': [model_fuel], 
    'unrepaired_damage': [model_damage]
})

current_price = model.predict(current_input)[0]

st.metric(label="Estimated Market Value", 
          value=f"${current_price:,.2f}", 
          delta="± $1,321 Margin of Error", 
          delta_color="off")
st.markdown("---")

# --- DYNAMIC DEPRECIATION CURVE ---
st.subheader("Projected Depreciation Lifecycle")
st.write("This chart simulates the estimated value of *this exact vehicle configuration* across different ages. It assumes an average usage of 15,000 km per year.")

ages = list(range(0, 21))
simulated_data = []

for age in ages:
    if age >= vehicle_age:
        sim_km = min(odometer_km + ((age - vehicle_age) * 15000), 300000)
    else:
        sim_km = max(odometer_km - ((vehicle_age - age) * 15000), 0)
        
    simulated_data.append({
        'brand': model_brand, 'vehicle_age': age, 'odometer_km': sim_km,
        'power_ps': power_ps, 'vehicle_type': model_type, 'gearbox': model_gearbox,
        'fuel_type': model_fuel, 'unrepaired_damage': model_damage
    })

sim_df = pd.DataFrame(simulated_data)
sim_df['Predicted Price'] = model.predict(sim_df)

fig = px.line(sim_df, x='vehicle_age', y='Predicted Price', 
              labels={'vehicle_age': 'Vehicle Age (Years)', 'Predicted Price': 'Estimated Value ($)'})
fig.add_scatter(x=[vehicle_age], y=[current_price], mode='markers', 
                marker=dict(size=14, color='red'), name='Current Configuration')

st.plotly_chart(fig, use_container_width=True)