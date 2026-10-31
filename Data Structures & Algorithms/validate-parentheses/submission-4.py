class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False

        parantheses = {')': '(', '}': '{', ']': '['}
        para_stack = []

        for para in s:
            if para == "[" or para == "(" or para == "{":
                para_stack.append(para)
            elif para_stack and para_stack[-1] == parantheses[para]:
                para_stack.pop()
            else:
                para_stack.append(para)


        if len(para_stack) == 0:
            return True

        return False