class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        result = []

        for asteroid in asteroids:
            if asteroid > 0:
                result.append(asteroid)
            else:
                while result and result[-1] > 0:
                    prev_asteroid = result.pop()
                    if prev_asteroid + asteroid == 0:
                        break
                    elif prev_asteroid > -asteroid:
                        result.append(prev_asteroid)
                        break
                else:
                    result.append(asteroid)
        return result

                    