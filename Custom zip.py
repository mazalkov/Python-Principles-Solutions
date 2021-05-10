# https://pythonprinciples.com/challenges/Custom-zip/


def zap(a, b):
    
    zap_list = []
    
    for i in range(len(a)):
        zap_list.append((a[i], b[i]))
        
    return zap_list
