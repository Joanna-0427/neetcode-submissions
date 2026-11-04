class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort() #排序
        k = len(meetings)
        rooms = [i for i in range(n)]
        heapq.heapify(rooms)
        busy = []
        roomcount = {}
        i = 0
        while i < k:
            while busy and busy[0][0] <= meetings[i][0]: 
                endtime, roomnum = heapq.heappop(busy)
                heapq.heappush(rooms,roomnum)

            if rooms: #1.每次分配一个房间，因为分房间之前都要先检查有没有busy需要先pop的会议室
                roomnum = heapq.heappop(rooms)
                roomcount[roomnum] = roomcount.get(roomnum,0) + 1
                end = meetings[i][1]
                heapq.heappush(busy,(end,roomnum))

            elif not rooms: #if rooms 和not rooms两个独立判断，不会在一个执行完之后紧接着执行另一个
                delta = meetings[i][1] - meetings[i][0]
                meetings[i][0] = busy[0][0]
                meetings[i][1] = busy[0][0] + delta
                end, roomnum = heapq.heappop(busy)
                heapq.heappush(busy,(meetings[i][1], roomnum)) #等后续while busy分配，会一次跳出来多个会议室，有些会议室会被捡漏，还没有延迟时间的会议可以直接用，会导致endtime错误；
                roomcount[roomnum] = roomcount.get(roomnum,0) + 1
                
            
            i += 1

                
        
            

        return max(roomcount,key=roomcount.get)

            

