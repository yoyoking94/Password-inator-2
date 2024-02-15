import string
from random import *

## ==== Import backend ==== ##

def password(array):
        print(array)
        
        passwordMin = 15
        passwordMax = 15
        uppers = string.ascii_uppercase
        lowers = string.ascii_lowercase
        symbols = string.punctuation
        numbers = string.digits
        
        if len(array) == 1:
                for arr in array:
                        if arr == "Include upper letters": 
                                return ''.join(choice(uppers) for x in range(randint(passwordMin, passwordMax)))
                        
                        elif arr == "Include lower letters":
                                return ''.join(choice(lowers) for x in range(randint(passwordMin, passwordMax)))
                        
                        elif arr == "Include numbers":
                                return ''.join(choice(numbers) for x in range(randint(passwordMin, passwordMax)))
                        
                        elif arr == "Include symbols":
                                return ''.join(choice(symbols) for x in range(randint(passwordMin, passwordMax)))
                        
        elif len(array) == 2:
                if "Include upper letters" in array and "Include lower letters" in array:
                        return ''.join(choice(uppers + lowers) for x in range(randint(passwordMin, passwordMax)))
                elif "Include upper letters" in array and "Include numbers" in array:
                        return ''.join(choice(uppers + numbers) for x in range(randint(passwordMin, passwordMax)))
                elif "Include upper letters" in array and "Include symbols" in array:
                        return ''.join(choice(uppers + symbols) for x in range(randint(passwordMin, passwordMax)))
                elif "Include lower letters" in array and "Include numbers" in array:
                        return ''.join(choice(lowers + numbers) for x in range(randint(passwordMin, passwordMax)))
                elif "Include lower letters" in array and "Include symbols" in array:
                        return ''.join(choice(lowers + symbols) for x in range(randint(passwordMin, passwordMax)))
                elif "Include numbers" in array and "Include symbols" in array:
                        return ''.join(choice(numbers + symbols) for x in range(randint(passwordMin, passwordMax)))
                
        elif len(array) == 3:
                if "Include upper letters" in array and "Include lower letters" in array and "Include numbers" in array:
                        return ''.join(choice(uppers + lowers + numbers) for x in range(randint(passwordMin, passwordMax)))
                elif "Include upper letters" in array and "Include lower letters" in array and "Include symbols" in array:
                        return ''.join(choice(uppers + lowers + symbols) for x in range(randint(passwordMin, passwordMax)))
                elif "Include upper letters" in array and "Include numbers" in array and "Include symbols" in array:
                        return ''.join(choice(uppers + numbers + symbols) for x in range(randint(passwordMin, passwordMax)))
                elif "Include lower letters" in array and "Include numbers" in array and "Include symbols" in array:
                        return ''.join(choice(lowers + numbers + symbols) for x in range(randint(passwordMin, passwordMax)))
        
        elif len(array) == 4:
                return ''.join(choice(uppers + lowers + numbers + symbols) for x in range(randint(passwordMin, passwordMax)))
        
        else:
                return 'Select params'
        