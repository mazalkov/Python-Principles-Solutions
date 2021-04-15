# https://pythonprinciples.com/challenges/Double-letters/


def double_letters(string):
    
    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            return True
            break
            
    return False
