
def add(number):
    if number == "":                #Upated the code
        return 0
    
    if "," in number:
        spliting = number.split(",")

        for n in spliting:
            sum = sum + int(n)
        return(sum)
    return(int(number))
    
