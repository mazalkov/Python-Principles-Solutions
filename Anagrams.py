# https://pythonprinciples.com/challenges/Anagrams/


def is_anagram(string1, string2):
    
    return (sorted(string1) == sorted(string2))
