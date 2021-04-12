# https://pythonprinciples.com/challenges/Online-status/


def online_count(dictionary):
    
    number_online = 0
    
    for i, (key, value) in enumerate(dictionary.items()):
        if value == 'online':
            number_online += 1
            
    return number_online
