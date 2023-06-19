
principal = 1000
rate = 0.05
for year in range (1,11):
    amount = principal * (1 + rate) ** year
    print(f"{year:>4}{amount:>15.2f}")