num_servings = int(input("Enter number of serving"))

ingredients = ["meat", "oil", "rice", "water", "yogurt", "masaly"]

amounts = [ 1 , 2 , 4 , 6 , 1 , 3 ]

adjusted_quantities = [amount * num_servings for amount in amounts]

print (adjusted_quantities)