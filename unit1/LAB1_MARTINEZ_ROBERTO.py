#A
grades=[80,90,70]
average=sum(grades)/len(grades)
print(average)
#B
def calculate_average(data):
    return sum(data)/len(data)
grades=[80,90,70]
print(calculate_average(grades))
#C
numbers=[1,2,3,4,5]
squares=list(map(lambda x: x**2,numbers))
print(squares)
#C With my modification
numbers=[3,90,23,1,7]
squares=list(map(lambda x: x**2,numbers))
print(squares)
