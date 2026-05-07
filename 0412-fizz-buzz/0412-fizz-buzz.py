class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = [""]*(n+1)
        for i in range(n+1):
            if i%3 == 0 and i%5 == 0:
                answer[i] = "FizzBuzz"
            elif i%3 == 0:
                answer[i] = "Fizz"
            elif i%5 == 0:
                answer[i] = "Buzz"
            else:
                answer[i] = str(i)
        return answer[1:]