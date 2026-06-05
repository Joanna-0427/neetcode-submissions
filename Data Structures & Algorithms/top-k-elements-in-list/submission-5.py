class Solution:
    import heapq
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # res = defaultdict(list)

        # dic = {}
        # for n in nums:
        #     dic[n] = dic.get(n,0) + 1
        # for key, value in dic.items():
        #     res[value].append(key)

        # ans = []
        # for freq in range(len(nums),0,-1):
        #     if freq in res:
        #         for num in res[freq]:
        #             ans.append(num)
        #             if len(ans) == k:
        #                 return ans


        # heap =[]
        # for key, value in dic.items():
        #     heapq.heappush(heap,(value,key))
        #     if len(heap) > k:
        #         heapq.heappop(heap)
        # return [key for value,key in heap]

        count = Counter(nums)
        # minheap = []
        # for k, v in count.items():
        #     heapq.heappush(minheap,[v, k])
        #     if len(minheap) > k:
        #         heapq.heappop(minheap)
        # return [k for v, k in heap]

        minheap = [[v, k] for k, v in count.items()]
        heapq.heapify(minheap)
        while len(minheap) > k:
            heapq.heappop(minheap)
        return [k for v, k in minheap]
        




