def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

class Solution:

    def evalRPN(self, tokens: List[str]) -> int:
        operands = []

        for token in tokens:
            if is_number(token):
                operands.append(token)
            else:
                right = operands.pop()
                left = operands.pop()
                if token == "+":
                    operands.append(int(left) + int(right))
                elif token == "-":
                    operands.append(int(left) - int(right))
                elif token == "*":
                    operands.append(int(left) * int(right))
                elif token == "/":
                    operands.append(int(left) / int(right))
                


        return int(operands[0])