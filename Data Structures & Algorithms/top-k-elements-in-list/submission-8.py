class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        freqs = {} # key is times of appearance, value is item @ index 
        for i in range(len(nums)):
            freqs[nums[i]] = freqs.get(nums[i], 0) +1
        for num,val in freqs.items():
            heapq.heappush(heap, (val,num))
            while len(heap) > k:
                heapq.heappop(heap)
        return [t[1] for t in heap]