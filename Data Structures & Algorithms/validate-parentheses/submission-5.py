class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False

        parantheses = {')': '(', '}': '{', ']': '['}
        para_stack = []

        for para in s:
            if para in parantheses.keys() and para_stack and para_stack[-1] == parantheses[para]:
                para_stack.pop()
            else:
                para_stack.append(para)


        if len(para_stack) == 0:
            return True

        return False