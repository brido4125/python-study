import sys

N = int(input())
dic = dict()  # Dictionary 선언
for _ in range(N):
    book_title = sys.stdin.readline()
    if book_title not in dic:
        dic[book_title] = 1
    else:
        dic[book_title] += 1;

max_value = -1
for v in dic.values():
    if max_value < v:
        max_value = v;

# dictionary에서 value로 key 값 찾기
answer_list = []
for key, value in dic.items():
    if value == max_value:
        answer_list.append(key)

if len(answer_list) == 1:
    print(answer_list[0])
else:
    answer_list.sort()
    print(answer_list[0])
