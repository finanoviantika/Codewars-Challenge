'''
Write a function that takes a single string (word) as argument. The function must return an ordered list containing the indexes of all capital letters in the string.

Example (Input --> Output)
"CodEWaRs" --> [0,3,4,6]

'''

def capitals(word):
    #your code here
    kata = []
    i = 0
    
    for letter in word:
        if letter.isupper():
            kata.append(i)
        i += 1
    
    return kata