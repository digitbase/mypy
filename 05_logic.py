from utile import pr
import random
    

def testif (x:int, y: str) -> int:
    n1 = 0
    n2 = 0
    n3 = 0
    for i in range(0,x):
        a = random.randint(0,2)
        if a >1 :
            n1 += 1
        elif a < 1 :
            n2 += 1
        else :
            n3 += 1
    
    return  [n1,n2,n3]

a = testif(x=100, y='ni hao')
print(type(a))
pr(a)

numbers = [1, 3, 7, 2, 8, 5]
target = 8
index = 0
while index < len(numbers):
    if numbers[index] == target:
        print(f"找到了目标元素 {target}，索引是 {index}")
        break
    index += 1
else:
    print("没有找到目标元素")

