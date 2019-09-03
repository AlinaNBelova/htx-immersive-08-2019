#exercise_1
name = input('What is your name?')
print ("Hello," + name)

#exercise_2
name = name.upper()
print ('HELLO,' + name + '!')
name_length =  len(name)
print (f'YOUR NAME HAS {name_length} LETTERS IN IT')

#exercise_3
name = input('What is your name?')
subject = input ('What is your favorite  subject in school?')
print (f'{name}\'s favorite subject in school is {subject}')


#exercise_4
day = int(input('Enter a number of the day from 0 to 6'))
if  day <0  and day> 6:
    print('Sorry, this  is  wrong number. Please try again...')
else:
    if day == 0:
        print ('This is Sunday')
    if day == 1:
        print ('This is Monday')
    if day == 2:
        print ('This is Tuesday')
    if day == 3:
        print ('This is Wednesday')
    if day == 4:
        print ('This is Thursday')
    if day == 5:
        print ('This is Friday')
    if day == 6:
        print ('This is Saturday') 


#exersice_5
day = int(input('Enter a number of the day from 0 to 6'))
if  day <0  and day> 6:
    print('Sorry, this  is  wrong number. Please try again...')
else:
    if day == 0 or day == 6:
        print('Lucky you, sleep in')
    else:
        print('Go to work')

#exercise_6
#Celsius to Fahrenheit
C = int(input('Enter the temperature in C' ))
F = C *1.8+32
print (f'Temperature in Fahrenheit is {int(F)}')


#exersicise_7
"""Tip Calculator"""
bill = float(input('Enter total bill amount '))
level_of_service = input('How was the service? type  "good", "fair" or "bad"   ')
if  level_of_service == 'bad':
    tip= 0.1
elif level_of_service == 'fair':
    tip = 0.15
else:
    tip = 0.2
tip_amount = bill*tip
print(f'Tip amount is {tip_amount:.2f} $')
total_amount = bill+ tip_amount
print (f'Total amount to pay is {total_amount:.2f} $')

#exercise_8

"""Tip Calculator 2"""
bill = float(input('Enter total bill amount '))
level_of_service = input('How was the service? type  "good", "fair" or "bad"   ')
if  level_of_service == 'bad':
    tip= 0.1
elif level_of_service == 'fair':
    tip = 0.15
else:
    tip = 0.2
tip_amount = bill*tip
print(f'Tip amount   $ {tip_amount:.2f} ')
total_amount = bill+ tip_amount
print (f'Total amount to pay is  ${total_amount:.2f} ')
number_of_person = int(input('Split how many ways?' ))
amount_per_person = total_amount/number_of_person
print(f'Amount per person is {amount_per_person:.2f}')


#exercise_9
n = 0
while n <10:
    n+=1    
    print(n)


#exercise_10
coin = 0
yes_or_no = ' '
while  yes_or_no != 'no':
     print (f'You have {coin} coins.')
     yes_or_no = input('Do you want another coin? Enter yes or no')
     coin +=1
print('bye')