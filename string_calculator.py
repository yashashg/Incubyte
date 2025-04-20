
def add(number):
    sum = 0
    #Refactored code

    #checking if string is empty
    if number == "":                
        return 0
    else:
        # Splitting string with comma
        spliting = number.split(",")
        for n in spliting:
            sum = sum + int(n)
        return(sum)
    
