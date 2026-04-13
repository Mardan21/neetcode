class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Brute Force: time -> O(n^2)
        result = []
        for i in range(len(temperatures)):
          future_warm_days = 0
          no_warmer_days = True
          for j in range(i + 1, len(temperatures)):
            future_warm_days += 1
            if temperatures[j] > temperatures[i]:
                no_warmer_days = False
                break
            else:
                continue
          result.append(future_warm_days) if no_warmer_days is False else result.append(0)
        return result
