principal = 1000  # Original amount invested
annual_rate = 0.07  # Annual rate of return (7%)


for years in [10, 20, 30]:
    amount = principal * (1 + annual_rate) ** years
    print(f"After {years} years, the amount on deposit will be: ${amount:.2f}")
