#coding practise
#BMI calculator
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

#write your code here

convert_height = float(height)
convert_weight = int(weight)
bmi_cal = convert_weight / convert_height ** 2
bmi_cal = convert_weight / (convert_height * convert_height)
print(int(bmi_cal))