import re              #imported library

def add(number):
    sum = 0

    #checking if string is empty
    if number == "":                
        return 0
    else:
        # Splitting string with re library
        spliting = re.split(r"[,\n]", number)
        for n in spliting:
            sum = sum + int(n)
        return(sum)
    
