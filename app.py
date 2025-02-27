import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

# Set up the Streamlit app
st.set_page_config(page_title='Investment Return Calculator', layout='centered')
st.title('💰 Investment Return Calculator')
st.markdown("Calculate your investment growth over time with different compounding options.")

# Add a sidebar for input parameters
st.sidebar.header('Investment Parameters')

# Input fields for the investment details
initial_investment = st.sidebar.number_input('Initial Investment Amount ($)', min_value=0.0, step=100.0, value=1000.0)
monthly_contribution = st.sidebar.number_input('Monthly Contribution ($)', min_value=0.0, step=50.0, value=100.0)
annual_interest_rate = st.sidebar.number_input('Expected Annual Return Rate (%)', min_value=0.0, max_value=100.0, step=0.1, value=5.0)
years = st.sidebar.number_input('Investment Duration (Years)', min_value=1, step=1, value=10)
compounding_frequency = st.sidebar.selectbox('Compounding Frequency', ['Annually', 'Semi-Annually', 'Quarterly', 'Monthly', 'Daily'])

# Mapping compounding frequency to numerical values
frequency_map = {
    'Annually': 1,
    'Semi-Annually': 2,
    'Quarterly': 4,
    'Monthly': 12,
    'Daily': 365
}
compoundings_per_year = frequency_map[compounding_frequency]

# Calculate the investment growth
if st.sidebar.button('Calculate Investment Growth'):
    total_periods = years * compoundings_per_year
    periodic_rate = (annual_interest_rate / 100) / compoundings_per_year
    investment_values = []
    total_value = initial_investment
    for period in range(1, total_periods + 1):
        total_value = total_value * (1 + periodic_rate) + monthly_contribution * (1 + periodic_rate)
        investment_values.append(total_value)
    
    # Display the results
    st.subheader(f'Estimated Value After {years} Years: ${total_value:,.2f}')
    
    # Visualization
    plt.figure(figsize=(10, 6))
    plt.plot(investment_values, label='Investment Growth', color='teal')
    plt.xlabel('Time (Periods)')
    plt.ylabel('Portfolio Value ($)')
    plt.title('📈 Investment Growth Over Time')
    plt.legend()
    plt.grid(True)
    st.pyplot(plt.gcf())

    # Show a breakdown of values
    df = pd.DataFrame({'Period': range(1, total_periods + 1), 'Portfolio Value ($)': investment_values})
    st.dataframe(df)

# Footer
st.write("\n\nMade with ❤️ using Streamlit")
