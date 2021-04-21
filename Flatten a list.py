# https://pythonprinciples.com/challenges/Flatten-a-list/


def flatten(list_of_lists):
    
    single_list = []
    
    for sublist in list_of_lists:
        for item in sublist:
            single_list.append(item)
        
    return single_list
