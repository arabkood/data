def evaluate(expression):
    def precedence(op):
        if op in ['+', '-']:
            return 1
        if op in ['*', '/']:
            return 2
        return 0

    def apply_op(operators, values):
        op = operators.pop()
        right = values.pop()
        left = values.pop()
        if op == '+':
            values.append(left + right)
        elif op == '-':
            values.append(left - right)
        elif op == '*':
            values.append(left * right)
        elif op == '/':
            values.append(left / right)

    expression = expression.replace(' ', '')
    operators = []
    values = []
    i = 0

    while i < len(expression):
        if expression[i].isdigit():
            num = 0
            while i < len(expression) and (expression[i].isdigit() or expression[i] == '.'):
                num = num * 10 + int(expression[i]) if expression[i] != '.' else num
                i += 1
            i -= 1
            values.append(num)
        elif expression[i] == '(':
            operators.append(expression[i])
        elif expression[i] == ')':
            while operators and operators[-1] != '(':
                apply_op(operators, values)
            operators.pop()
        elif expression[i] in ['+', '-', '*', '/']:
            while (operators and operators[-1] != '(' and
                   precedence(operators[-1]) >= precedence(expression[i])):
                apply_op(operators, values)
            operators.append(expression[i])
        i += 1

    while operators:
        apply_op(operators, values)

    return values[0]
