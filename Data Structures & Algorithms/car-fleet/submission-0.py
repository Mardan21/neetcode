class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_ps_pairs = [[pos, speed] for pos, speed in zip(position, speed)]

        stack = []
        for pos, speed in sorted(car_ps_pairs)[::-1]: # Reverse Sorted Order
            time_to_target = (target - pos) / speed
            stack.append(time_to_target) # Car's time to reach target
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)

