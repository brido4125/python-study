# 순서가 상관없다 => 조합 Combination
# 순서가 상관있다 => 순열 Permutation

from itertools import combinations

tall_list = []
# 일곱 난쟁이의 키의 합이 100, 순서에 상관없이 9명중 7명 선택해서 비교
for i in range(9):
    tall_list.append(int(input()))

answer = []

for nCr in combinations(tall_list,7):
    if sum(nCr) == 100:
        answer = list(nCr)
        break;

answer.sort()
for i in answer:
    print(i)
