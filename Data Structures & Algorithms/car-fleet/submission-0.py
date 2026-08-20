class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        merged_dict = dict(zip(position, speed))
        sorted_arr = [list(item) for item in sorted(merged_dict.items(), key=lambda x: x[0])]
        
        times = []
        while len(sorted_arr):
            position, speed = sorted_arr.pop()
            time_to_arrive = float((target - position)/speed)
            if not times:
                times.append(time_to_arrive)
            elif times and times[-1] < time_to_arrive:
                times.append(time_to_arrive)
        return len(times)
        
