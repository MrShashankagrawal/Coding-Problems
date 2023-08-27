def isValid(string):
    
    n = len(string)
    
    # Case 1: Checking for length of password.
    if n < 8 or n > 15:
        return False
        
    containDigit = False
    containSpace = False
    containUpper = False
    containLower = False
    containSpecial = False
    
    for char in string:
        # Case 2: Checking for space.
        if char == ' ':
            containSpace = True
            break
        
        # Case 3: Checking for digits.
        if char.isdigit():
            containDigit = True
            
        # Case 4: Checking for UpperCase.
        if char.isupper():
            containUpper = True
            
        # Case 5: Checking for LowerCase.
        if char.islower():
            containLower = True
            
        # Checking for special characters.
        if not char.isalnum():
            containSpecial = True
    
    if not containSpace and containDigit and containLower and containSpecial and containUpper:
        return True
            
    return False
