__author__ = 'butterfly'

class SortMap:
    def __init__(self,capacity):
        self.dict = dict()
        self.sortedList = list()
        self.capacity = capacity
        self.size = 0
    def get(self,key):
        return self.dict.get(key)

    def removeLeastUsed(self):
        ans = None
        min = int(1<<31)
        for (key,value) in self.dict.items():
            num = value[1]
            if num < min:
                min = num
                ans = key
        #if ans != None:
        result = self.dict.pop(ans,None)
        if result != None:
            self.size = self.size - 1
    #log(n)
    def insert(self,key,value,level):
        return
    #log(n)
    def update(self,key,value,level):
        return
    #o(1)
    def removeFromList(self,key,value,level):
        return
    def insertItem(self,key,value):
        value1 = self.dict.get(key)
        if self.size < self.capacity and value1 == None:
            self.dict[key] = [value,1]
            self.levelMap
            self.size = self.size + 1
            return
        elif self.size < self.capacity:
            self.dict[key] = [value1[0],value1[1]+1]
            return
        else:
            self.removeLeastUsed()
            self.dict[key] = [value1[0],value1[1] + 1]

class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.sortMap = SortMap(capacity)


    # @return an integer
    def get(self, key):
        value = self.sortMap.get(key)
        if value == None:
            return -1
        return value

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        self.sortMap.insertItem(key,value)