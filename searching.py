def linearSearch(iterable,key):
    """Simple liner search"""
    ops = 0
    for i in range(len(iterable)):
        if key == iterable[i]:
            print("Key found at index",i)
            print(ops,"operations")
            return i
        ops += 1
    else:
        print("Search for {} unsuccessful".format(key))
        print(ops,"operations")
        return None

def binarySearch(iterable,key):
    """Binary search that checks middle values,
    changes search domain accordingly"""
    mid = len(iterable)//2
    high = len(iterable)
    low = 0
    ops = 0
    while mid > low:
        if iterable[mid] == key: # key happens to be middle element
            print("Key found at index",mid)
            print(ops, "operations")
            return mid
        elif iterable[mid] > key: # key must be in first half
            high = mid
            mid = (low+high)//2
        else: # key must be in second half
            low = mid
            mid = (low+high)//2
        ops += 1
    else:
        print("Search for {} unsuccessful".format(key))
        print(ops,"operations")

def genHash(lst):
    """Creates a hash table"""
    print("creating hash")
    n = len(lst)+5
    hash_table = [None]*n # initialises a hash table
    for j in lst: # assigns to table
        i = j%n
        if type(hash_table[i]) != list and hash_table[i] == None:
            hash_table[i] = j
        elif type(hash_table[i]) != list and hash_table[i] != None:
            hash_table[i] = [hash_table[i],j]
        else:
            hash_table[i].append(j)
    return hash_table

def hashSearch(hash_table,key):
    n = len(hash_table)
    x = hash_table[key%n]
    if type(x) == list:
        if key in x:
            print("Search successful")
            print("Key found at",key%n+1)
            return
    else:
        if x == key:
            print("Search successful")
            print("Key found at",key%+1)
            return
    print("Search for {} unsuccessful".format(key))

def compareSearches():
    lst = list(range(9000000))
    nums = [1,8999999,-1,8999999//2]
    functs = [linearSearch,binarySearch,hashSearch]
    hash_table = genHash(lst)
    for i in nums:
        for j in functs:
            print(j)
            j(lst*(j!=hashSearch)+hash_table*(j==hashSearch),i)
            print()

if __name__ == "__main__":
    compareSearches()