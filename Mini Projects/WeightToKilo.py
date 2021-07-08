weight_pounds = input("Please enter your weight in pounds: ")
## My way, convert and save float into weight
weight_pounds = float(weight_pounds)
## Vid way, convert to float when you need it in the equation
##weight_kilo = float(weight_pounds) * .454
weight_kilo = weight_pounds * .454

print("Your weight in kilos is " + str(weight_kilo))

