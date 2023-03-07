weight = 9999
# Ground shipping
flat_charge = 20.00
cost = 0
if weight <= 2:
  cost = flat_charge + weight * 1.50
elif weight <=6:
  cost = flat_charge + weight * 3.00
elif weight <=6:
  cost = flat_charge + weight * 4.00
else:
  cost = flat_charge + weight * 4.75
print("Total cost for Ground shipping: $",cost)
# Ground shipping Premium
precost = 125.00
print("Total cost for Ground shipping Premium: $",precost)
# Drone Shipping
dr_cost = 0
flat_charge = 0
if weight <= 2:
  dr_cost = flat_charge + weight * 4.50
elif weight <=6:
  dr_cost = flat_charge + weight * 9.00
elif weight <=6:
  dr_cost = flat_charge + weight * 12.00
else:
  dr_cost = flat_charge + weight * 14.25
print("Total cost for Drone shipping: $",dr_cost)
