def is_symmetrical(text):
    stack = []
    for char in text:
        if char in ["{", "(", "["]:
            stack.append(char)
        elif char in ["}", ")", "]"]:
            prev_bracket = stack.pop()
            if (
                (char == "}" and prev_bracket != "{")
                or (char == ")" and prev_bracket != "(")
                or (char == "]" and prev_bracket != "[")
            ):
                return False
    return len(stack) == 0


print(is_symmetrical("( ){[ 1 ]( 1 + 3 )( ){ }}"))  # True
print(is_symmetrical("( 23 ( 2 - 3)"))  # False
print(is_symmetrical("( 11 }"))  # False
print(is_symmetrical("((())){{{{}}}}(((())))"))  # True
print(is_symmetrical("((({{{{(((("))  # False
