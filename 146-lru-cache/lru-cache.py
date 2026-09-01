class LRUCache:
    class Node:
        def __init__(self,key=None,val=None):
            self.key=key
            self.val=val
            self.prev=None
            self.next=None

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache={}
        #dummmy nodes
        self.head=self.Node()
        self.tail=self.Node()
        self.head.next=self.tail
        self.tail.prev=self.head
    def remove(self,node):
        node.prev.next=node.next
        node.next.prev=node.prev
    def insert(self,node):
        prev=self.tail.prev
        node.next=self.tail
        node.prev=prev
        prev.next=node
        self.tail.prev=node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node=self.cache[key]
        self.remove(node)
        self.insert(node)
        return node.val
        
    def put(self, key: int, value: int) -> None:
        if key  in self.cache:
            self.cache[key].val=value
            node=self.cache[key]
            self.remove(node)
            self.insert(node)
            return
        self.cache[key]=self.Node(key,value)
        self.insert(self.cache[key])
        if len(self.cache)>self.capacity:
            node=self.head.next
            self.remove(node)
            del self.cache[node.key]
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)