'''
Find the last element of the given argument(s).

Examples
last([1, 2, 3, 4]) ==>  4
last("xyz")        ==> "z"
last(1, 2, 3, 4)   ==>  4
In javascript and CoffeeScript a list will be an array, a string or the list of arguments.

'''

def last(*args):
    #your awesome code here
    if not args:
        return None
    
    lst = args[-1]
    
    if isinstance(lst, (list, str)):
        return lst[-1]
    else:
        return lst
