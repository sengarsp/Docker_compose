import os
IP=10.0.2.15
while True:

    print('''         
             Press 1: To enter WordPress
             Press 2: To enter Joomla
             Press 3: To enter Ghost
             Press 4: To exit from menu''')


    ch=int(input())
    
    if int(ch) == 1:
        print(" Launching Wordpress .....")
        print(IP,":8081")

    elif int(ch) == 2:
        print("Launching Joomla ........ ")
        print(IP,":8082")

    elif int(ch) == 3:
        print("Launching Ghost ........ ")
        print(IP,":8083")
    
    elif int(ch) == 4:
        os.system( exit() )

    else:
        print("eror")
    
    input("Enter to continue......")
    os.system("clear")
    
