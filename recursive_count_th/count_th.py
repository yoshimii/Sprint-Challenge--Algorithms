'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    print(word)
    if len(word) < 2:
        return 0
    if word == '':
        return 0
    if word[:2] == 'th':
        print(word[:2])
        return 1 + count_th(word[1:])
    else:
        return count_th(word[1:])

    # PSEUDOCODE
    # looping through string
    # check if first two letters are 'th'
    # if so return 1
    # else return 0
    # check if next two letters are th 
    # if so return 1
    # else return 0
    # if word is less than 0 or empty string return 0
