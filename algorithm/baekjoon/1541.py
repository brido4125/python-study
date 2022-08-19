str = input()

numbers = []
opers = []

target = ''
# 숫자와 문자 분리 작업
for elem in str:
    if elem != '+' and elem != '-':
        target = target + elem
    else:
        numbers.append(int(target))
        target = ''
        opers.append(elem)

# 마지막 숫자 추가
numbers.append(int(target))

for i in range(len(opers)):
    if opers[i] == '-':
        minus_index = i + 1
        break

answer = 0

for i in range(len(numbers)):
    try:
        if i >= minus_index:
            answer -= numbers[i]
        else:
            answer += numbers[i]
    except NameError:
        answer += numbers[i]

print(answer)
