import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from fpdf import FPDF

# Set up the Streamlit app
st.set_page_config(page_title='Investment Return Calculator', layout='centered', initial_sidebar_state='expanded')
st.markdown("# 💰 Investment Return Calculator")
st.markdown("Calculate your investment growth over time with different compounding options.")

# Add a sidebar for input parameters with styling
st.sidebar.header('⚙️ Investment Parameters')
st.sidebar.markdown("---")

# Input fields for the investment details with validation
try:
    initial_investment = st.sidebar.number_input('💵 Initial Investment Amount ($)', min_value=0.0, step=100.0, value=1000.0)
    monthly_contribution = st.sidebar.number_input('📥 Monthly Contribution ($)', min_value=0.0, step=50.0, value=100.0)
    annual_interest_rate = st.sidebar.number_input('📈 Expected Annual Return Rate (%)', min_value=0.0, max_value=100.0, step=0.1, value=5.0)
    years = st.sidebar.number_input('⏳ Investment Duration (Years)', min_value=1, step=1, value=10)
    compounding_frequency = st.sidebar.selectbox('🔁 Compounding Frequency', ['Annually', 'Semi-Annually', 'Quarterly', 'Monthly', 'Daily'])

    # Investment Goal Planner
    st.sidebar.header('🎯 Investment Goal Planner')
    st.sidebar.markdown("---")
    investment_goal = st.sidebar.number_input('🏁 Investment Goal ($)', min_value=0.0, step=500.0, value=50000.0)

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
    if st.sidebar.button('🚀 Calculate Investment Growth'):
        st.markdown("---")
        st.header('📊 Investment Growth Analysis')
        total_periods = years * compoundings_per_year
        periodic_rate = (annual_interest_rate / 100) / compoundings_per_year
        investment_values = []
        total_value = initial_investment
        for period in range(1, total_periods + 1):
            total_value = total_value * (1 + periodic_rate) + monthly_contribution * (1 + periodic_rate)
            investment_values.append(total_value)
        
        # Display the results
        st.subheader(f'💰 Estimated Value After {years} Years: **${total_value:,.2f}**')
        
        # Goal achievement
        if total_value >= investment_goal:
            st.success(f'🎉 Congratulations! You will achieve your investment goal of **${investment_goal:,.2f}**.')
        else:
            st.warning(f'⚠️ You will not reach your investment goal of **${investment_goal:,.2f}**. Consider increasing contributions or duration.')

        # Visualization
        st.markdown("---")
        st.header('📈 Investment Growth Over Time')
        plt.figure(figsize=(10, 6))
        plt.plot(investment_values, label='Investment Growth', color='teal')
        plt.xlabel('Time (Periods)')
        plt.ylabel('Portfolio Value ($)')
        plt.title('Investment Growth Over Time')
        plt.legend()
        plt.grid(True)
        st.pyplot(plt.gcf())

        # Show a breakdown of values
        df = pd.DataFrame({'Period': range(1, total_periods + 1), 'Portfolio Value ($)': investment_values})
        st.dataframe(df)

        # Risk & Volatility Analysis
        st.markdown("---")
        st.header('📉 Risk & Volatility Analysis')
        returns = pd.Series(investment_values).pct_change().dropna()
        volatility = returns.std() * np.sqrt(compoundings_per_year)
        st.write(f'Estimated Volatility (Standard Deviation): **{volatility:.2%}**')

        # Scenario Comparison Tool
        st.markdown("---")
        st.header('🆚 Scenario Comparison Tool')
        alt_return_rate = st.slider('Alternative Annual Return Rate (%)', 0.0, 20.0, 7.0)

        if alt_return_rate >= 0 and compoundings_per_year > 0:
            alt_periodic_rate = (alt_return_rate / 100) / compoundings_per_year
            alt_investment_values = []
            alt_total_value = initial_investment
            for period in range(1, total_periods + 1):
                alt_total_value = alt_total_value * (1 + alt_periodic_rate) + monthly_contribution * (1 + alt_periodic_rate)
                alt_investment_values.append(alt_total_value)

            plt.figure(figsize=(10, 6))
            plt.plot(investment_values, label='Original Scenario', color='teal')
            plt.plot(alt_investment_values, label='Alternative Scenario', color='orange')
            plt.xlabel('Time (Periods)')
            plt.ylabel('Portfolio Value ($)')
            plt.title('Scenario Comparison')
            plt.legend()
            plt.grid(True)
            st.pyplot(plt.gcf())
        else:
            st.warning('⚠️ Please ensure a valid alternative return rate and compounding frequency.')

except Exception as e:
    st.error(f'⚠️ An unexpected error occurred: {str(e)}')

# Footer
st.markdown("---")
st.write("📄 Made with ❤️ using Streamlit")