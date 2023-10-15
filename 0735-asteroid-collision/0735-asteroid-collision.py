class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        old_asteroids = []
        while len(old_asteroids) != len(asteroids):
            old_asteroids = asteroids.copy()
            idx = 0
            while idx < len(asteroids)-1:
                if asteroids[idx] > 0 and asteroids[idx+1] < 0:
                    if asteroids[idx] > -asteroids[idx+1]:
                        asteroids.pop(idx+1)
                    elif asteroids[idx] < -asteroids[idx+1]:
                        asteroids.pop(idx)
                    elif asteroids[idx] == -asteroids[idx+1]:
                        asteroids.pop(idx+1)
                        asteroids.pop(idx)
                idx += 1
            
        return asteroids
                    