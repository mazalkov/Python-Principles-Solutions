# https://pythonprinciples.com/challenges/Middle-letter/


def mid(string):
    
    if len(string) % 2 == 0:
        return ""
        
    else:
        return string[int(len(string)/2)]
