# Write your code here
import math
from ipywidgets import interactive
import matplotlib.pyplot as plt
import numpy as np
from IPython.display import display

def calculate_annuity(principal, rate, time, compounding_type, monthly_contribution=0):
    """Calculates the future value of an annuity."""
    if rate < 0 or time < 0 or principal < 0 or monthly_contribution < 0:
        return "Error: Inputs cannot be negative."

    if compounding_type.lower() == 'monthly':
        r_monthly = rate / (12 * 100)  # Annual rate to monthly decimal
        n_months = time * 12
        if r_monthly == 0:
            future_value = principal + (monthly_contribution * n_months)
        else:
            future_value = principal * (1 + r_monthly)**n_months
            if monthly_contribution > 0:
                future_value += monthly_contribution * (((1 + r_monthly)**n_months - 1) / r_monthly)
        return f"Annuity with monthly growth: ${future_value:.2f}"
    elif compounding_type.lower() == 'continuous':
        r_annual = rate / 100
        future_value = principal * math.e**(r_annual * time)
        return f"Annuity with continuous growth: ${future_value:.2f}"
    else:
        return "Error: Invalid compounding type. Choose 'monthly' or 'continuous'."

def calculate_mortgage_payment(principal, rate, time):
    """Calculates the monthly mortgage payment."""
    if principal < 0 or rate < 0 or time < 0:
        return "Error: Inputs cannot be negative."

    r_monthly = rate / (12 * 100)
    n_months = time * 12
    if r_monthly == 0:
        if n_months == 0:
            return f"Monthly payment: ${principal:.2f} (one-time payment)"
        else:
            return f"Monthly payment: ${principal / n_months:.2f} (no interest)"
    else:
        numerator = principal * r_monthly * (1 + r_monthly)**n_months
        denominator = ((1 + r_monthly)**n_months) - 1
        if denominator == 0:
            return "Error: Cannot calculate payment (likely zero interest and zero term)."
        monthly_payment = numerator / denominator
        return f"Monthly mortgage payment: ${monthly_payment:.2f}"

def estimate_retirement_balance(current_age, retirement_age, current_savings, annual_contribution, annual_growth_rate):
    """Estimates retirement investment balance."""
    if current_age < 0 or retirement_age <= current_age or current_savings < 0 or annual_contribution < 0 or annual_growth_rate < 0:
        return "Error: Invalid input values."

    years_to_retirement = retirement_age - current_age
    monthly_growth_rate = annual_growth_rate / (12 * 100)
    months_to_retirement = years_to_retirement * 12
    monthly_contribution = annual_contribution / 12

    future_value = current_savings
    for _ in range(months_to_retirement):
        future_value = (future_value + monthly_contribution) * (1 + monthly_growth_rate)

    return f"Estimated retirement balance: ${future_value:.2f}"

def time_to_double(initial_amount, rate, compounding_type='continuous'):
    """Determines how long until an amount doubles."""
    if initial_amount <= 0 or rate <= 0:
        return "Error: Initial amount and rate must be positive."

    if compounding_type.lower() == 'continuous':
        time_required = math.log(2) / (rate / 100)
        return f"Time to double (continuous): {time_required:.2f} years"
    elif compounding_type.lower() == 'annually':
        if rate / 100 >= 1:
            return "Warning: At this rate, doubling occurs in the first year."
        time_required = math.log(2) / math.log(1 + (rate / 100))
        return f"Time to double (annually): {time_required:.2f} years"
    else:
        return "Error: Invalid compounding type. Choose 'continuous' or 'annually'."

def solve_logarithmic_equation(base, result):
    """Solves for x in log_base(result) = x."""
    if base <= 0 or base == 1 or result <= 0:
        return "Error: Base must be > 0 and not equal to 1, result must be > 0."
    exponent = math.log(result, base)
    return f"Solution (exponent): {exponent:.2f}"

def to_scientific_notation(number):
    """Converts a number to scientific notation."""
    if number == 0:
        return "0.0 * 10^0"
    exponent = math.floor(math.log10(abs(number)))
    coefficient = round(number * 10**(-exponent), 2)
    return f"{coefficient} * 10^{exponent}"

def from_scientific_notation(coefficient_str, exponent_str):
    """Converts from scientific notation to a regular number."""
    try:
        coefficient = float(coefficient_str)
        exponent = int(exponent_str)
        return coefficient * (10**exponent)
    except ValueError:
        return "Error: Invalid coefficient or exponent format."

def financial_app():
    """Interactive financial application."""
    print("Welcome to the Interactive Financial App!")

    while True:
        print("\nChoose an operation:")
        print("1. Calculate Annuity")
        print("2. Calculate Monthly Mortgage Payment")
        print("3. Estimate Retirement Balance")
        print("4. Time Until Amount Doubles")
        print("5. Solve Logarithmic Equation")
        print("6. Convert to Scientific Notation")
        print("7. Convert from Scientific Notation")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            principal = float(input("Enter principal amount: "))
            rate = float(input("Enter annual interest rate (%): "))
            time = float(input("Enter investment time (years): "))
            compounding = input("Enter compounding type (monthly/continuous): ")
            monthly_contribution = float(input("Enter monthly contribution (if any): "))
            result = calculate_annuity(principal, rate, time, compounding, monthly_contribution)
            print(result)

        elif choice == '2':
            principal = float(input("Enter loan amount (principal): "))
            rate = float(input("Enter annual interest rate (%): "))
            time = float(input("Enter loan term (years): "))
            result = calculate_mortgage_payment(principal, rate, time)
            print(result)

        elif choice == '3':
            current_age = int(input("Enter your current age: "))
            retirement_age = int(input("Enter your desired retirement age: "))
            current_savings = float(input("Enter your current retirement savings: "))
            annual_contribution = float(input("Enter your annual contribution: "))
            annual_growth_rate = float(input("Enter estimated annual growth rate (%): "))
            result = estimate_retirement_balance(current_age, retirement_age, current_savings, annual_contribution, annual_growth_rate)
            print(result)

        elif choice == '4':
            initial_amount = float(input("Enter initial amount: "))
            rate = float(input("Enter annual interest rate (%): "))
            compounding = input("Enter compounding type (continuous/annually): ")
            result = time_to_double(initial_amount, rate, compounding)
            print(result)

        elif choice == '5':
            base = float(input("Enter the base of the logarithm: "))
            result_log = float(input("Enter the result of the logarithmic equation: "))
            result = solve_logarithmic_equation(base, result_log)
            print(result)

        elif choice == '6':
            number_to_convert = float(input("Enter a number to convert to scientific notation: "))
            result = to_scientific_notation(number_to_convert)
            print(result)

        elif choice == '7':
            coefficient_str = input("Enter the coefficient (e.g., 1.23): ")
            exponent_str = input("Enter the exponent (e.g., 4): ")
            result = from_scientific_notation(coefficient_str, exponent_str)
            print("Regular number:", result)

        elif choice == '8':
            print("Thank you for using the Financial App!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

if __name__ == "__main__":
    financial_app()

# This step does not have a test
