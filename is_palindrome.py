import re

def is_palindrome(string):
    forwards = ''.join(re.findall(r'[a-z]+', string.lower()))
    backwards = forwards[::-1]

    return forwards == backwards
