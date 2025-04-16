class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        stack = []

        for i in range(1, len(path)):
            if path[i] == '' or path[i] == '.':
                continue
            if path[i] == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(path[i])

        return "/" + "/".join(stack)

        