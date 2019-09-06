# Farenheit to Celsius conversion
temp_Fahr = int(input('Enter the temperature in Fahrenheit: '))
def Fahr_convector(temp_):
    #temp_Fahr = int(input('Enter the temperature in Fahrenheit: '))
    temp_Cels = (temp_Fahr- 32) * 5/9
    print(f'{temp_Fahr} Fahrenheit is {int(temp_Cels)} Celsius')
    return temp_Cels
Fahr_convector(temp_Fahr)
