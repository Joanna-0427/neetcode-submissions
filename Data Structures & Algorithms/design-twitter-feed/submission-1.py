class Twitter:

    def __init__(self):
        self.count = 0
        self.followmap = defaultdict(set)
        self.Tweetmap = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.Tweetmap[userId].append([self.count,tweetId])
        self.count -= 1


    def getNewsFeed(self, userId: int) -> List[int]:
        self.followmap[userId].add(userId)
        minheap = []
        res = []
        for id in self.followmap[userId]:
            if id in self.Tweetmap:
                index = len(self.Tweetmap[id]) - 1
                count, tweetId = self.Tweetmap[id][index]
                heapq.heappush(minheap,[count, tweetId, id, index])
        
        while minheap and len(res) < 10:
            count, tweetId, id, index = heapq.heappop(minheap)
            res.append(tweetId)
            if index > 0:
                count, tweetId = self.Tweetmap[id][index-1]
                heapq.heappush(minheap, [count, tweetId, id, index-1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followmap[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followmap[followerId]:
            self.followmap[followerId].remove(followeeId)

        
