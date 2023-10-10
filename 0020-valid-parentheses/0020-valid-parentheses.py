class Solution:
    def isValid(self, s: str) -> bool:
        bracket_stack = []
        according_bracket = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        for bracket in s:
            if bracket in ['(','{','[']:
                bracket_stack.append(bracket)
            else:
                if len(bracket_stack) <= 0:
                    return False
                if according_bracket[bracket_stack[-1]] == bracket:
                    bracket_stack.pop()
                else:
                    return False

        if len(bracket_stack) > 0:
            return False

        return True