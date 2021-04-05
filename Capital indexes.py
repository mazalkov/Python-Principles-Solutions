# https://pythonprinciples.com/challenges/Capital-indexes/


def capital_indexes(string):
    
    indices = []
    
    for i in range(len(string)):
        if string[i].isupper():
            indices.append(i)
            
    return indices
