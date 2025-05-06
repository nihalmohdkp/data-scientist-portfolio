phonebook = {}

while True:
    print('\nPhone Book Menu : ')
    print('1.Add Contact')
    print('2.View Contact')
    print('3.Update Contact')
    print('4.Display contact')
    print('5.Delete contact')
    print('6.Exit')

    choice = int(input('Enter your choice : '))

    if choice ==1:
        sub={}

        name= input('enter your name : ')
        phone= int(input('enter your phone number : '))
        email= input('enter your email id : ') 
        sub['name']=name
        sub['phone']=phone
        sub['email']=email
        phonebook[name]=sub
        print(sub)
        print (phonebook)
        
#########################################################

    elif choice==2:
        name= input('enter the name of contact to view : ')
        if name in phonebook :
            print (name,phonebook[name])
            
        else :
            print ('error')

            ########################################

    elif choice ==3 :
        name= input('enter the name of contact to update : ')
        if name in phonebook:
            ch=int(input('''1.number\n2.email\nenter ur choice : '''))
            if ch == 1:
                ph= int(input('enter new phone number : '))
                phonebook[name].update({'phone':ph})
              
                print(phonebook[name])
            elif ch==2 :
                email= input('enter your new email id : ')
                phonebook[name].update({'email':email})
                print(phonebook[name])
            else:
                print("invalid number \nplease check if your number is correct . ")
        else :
            print('invalid contact .')

            #################################################
    elif choice ==4:
        if phonebook:
            for name, phone in phonebook.items():
                print(f"{name}: {phone}")
        else:
            print("No contacts in phone book.")
        #################################################

    elif choice ==5:
        name=(input('enter the name of the contact to delete details : '))
        if name in phonebook:
            dl=int(input('choose what to delete:: \n1.phone.no \n2.email\n'))
            if dl==1:
                del phonebook[name]["phone"]
            elif dl==2:
                del phonebook[name]["email"]
            elif dl>2:
                print('This choice is not available : ')
        else:
            print('name not in phone book \n try another name ;-)')
            #################################################
    elif choice==6:
        break

        
