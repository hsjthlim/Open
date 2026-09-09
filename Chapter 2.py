# %%
numbers = [10, 20, 30, 40, 50, 60, 70]
first_four = numbers[:4]
last_three = numbers[-3:]
print(first_four)
print(last_three)

every_odd_list = numbers[::2]
reverse_list = numbers[::-1]
print(every_odd_list)
print(reverse_list)


# %%
matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16],
]

first_two_row = matrix[0:2]
print(first_two_row)
first_two_columns = [a[0:2] for a in matrix]
print(first_two_columns)
# %%

numbers = []

for i in range(5):
    numbers.append(i)
print(numbers)
# %%

numbers_10 = [n for n in range(10)]
print(numbers_10)
# %%

squares=[]
squares = [s**2 for s in numbers_10]
print(squares)
# %%

numbers_1_10 = list(range(1,11))

even_numbers = []
even_numbers = [e for e in numbers_1_10 if e % 2 == 0]

print(even_numbers)
# %%

list1 = ["사과", "복숭아", "바나나"]
list2 = ["주스", "잼", "통조림"]

pairs = []

pairs = [ (fruit,product) for fruit in list1 for product in list2]
print(pairs)
# %%

squares = {}
squares = {i:i**2 for i in range(5)}
print(squares)

# %%
city_population = {
    '서울': 957, '부산': 339, '인천': 294, '대구': 242, '광주': 145, '대전': 147,
    '울산': 114, '세종': 36, '수원': 115, '창원': 103, '고양': 105, '용인': 108, '성남': 94
}

large_city = {city:pop for city,pop in city_population.items() if pop > 200}
print(large_city)
# %%

large_name_city = {city:pop for city, pop in city_population.items() if pop > 300 and "산" in city}
print(large_name_city)

# %%
name = "하시준"
age = 8
salary = 10**10
tax_rate = 0.1

basic_format = '이름:%s, 나이:%d, 월급:%d원' % (name, age, salary)
print(basic_format)


# %%
basic_format = f'우리 아기 이름은 {name}이고 나이는 {age}이고 월급은 무려 {salary:,}원이랍니다'
print(basic_format)
# %%

basic_format = '이름은 %s이고 나이는 %d이고 월급은 %d이고 실수령액은 %d 랍니다' % (name, age, salary, tax_rate*salary)
print(basic_format)
# %%

basic_format = ("이름은 {0}이고 나이는 {1}이고 월급은 {2}이고 실수령액은 무려 {3:,}입니다 헤헤".format(name, age, salary, (1-tax_rate)*salary))
print(basic_format)
# %%

file = open("output.txt","w")
file.write("Hello, world! Haha\n")
file.close()
# %%
with open("output.txt","w") as f:
    f.write("Hello, world! Hehe!\n")

# %%

import urllib.request
import ssl
import pandas as pd
from io import StringIO

# URL 연결 관리
context = ssl._create_unverified_context()
response = urllib.request.urlopen('https://raw.githubusercontent.com/jaehwachung/Data-Analysis-with-Open-Source/refs/heads/main/Chapter%203/students.csv', context=context)


data = response.read( ).decode('utf-8')


cc = pd.read_csv(StringIO(data))
df = pd.DataFrame(cc)
df = df.assign (오픈소스 = 100)
df = df.assign (총점 = (lambda x: (x["데이터베이스"]+x["파이썬"]+x["클라우드"]+x["오픈소스"])),
                평균 = (lambda y: y["총점"]/4))
df
# %%
