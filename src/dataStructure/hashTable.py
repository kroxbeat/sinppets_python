from typing import *

class Node:
    def __init__(self,key: str,value: str) -> None:
        self.key: str = key
        self.value: str = value

    def setValue(self,value: str) -> None:
        self.value = value

    def getValue(self) -> str:
        return self.value

    def getKey(self) -> str:
        return self.key

class HashTable:
    def __init__(self,size: int) -> None:
        self.data = [None for i in range(size)]

    @staticmethod
    def makeHashCode(key: str) -> int:
        countSum: int = 0
        for char in list(key):
            countSum += ord(char)
        return countSum

    def findIndex(self,hashCode: int) -> int:
        return hashCode % len(self.data)

    @staticmethod
    def searhNodeInList(list: List, key: str) -> List:
        if list is None or len(list) == 0:
            return None
        for node in list:
            if node.getKey() == key:
                return node
        return Node

    def put(self,key: str,value: str) -> None:
        hashcode = self.makeHashCode(key)
        index = self.findIndex(hashcode)
        list: List = self.data[index]
        if list is None:
            list = []
            self.data[index] = list
        node = self.searhNodeInList(list, key)
        if node is None:
            list.append(Node(key,value))
        else:
            node.setValue(value)


    def get(self,key: str) -> str:
        hashcode = self.makeHashCode(key)
        index = self.findIndex(hashcode)
        list: List = self.data[index]
        node = self.searhNodeInList(list, key)
        if node is None:
            return "Not Found"
        else:
            return node.getValue()



