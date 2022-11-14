import what ever required
def main():
    call showOPtions.py
    number = call takeOption.py
    call Pet_service.py with above number as parameter
    if pet_service returns false then show error as "please contact  admin"
    if pet_service returns true then show options
def take_input_from_user_as_y_or_n():
    show options ( " DO you want to continue y/n ? )
    take input and return boolean representing to continue or stop
    use if statement to check if user entered y then return true
    use if statement to check if user entered n then return false
    if any other input given print("show him gaali")
        and call  this function again like so take_input_from_user_as_y_or_n()
shouldContinue = True
while(user  not selected n- shouldContinue)
    main()
    shouldContinue = take_input_from_user_as_y_or_n()

    