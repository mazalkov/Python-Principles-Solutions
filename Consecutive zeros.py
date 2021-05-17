# https://pythonprinciples.com/challenges/Consecutive-zeros/


def consecutive_zeros(string):
    
    count = 0
    result = 0
    
    for i in range(0, len(string)):
        
        if (string[i] == "1"):
            count = 0
            
        else:
            count += 1
            result = max(result, count)
            
    return result
