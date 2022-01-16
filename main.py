from src.dataStructure.hashTable import HashTable,Node


def _main():
    h = HashTable(4)
    h.put("kang","kang message")
    h.put("jung","jung name")
    h.put("kang","dubble message")

    print(h.get("jung"))
    print(h.get("kang"))
    print(h.get("kang2"))

    for index in range(len(h.data)):
        for l in h.data[index]:
            print(l)

if __name__ == '__main__':
    _main()

