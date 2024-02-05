items_names = (input("Enter Items Name"))
item_names = ('chocolate', 'juice', 'banana', 'shoes')
price = [2.5, 2.6, 4.2, 6.2]
quantity= [5, 1 , 2 , 2]
budget = 5.0
total_cost = sum(quantity * price for quantity, price in zip (quantity, price))

if total_cost <= budget:
 print("You're in Budget")

else:
 print(" sorry this will be Out from your Budget")