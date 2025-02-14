from utile import pr
import random
    
#01
def fn01 (x:int, y: str) -> int:
    li = ['a', 'b', 'c', 'd', 'e', 'f']
    for i in li:
        pr(i)
    pr(len(li))

#02
def add (x:list, y:list) -> int:
    return x + y

list01 = li = ['a', 'b', 'c', 'd', 'e', 'f']
list02 = ['1', '2', '3', '4', '5']

pr(add(list01, list02))


#03
def insert (x:list, y: str) -> int:
    return x.insert(1, y)


pr(insert(list01, 'hihao'))