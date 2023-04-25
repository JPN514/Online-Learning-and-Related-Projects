# create the initial variables below
age = 30
sex = 1
bmi = 20
num_of_children = 0
smoker = 0

# Add insurance estimate formula below
insurance_cost = 250 * age - 128 * sex + 370 * bmi +425 * num_of_children + 24000*smoker - 12500
print("The cost of this person's insurance is {} dollars.".format(insurance_cost))

# Age Factor
age += 4
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi +425 * num_of_children + 24000*smoker - 12500

change_in_cost = new_insurance_cost - insurance_cost
print("The change in cost of insurance after increasing the age by 4 years is {} dollars.".format(change_in_cost))
# BMI Factor
age = 30
bmi += 3.1

new_insurance_cost = 250 * age - 128 * sex + 370 * bmi +425 * num_of_children + 24000*smoker - 12500

change = new_insurance_cost - insurance_cost
print("The change in estimated insurance cost after increasing BMI by 3.1 is {} dollars.".format(change))
# Male vs. Female Factor
sex = 1
new_insurance_cost = 50 * age - 128 * sex + 370 * bmi +425 * num_of_children + 24000*smoker - 12500
change = new_insurance_cost - insurance_cost
print("The change in estimated cost for being male instead of female is {} dollars.".format(change))