import re              #imported library

def add(number):
    sum = 0

    #checking if string is empty
    if number == "":                
        return 0
    else:
        delimiters = [",", "\n"]
        if number.startswith("//"):

            #Separates delimiter and numbers
            delimiter_part, number = number.split("\n", 1)

            #Extracts custom delimiter which were seperated
            custom_delimiter = delimiter_part[2:]

            #Overrides default delimiters
            delimiters = [custom_delimiter]

        # Create a regex pattern from all delimiters
        pattern = "|".join(map(re.escape, delimiters))
        spliting = re.split(pattern, number)
        
        for n in spliting:
            if(int(n)<=0):
                raise ValueError(f"negative numbers not allowed {n}")
            else:
                sum = sum + int(n)

        return(sum)
    
