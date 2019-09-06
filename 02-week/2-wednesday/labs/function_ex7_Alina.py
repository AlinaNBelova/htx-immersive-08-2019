#only_odds function
#numbers =[11,20,42,97,23,10]
def only_evens(list_of_numbers):
    result=[]
    import function_ex5_Alina
    for number in list_of_numbers:
        if function_ex5_Alina.is_odd(number):
            result.append(number)
    return result
#print(only_evens(numbers))