#only_evens function
#numbers =[11,20,42,97,23,10]
def only_evens(list_of_numbers):
    result=[]
    import function_ex4_Alina
    for number in list_of_numbers:
        if function_ex4_Alina.is_even(number):
            result.append(number)
    return result
#print(only_evens(numbers))


