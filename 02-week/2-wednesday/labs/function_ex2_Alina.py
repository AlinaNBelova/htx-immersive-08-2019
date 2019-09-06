#Celsius to Fahrenheit conversion
temp_Cels = int(input( 'Enter the temperature in Celsius'))
def  temp_convector(temp_Cels):
    temp_Fahr = (temp_Cels* 9/5)+32
    print(f'{temp_Cels} Celsius is {int(temp_Fahr)} Fahrenheit ')
    return temp_Fahr
temp_convector(temp_Cels)
