print("Agosta\n Awais\n "*5)
student_count = 1000
is_published = False
course = "Python Programming"
print(student_count)
print(course[0])
print(course[-1])
print(course[0:5])


def myFunction(*numbers):
    # print(numbers)
     total = 1
     for i in numbers:
          total *= i
     return total
print("Hello world")
print(myFunction(2,3,4,5,6))


def fizz_buzz(input):
     if (input % 3 ==0) and (input % 5 ==0):
          return "fizz_buzz"
     if input % 3==0:
          return "fizz"
     if input % 5 == 0:
          return "buzz"
     else:
          return input

result = fizz_buzz(7)
print(result)


numbers = list(range(20))
print( numbers[::-1])

items =[
     ("Product1", 10),
     ("Product2", 9),
     ("Product3", 12),
]

maped = list(map(lambda item: item[1], items))

# print(maped)

filtered = list(filter(lambda item:item[1]<=10, items))
# print(filtered)


from collections import deque
# Collections is module and deque is a class .
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.popleft()
# print(queue)


x=20
y=4

# x=x+y  #x=24,   y = 20 , x=4 
# y=x-y
# x=x-y

(x,y) = (y,x)
# print("X = ",x)
# print("Y = ",y)


from timeit import timeit
from pprint import pprint

sentence = "This is a common interview question"
char_frequency ={}
for char in sentence:
     if char in char_frequency:
          char_frequency[char]+=1
     else:
          char_frequency[char]=1

char_frequency_sorted =sorted(
     char_frequency.items(), 
     key=lambda keyValue : keyValue[1],
     reverse=True)     
# print(char_frequency_sorted[0])
# pprint(char_frequency)

numbers=[2,3]
print(numbers[3])
code = """
def cal(age):
     if age<=0:
          return None
     return 10/age


x=cal(-1)
if x == None:
     pass  
"""
 # Pass is a statement that doesn't do anything
print("First Code= ",timeit(code, number=100))