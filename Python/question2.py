import getpass

no_of_allowed_attempts = 3
invalid_attempts = 0
valid_attempts = 0

while invalid_attempts < no_of_allowed_attempts:
    supplied_pin = getpass.getpass(prompt='Enter your pin: ')
    supplied_pin = (int(supplied_pin))
    print("PIN entered: %s " % supplied_pin)

    if int(supplied_pin)==1234:
        print("CORRECT")
        valid_attempts += 1
        number_of_attempts = invalid_attempts + valid_attempts
        print("number of attempts: ", number_of_attempts)
        break

    else:
        print("INCORRECT")
        invalid_attempts += 1
        number_of_attempts = invalid_attempts + valid_attempts
        print("number of attempts: ", number_of_attempts)