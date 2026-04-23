class LRUCache:
    class Node:
        def __init__(self,key : int,val : int):
            self.key=key
            self.val=val
            self.prev=None
            self.next=None

    def __init__(self, capacity: int):
        self.map={}
        self.capacity=capacity
        self.head=None
        self.tail=None

    def get(self, key: int) -> int:
        if key not in self.map.keys():
            return -1
        else:
            #print("Get, Before : ",key,self.head.val,self.tail.val)
            node=self.map[key]
            if node==self.head or self.head==self.tail:
                return node.val
            elif node==self.tail:
                node.prev.next=None
                self.tail=node.prev
            else:
                node.prev.next=node.next
                node.next.prev=node.prev
            node.next=self.head
            node.prev=None
            self.head.prev=node
            self.head=node
            #print("Get, After : ",key,self.head.val,self.tail.val)
            return self.head.val


    def put(self, key: int, value: int) -> None:
        print("Length = ",len(self.map))
        if len(self.map)==0:
            self.map[key]=self.head=self.tail=self.Node(key,value)            
        elif len(self.map)<self.capacity:
            print("Put, Before : ",key,self.head.val,self.tail.val)
            if key in self.map.keys():
                node=self.map[key]
                node.val=value
                if node==self.head or self.head==self.tail:
                    return
                elif node==self.tail:
                    node.prev.next=None
                    self.tail=node.prev
                else:
                    node.prev.next=node.next
                    node.next.prev=node.prev
                node.next=self.head
                node.prev=None
                self.head.prev=node
                self.head=node
            else:
                node=self.Node(key,value)
                node.next=self.head
                self.head.prev=node
                self.head=node
                self.map[key]=node
            print("Put, After : ",key,self.head.val,self.tail.val)
        else:
            print("Put FUll, Before : ",key,self.head.val,self.tail.val)
            if key in self.map.keys():
                node=self.map[key]
                node.val=value
                if node==self.head or self.head==self.tail:
                    return
                elif node==self.tail:
                    node.prev.next=None
                    self.tail=node.prev
                else:
                    node.prev.next=node.next
                    node.next.prev=node.prev
                node.next=self.head
                node.prev=None
                self.head.prev=node
                self.head=node
            else:
                node=self.Node(key,value)
                node.next=self.head
                self.head.prev=node
                self.head=node
                self.tail.prev.next=None
                self.map.pop(self.tail.key)
                self.tail=self.tail.prev
                self.map[key]=node
            print("Put, After : ",key,self.head.val,self.tail.val)
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)