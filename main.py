
print('''
#                               #     #                          #####                                                                
#       ######   ##   #####      #   #  ######   ##   #####     #     #   ##   #       ####  #    # #        ##   #####  ####  #####  
#       #       #  #  #    #      # #   #       #  #  #    #    #        #  #  #      #    # #    # #       #  #    #   #    # #    # 
#       #####  #    # #    #       #    #####  #    # #    #    #       #    # #      #      #    # #      #    #   #   #    # #    # 
#       #      ###### #####        #    #      ###### #####     #       ###### #      #      #    # #      ######   #   #    # #####  
#       #      #    # #            #    #      #    # #   #     #     # #    # #      #    # #    # #      #    #   #   #    # #   #  
####### ###### #    # #            #    ###### #    # #    #     #####  #    # ######  ####   ####  ###### #    #   #    ####  #    # 
''')


while True:
    user_input = int(input("Type the year you want check? "))

    if user_input % 4 != 0:
        print(f"{user_input} is a common year")
    elif user_input % 100 != 0:
        print(f"{user_input} is a leap year")
    elif user_input % 400 != 0:
        print(f"{user_input} is a common year")
    else:
        print(f"{user_input} is a leap year")
