class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        answer = []

        for query in queries:
            for word in dictionary:
                difference = 0

                for i in range(len(query)):
                    if query[i] != word[i]:
                        difference += 1

                if difference <= 2:
                    answer.append(query)
                    break

        return answer