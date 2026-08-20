class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        stack = []
        
        for character in s:
            if character != "[" and character != "(" and character != "{":
                if len(stack) == 0:
                    return False

                if character == "]":
                    val = stack.pop()
                    if val != "[":
                        return False
                if character == "}":
                    val = stack.pop()
                    if val != "{":
                        return False
                if character == ")":
                    val = stack.pop()
                    if val != "(":
                        return False     
            else:
                stack.append(character)

        return True if len(stack) == 0 else False
        
            