
original_wages = 10
percentage = 0.03
for year in range(1,11):
    new_wages = original_wages * (1 + percentage) ** year
    print(f"the new wages for good performance in year {year:>2} {new_wages:>10.2f}")

