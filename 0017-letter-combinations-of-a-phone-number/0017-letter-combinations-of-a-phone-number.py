class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        num_2_letters = {"2": "abc",
                            "3": "def",
                            "4": "ghi",
                            "5": "jkl",
                            "6": "mno",
                            "7": "pqrs",
                            "8": "tuv",
                            "9": "wxyz"}

        combinations = [""]
        temp = []
        for digit in digits:
            temp = []
            for letter in num_2_letters[digit]:
                for combination in combinations:
                    temp.append(combination+letter)
            combinations = temp
        return combinations