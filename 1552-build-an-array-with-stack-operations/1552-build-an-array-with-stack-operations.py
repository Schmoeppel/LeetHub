class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        result = []

        target_pointer = 0
        stream_pointer = 1

        while target_pointer < len(target):
            result += ["Push", "Pop"]*(target[target_pointer]-stream_pointer)
            result.append("Push")
            stream_pointer = target[target_pointer]+1
            target_pointer += 1

        return result


