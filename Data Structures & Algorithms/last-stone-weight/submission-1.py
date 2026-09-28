import heapq as hq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0
        if len(stones) == 1:
            return stones[0]
 
        hq.heapify_max(stones)
        while len(stones) > 1:
            if stones[0] - stones[1] == 0:
                hq.heappop_max(stones)
                hq.heappop_max(stones)
                if not stones:
                    return 0
            elif stones[0] - stones[1] > 0:
                tempStone = hq.heappop_max(stones) - hq.heappop_max(stones)
                hq.heappush_max(stones, tempStone)
        return stones[0]

