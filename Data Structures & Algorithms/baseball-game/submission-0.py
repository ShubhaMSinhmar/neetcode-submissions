class Solution:
    def calPoints(self, operations: List[str]) -> int:
        answer = []
        for ops in operations:
            if ops == "D":
                result = answer[-1] * 2
                answer.append(result)
            elif ops == "C":
                answer.pop()
            elif ops == "+":
                result = answer[-1] + answer[-2]
                answer.append(result)
            else:
                answer.append(int(ops))

        return sum(answer)