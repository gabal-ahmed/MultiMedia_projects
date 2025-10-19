item1 = 45.50
item2 = 30.75
item3 = 25.20

budget = 100.00

total_cost = item1 + item2 + item3

# 4. Compare the total cost with the budget
print("Total cost of items:", total_cost)
print("Budget:", budget)

if total_cost > budget:
    difference = total_cost - budget
    print("You need", difference, "more to reach your budget.")
elif total_cost < budget:
    difference = budget - total_cost
    print("You have", difference, "left after purchase.")
else:
    print("You spent exactly your budget!")
