#Fitness Tracker.
daily_steps= int(input("Enter the number of steps:"))

distance_walked = int(input("Enter the Distance:"))

calories_burned = int(input("enter the number of calories you have burned:"))

average_steps_per_Week = (daily_steps) / 7

total_distance = (average_steps_per_Week) * (distance_walked)

print("The total distance you have covered in a month is",{total_distance},"Km")