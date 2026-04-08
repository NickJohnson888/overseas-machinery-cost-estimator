import streamlit as st
from calculator import MachineryCostCalculator

st.set_page_config(page_title="Overseas EPC Machinery Cost Estimator", layout="wide")
st.title('🌍 Overseas EPC Machinery Cost Estimator')

st.sidebar.header('⚙️ User Inputs')
equipment_value = st.sidebar.number_input('Equipment Value (USD)', value=150000.0, step=1000.0)
freight_customs = st.sidebar.number_input('Freight & Customs (USD)', value=15000.0, step=1000.0)
depreciation_years = st.sidebar.number_input('Depreciation Years', value=10, min_value=1)
fuel_consumption = st.sidebar.number_input('Fuel Consumption per Shift', value=100.0, step=10.0)
fuel_unit_price = st.sidebar.number_input('Fuel Unit Price (USD)', value=1.2, step=0.1)

# Instantiate the calculator
calculator = MachineryCostCalculator(
    equipment_value=equipment_value,
    freight_and_customs=freight_customs,
    depreciation_years=depreciation_years,
    fuel_consumption_per_shift=fuel_consumption,
    fuel_unit_price=fuel_unit_price
)

st.header("📊 Calculation Results")
col1, col2 = st.columns(2)

with col1:
    st.metric('First-Category Costs (Shift)', f"${calculator.calc_first_category_costs():,.2f}")
    st.metric('Second-Category Costs (Shift)', f"${calculator.calc_second_category_costs():,.2f}")

with col2:
    st.metric('Total Shift Cost', f"${calculator.calc_total_shift_cost():,.2f}")
    st.metric('🔥 Final Hourly Rate', f"${calculator.calc_hourly_rate():,.2f}")