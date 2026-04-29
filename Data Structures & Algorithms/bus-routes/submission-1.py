from collections import defaultdict, deque
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        
        if source==target: 
            return 0
        
        stop_bus = defaultdict(list)
        
        for bus, route in enumerate(routes): 
            for stop in route: 
                stop_bus[stop].append(bus)

        q = deque([(source, 0)])
        vis_bus = set()

        while q: 
            stop, cnt = q.popleft()

            if stop==target: 
                return cnt

            for bus in stop_bus[stop]: 
                if bus not in vis_bus: 
                    vis_bus.add(bus)
                    for new_stop in routes[bus]: 
                        q.append((new_stop, cnt+1))
        
        return -1
