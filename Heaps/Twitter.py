import heapq
import collections

class Twitter:
    priority=0
    def __init__(self):
        pass
        self.post_mapping=collections.defaultdict(list)
        self.follower_mapping=collections.defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        Twitter.priority+=1
        self.post_mapping[userId].append([Twitter.priority,tweetId])

    def getNewsFeed(self, userId: int) -> list[int]:
        pass

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follower_mapping[followeeId].append(followerId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follower_mapping[followeeId].remove(followerId)

actions=["Twitter","postTweet","getNewsFeed","follow","postTweet","getNewsFeed","unfollow","getNewsFeed"]
values=[[],[1,5],[1],[1,2],[2,6],[1],[1,2],[1]]

for i in range(len(actions)):
    action=actions[i]
    value=values[i]
    if action=="Twitter":
        t=Twitter()
    elif action=="postTweet":
        t.postTweet(*value)
        print("Post Mapping = ",t.post_mapping)
    elif action=="getNewsFeed":
        pass
    elif action=="follow":
        t.follow(*value)
        print("Follower Mapping = ",t.follower_mapping)
    elif action=="unfollow":
        t.unfollow(*value)
        print(t.follower_mapping)