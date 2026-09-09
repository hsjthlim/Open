# %%
coordinates = (10,20)
x,y = coordinates
print(f'X좌표: {x}, y좌표: {y}')
# %%

rgb = [255, 128, 0]
r,g,b = rgb
print(f'빨강: {r}, 초록: {g}, 파랑: {b}')
# %%
word = "ABC"
w1, w2, w3 = word
print(f'알파벳의 첫번째 글짜는 {w1}, 두번째 글자는 {w2}, 세번째 글자는 {w3} 입니다')

# %%
def get_dataset_stats(values):
    return min(values), max(values), sum(values)/len(values)

data = [12, 8, 21, 17, 5]

min, max, avg = get_dataset_stats(data)
print(f'이 리스트의 최소값은 {min}, 최대값은 {max}, 평균은 {avg} 입니다')
# %%

students_scores = [
    ("김철수", 85, 92, 78),
    ("이영희", 92, 88, 95),
    ("박지민", 75, 83, 90)
]



for s in students_scores:
    name, db, py, cl = s
    print(f'{name} 학생의 평균 점수는 {(db+py+cl)/3:.2f} 입니다')
# %%
monthly_sales = [1200, 1350, 1420, 1500, 1300, 1580, 1620, 1700, 1800, 1850, 1900, 2000]

first, second, *last  = monthly_sales
print(f'1월 판매액은 {first}, 2월 판매액은 {second}, 나머지 기간 판매액은 {sum(last)}')
# %%

