class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # seen is a hashmap = frequency : number
        seen = {} 
        heap = []
        for i in range(len(nums)):
            seen[nums[i]] = seen.get(nums[i], 0) +1
        for num, freq in seen.items():
            heapq.heappush(heap, (freq,num))
            if len(heap) > k:
                heapq.heappop(heap)
        return [i[1] for i in heap]

