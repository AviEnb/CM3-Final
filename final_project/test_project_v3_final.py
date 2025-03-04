import pytest
from project_v3_final import (
    calculate_investment_growth, 
    calculate_volatility, 
    scenario_comparison
)


# Test for volatility calculation
def test_calculate_volatility():
    investment_values = [1000, 1050, 1100, 1150, 1200]
    compoundings_per_year = 12

    volatility = calculate_volatility(investment_values, compoundings_per_year)
    
    assert volatility is not None, "Volatility calculation returned None."
    assert volatility > 0, "Volatility should be greater than zero for increasing values."
    assert isinstance(volatility, float), "Volatility should be a float."

# Test for scenario comparison
def test_scenario_comparison():
    initial_investment = 1000
    monthly_contribution = 100
    annual_interest_rate = 5
    years = 10
    compoundings_per_year = 12  # Ensure integer type
    
    scenarios = scenario_comparison(
        initial_investment, monthly_contribution, annual_interest_rate, years, compoundings_per_year
    )
    
    assert isinstance(scenarios, dict), "Scenario comparison should return a dictionary."
    assert len(scenarios) == 3, "Scenario comparison did not generate all expected scenarios."
    
    for rate, values in scenarios.items():
        assert isinstance(values, list), f"Scenario {rate} should return a list."
        assert len(values) == years * 12, f"Scenario {rate} has incorrect value length."