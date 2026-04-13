class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # init res -> all 0 -> [0, 0, ..., 0]
        # stack = [] -> monotonically decreasing stack -> track (idx, temp) of list
        # enumerate temperatures (idx, temp):
        #   while stack has vals & top val (curr least warm) < temp:
        #       pop top stack vals (stack_idx, stack_temp)
        #       set res[stack_pop_idx] = (idx - stack_idx)
        #   append (idx, temp) to stack -> it is empty or temp is smaller than cur top val
        # return res -> remaining temps w/out warmer days after alr set to 0
        res = [0] * len(temperatures)
        stack = []
        for idx, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                stack_idx, stack_temp = stack.pop()
                res[stack_idx] = idx - stack_idx
            stack.append([idx, temp])
        return res


        # Brute Force: time -> O(n^2)
        # result = []
        # for i in range(len(temperatures)):
        #   future_warm_days = 0
        #   no_warmer_days = True
        #   for j in range(i + 1, len(temperatures)):
        #     future_warm_days += 1
        #     if temperatures[j] > temperatures[i]:
        #         no_warmer_days = False
        #         break
        #     else:
        #         continue
        #   result.append(future_warm_days) if no_warmer_days is False else result.append(0)
        # return result
