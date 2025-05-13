########  College school course registration code

reg = ""
math_reg = False
physic_reg = False
biology_reg = False

while True:    # terminal is open idenfinately (code blocks run indefinately) until code is exited
    reg = input("enter course: ").lower()
    if reg == "physics":
        if physic_reg:
            print (f"{reg} already registered for")
        else:
            physic_reg = True
            print (f"{reg} now registered")

    elif reg == "math":
        if math_reg:
            print (f"{reg} already registered for")
        else:
            math_reg = True
            print (f"{reg} now registered")

    elif reg == "biology":
        if biology_reg:
            print (f"{reg} already registered for")
        else:
            biology_reg = True
            print (f"{reg} now registered")

    elif reg == "help":
        print ('''
Available subject:
Math
Physics
Biology

When you have registered for all courses. Type COMPLETE in the terminal
               
''')
    
    elif reg == "complete":
         print ("Registrations completed. Thank you. Terminal locked.")

         break
    else:
        print ("Sorry, entry is invalid!")
