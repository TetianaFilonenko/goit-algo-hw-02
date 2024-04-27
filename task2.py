from collections import deque

def is_palindrom(text):
    text = text.lower().replace(" ", "")
    print(text)
    d = deque()
    for char in text:
        d.append(char)
    while len(d) > 0:
        r = d.pop()
        if len(d) > 0:
            l = d.popleft()
        else:
            l = None
        if r != l and l != None:
            return False
    return True

# Testing
print(is_palindrom("aabbcdcbbaa"))
print(is_palindrom("aabbcddcbbaa"))

print(is_palindrom("aabBcCbbaA"))
print(is_palindrom("aabB cCbbaA"))

print(is_palindrom("aabBcbbaA"))
print(is_palindrom("aabBc bbaA"))

print(is_palindrom("aabBcDbbaA"))
print(is_palindrom(""))
print(is_palindrom("qqqqqqqqqq"))
print(is_palindrom("qqqqqqqqq"))
print(is_palindrom("q"))
