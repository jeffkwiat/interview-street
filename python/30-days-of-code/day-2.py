mealCost = float(input())
tipPercent = int(input())
taxRate = int(input())
tip = mealCost * (tipPercent / 100)
tax = mealCost * (taxRate / 100)
print('The total meal cost is %s dollars.' % (round(mealCost + tip + tax)))