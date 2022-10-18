print("Celsius to Fahrenheit = 1")
print("Celsius to Kelvin = 2")
print("Fahrenheit to Celsius = 3")
print("Fahrenheit to Kelvin = 4")
a = input("Number key Representing Convertion: ")
def C_to_F():
   c = float(input("The temperature in Celeus: "))
   C_to_F = round((c * 9 / 5) + 32)
   print(str(C_to_F) + 'F')
def F_to_C():
  f = float(input("The temperature in Fahrenheit: "))
  F_to_C = round((f-32) * 5 / 9, 2)
  print(str(F_to_C) + 'C')
def F_to_K():
  f = float(input("The temperature in Fahrenheit: "))
  F_to_K = round((f - 32) * 5 / 9 + 273.15, 2)
  print(F_to_K + 'K')
def C_to_K():
  K = float(input("The temperature in Celeus: "))
  C_to_K = round(K - 273.15)
  print(C_to_K + 'K')
if a == '1':
  C_to_F()
if a == '2':
  C_to_K()
if a == '3':
  F_to_C()
if a == '4':
  F_to_K()
if a >= '5':
  print("That's not a number key.")
  