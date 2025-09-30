class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for ast in asteroids:
            while stack and stack[-1] > 0 and ast < 0:
                diff = ast + stack[-1]
                if diff < 0:
                    stack.pop()
                elif diff == 0:
                    stack.pop()
                    break
                else:
                    break
            else:
                stack.append(ast)
        return stack