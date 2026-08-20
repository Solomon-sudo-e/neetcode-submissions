class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        total = 0

        for token in tokens:
            if token == "+" or token == "-" or token == "*" or token == "/":
                val1, val2 = stack.pop(), stack.pop()
                new_val = self.calculate_num(val1, val2, token)
                stack.append(int(new_val))
            else:
                stack.append(int(token))
        return stack[0]

    def calculate_num(self, val, total, token):
            match token:
                case "+":
                    return total + val
                case "-":
                    return total - val
                case "*":
                    return total * val
                case "/":
                    return int(total / val)
