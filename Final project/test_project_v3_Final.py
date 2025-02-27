import pytest
from project_v3_Final import calculate_investment_growth, calculate_volatility, scenario_comparison

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

# Test for edge case with zero initial investment
def test_zero_initial_investment():
    total_value, _ = calculate_investment_growth(0, 100, 5, 10, 'Monthly', 5000)
    assert total_value > 0, "Investment should grow even with zero initial investment if contributions are made."

# Test for negative interest rates
def test_negative_interest_rate():
    total_value, _ = calculate_investment_growth(1000, 100, -5, 10, 'Monthly', 5000)
    assert total_value < 1000, "Investment value should decrease with negative interest rates."

# Test for extremely high interest rates
def test_extremely_high_interest_rate():
    total_value, _ = calculate_investment_growth(1000, 100, 100, 10, 'Monthly', 5000)
    assert total_value > 50000, "Investment value should be significantly high with 100% annual return rate."

# Test for zero monthly contributions
def test_zero_monthly_contribution():
    total_value, _ = calculate_investment_growth(1000, 0, 5, 10, 'Monthly', 5000)
    assert total_value > 1000, "Investment should grow even without additional monthly contributions."

# Test for daily compounding frequency
def test_daily_compounding():
    total_value, investment_values = calculate_investment_growth(1000, 100, 5, 10, 'Daily', 5000)
    assert len(investment_values) == 10 * 365, "Daily compounding should calculate the correct number of periods."

# Test for short investment duration
def test_short_investment_duration():
    total_value, _ = calculate_investment_growth(1000, 100, 5, 1, 'Monthly', 5000)
    assert total_value < 5000, "One year of investment should not meet a long-term goal of $5000 with the given contributions."

