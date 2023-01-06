the_height = float(input("Enter the Height:"))
the_weight = float(input("Enter the Weight:"))
the_bmi = the_weight/(the_height/100)**2
print("Your Body Mass Index is", the_bmi)
if the_bmi <= 18.5:
    print("You're underweight")
elif the_bmi <= 25.5:
    print("you're Healthy")
elif the_bmi <= 29.5:
    print("You're OverWeight")
else:
    print("You should consult Doctor")