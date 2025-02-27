import pytest
from final_project.project_v3_final import calculate_investment_growth, calculate_volatility, scenario_comparison

# Test for investment growth calculation
def test_calculate_investment_growth():
    initial_investment = 1000
    monthly_contribution = 100
    annual_interest_rate = 5
    years = 10
    compounding_frequency = 'Monthly'
    investment_goal = 5000
    
    total_value, investment_values = calculate_investment_growth(
        initial_investment, monthly_contribution, annual_interest_rate, years, compounding_frequency, investment_goal
    )
    assert total_value > 5000, "Investment growth calculation failed to meet expected value."
    assert len(investment_values) == years * 12, "Incorrect number of investment periods calculated."

# Test for volatility calculation
def test_calculate_volatility():
    investment_values = [1000, 1050, 1100, 1150, 1200]
    compoundings_per_year = 12
    volatility = calculate_volatility(investment_values, compoundings_per_year)
    assert volatility is not None, "Volatility calculation returned None."
    assert volatility > 0, "Volatility should be greater than zero for increasing values."

# Test for scenario comparison
def test_scenario_comparison():
    initial_investment = 1000
    monthly_contribution = 100
    annual_interest_rate = 5
    years = 10
    compoundings_per_year = 12
    scenarios = scenario_comparison(
        initial_investment, monthly_contribution, annual_interest_rate, years, compoundings_per_year
    )
    assert len(scenarios) == 3, "Scenario comparison did not generate all expected scenarios."
    for rate, values in scenarios.items():
        assert len(values) == years * compoundings_per_year, f"Scenario {rate} has incorrect value length."


