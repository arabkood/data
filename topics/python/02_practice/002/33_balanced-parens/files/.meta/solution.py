def isBalanced(text):
    stack = []
    pairs = {"(": ")", "[": "]", "{": "}"}

    for char in text:
        if char in pairs:
            stack.append(char)
        elif char in pairs.values():
            if not stack or pairs[stack.pop()] != char:
                return False

    return len(stack) == 0
