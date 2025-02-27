import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import io

# Main function to run the Streamlit app
def main():
    st.set_page_config(page_title='Investment Return Calculator', layout='centered', initial_sidebar_state='expanded')
    st.markdown("# 💰 Investment Return Calculator")
    st.markdown("Calculate your investment growth over time with different compounding options.")
    setup_sidebar()
    print('App initialized')

# Function to set up the sidebar and handle user inputs
def setup_sidebar():
    st.sidebar.header('⚙️ Investment Parameters')
    st.sidebar.markdown("---")
    initial_investment = st.sidebar.number_input('💵 Initial Investment Amount ($)', min_value=0.0, step=100.0, value=1000.0)
    print(f'Initial Investment: {initial_investment}')
    monthly_contribution = st.sidebar.number_input('📥 Monthly Contribution ($)', min_value=0.0, step=50.0, value=100.0)
    print(f'Monthly Contribution: {monthly_contribution}')
    annual_interest_rate = st.sidebar.number_input('📈 Expected Annual Return Rate (%)', min_value=0.0, max_value=100.0, step=0.1, value=5.0)
    print(f'Annual Interest Rate: {annual_interest_rate}')
    years = st.sidebar.number_input('⏳ Investment Duration (Years)', min_value=1, step=1, value=10)
    print(f'Investment Duration: {years} years')
    compounding_frequency = st.sidebar.selectbox('🔁 Compounding Frequency', ['Annually', 'Semi-Annually', 'Quarterly', 'Monthly', 'Daily'])
    print(f'Compounding Frequency: {compounding_frequency}')
    investment_goal = st.sidebar.number_input('🏁 Investment Goal ($)', min_value=0.0, step=500.0, value=50000.0)
    print(f'Investment Goal: {investment_goal}')

    if st.sidebar.button('🚀 Calculate Investment Growth'):
        print('Calculate button clicked')
        calculate_investment_growth(initial_investment, monthly_contribution, annual_interest_rate, years, compounding_frequency, investment_goal)

# Function to calculate investment growth and display results
def calculate_investment_growth(initial_investment, monthly_contribution, annual_interest_rate, years, compounding_frequency, investment_goal):
    frequency_map = {'Annually': 1, 'Semi-Annually': 2, 'Quarterly': 4, 'Monthly': 12, 'Daily': 365}
    compoundings_per_year = frequency_map.get(compounding_frequency, 1)
    total_periods = years * compoundings_per_year
    periodic_rate = (annual_interest_rate / 100) / compoundings_per_year
    print(f'Periodic Rate: {periodic_rate}, Total Periods: {total_periods}')
    investment_values = []
    total_value = initial_investment

    for period in range(1, total_periods + 1):
        total_value = total_value * (1 + periodic_rate) + monthly_contribution * (1 + periodic_rate)
        investment_values.append(total_value)
    print(f'Final Investment Value: {total_value}')

    st.subheader(f'💰 Estimated Value After {years} Years: **${total_value:,.2f}**')
    if total_value >= investment_goal:
        st.success(f'🎉 Congratulations! You will achieve your investment goal of **${investment_goal:,.2f}**.')
    else:
        st.warning(f'⚠️ You will not reach your investment goal of **${investment_goal:,.2f}**. Consider increasing contributions or duration.')

    # Visualization of investment growth
    st.markdown("---")
    st.header('📈 Investment Growth Over Time')
    plt.figure(figsize=(10, 6))
    plt.plot(investment_values, label='Investment Growth', color='teal')
    plt.axhline(y=investment_goal, color='r', linestyle='--', label='Investment Goal')
    plt.xlabel('Time (Periods)')
    plt.ylabel('Portfolio Value ($)')
    plt.title('Investment Growth Over Time')
    plt.legend()
    plt.grid(True)
    st.pyplot(plt.gcf())

    # Volatility Analysis
    st.markdown("---")
    st.header('📉 Risk & Volatility Analysis')
    volatility = calculate_volatility(investment_values, compoundings_per_year)
    if volatility is not None:
        st.write(f'Estimated Volatility (Standard Deviation): **{volatility:.2%}**')
    else:
        st.warning('⚠️ Not enough data for volatility analysis.')

    # Scenario Comparison Tool
    st.markdown("---")
    st.header('🆚 Scenario Comparison Tool')
    scenario_values = scenario_comparison(initial_investment, monthly_contribution, annual_interest_rate, years, compoundings_per_year)
    plt.figure(figsize=(10, 6))
    for rate, values in scenario_values.items():
        plt.plot(values, label=f'{rate}', linestyle='--')
    plt.xlabel('Time (Periods)')
    plt.ylabel('Portfolio Value ($)')
    plt.title('Scenario Comparison with ±3% Deviation')
    plt.legend()
    plt.grid(True)
    st.pyplot(plt.gcf())

# Function to calculate the volatility of investment returns
def calculate_volatility(investment_values, compoundings_per_year):
    returns = pd.Series(investment_values).pct_change().dropna()
    if not returns.empty:
        volatility = returns.std() * np.sqrt(compoundings_per_year)
        print(f'Volatility: {volatility}')
        return volatility
    print('No volatility data available')
    return None

# Function to compare different investment scenarios
def scenario_comparison(initial_investment, monthly_contribution, annual_interest_rate, years, compoundings_per_year):
    lower_bound = max(0, annual_interest_rate - 3)
    upper_bound = annual_interest_rate + 3
    comparison_rates = [lower_bound, annual_interest_rate, upper_bound]
    scenario_values = {}
    print(f'Scenario Comparison Rates: {comparison_rates}')

    for rate in comparison_rates:
        periodic_rate = (rate / 100) / compoundings_per_year
        scenario_total_value = initial_investment
        values = []
        for _ in range(years * compoundings_per_year):
            scenario_total_value = scenario_total_value * (1 + periodic_rate) + monthly_contribution * (1 + periodic_rate)
            values.append(scenario_total_value)
        scenario_values[f'{rate}% Return'] = values
        print(f'Calculated Scenario for {rate}%: Final Value: {scenario_total_value}')

    return scenario_values

if __name__ == '__main__':
    main()

