ask_the_name = input('Enter the name ')
ask_the_subject = input('Enter the subject ')
def madlib_mad(name,subject):
    if name == '':
       name ='Sam'
    else:
         name= name
    if subject =='':
       subject='beer'
    else:
        subject= subject

    print (f'{name}\'s favorite subject is {subject}')
    return


madlib_mad (ask_the_name, ask_the_subject)
