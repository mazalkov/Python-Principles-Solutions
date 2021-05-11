# https://pythonprinciples.com/challenges/Solution-validation/


def validate(code):
    
    if "def" not in code:
        return "missing def"
        
    elif ":" not in code:
        return "missing :"
        
    elif "(" not in code:
        return "missing paren"
        
    elif ")" not in code:
        return "missing paren"
        
    elif ('()' in code) and ("'()'" not in code):
        return "missing param"
        
    elif "    " not in code:
        return "missing indent"
        
    elif "validate" not in code:
        return "wrong name"
        
    elif "return" not in code:
        return "missing return"
        
    else:
        return True
