class MatchingParenthesis:
    @staticmethod
    def check_if_balanced(expr):
        opening = set('([{')
        new = set(')]}{[(')
        match = set([('(', ')'), ('[', ']'), ('{', '}')])
        stack = []
        stackcount = []
        for i, char in enumerate(expr, 1):
            if char not in new:
                continue
            elif char in opening:
                stack.append(char)
                stackcount.append(i)
            else:
                if len(stack) == 0:
                    return False
                last_open = stack.pop()
                last_index = stackcount.pop()
                if (last_open, char) not in match:
                    return False
        length = len(stack)
        if length != 0:
            elem = stackcount[0]
        return length == 0

    @staticmethod
    def is_balanced(input_string):
        return "YES" if(MatchingParenthesis.check_if_balanced(input_string)) else "NO"
