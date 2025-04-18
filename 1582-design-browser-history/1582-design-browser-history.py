class BrowserHistory:

    def __init__(self, homepage: str):
        self.history_stack = [homepage]
        self.forward_stack = []

    def visit(self, url: str) -> None:
        self.history_stack.append(url)
        self.forward_stack = []

    def back(self, steps: int) -> str:
        for i in range(min(steps, len(self.history_stack)-1)):
            self.forward_stack.append(self.history_stack.pop())
        return self.history_stack[-1]

    def forward(self, steps: int) -> str:
        for i in range(min(steps, len(self.forward_stack))):
            self.history_stack.append(self.forward_stack.pop())
        return self.history_stack[-1]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)