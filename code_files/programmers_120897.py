def solution(n):
result = []
for i in range(1, n+1): # 약수
if n % i == 0:
num = int(n / i) # 주어진 숫자가 1인경우 제외
if n == 1:
return [1] # 약수를 다 구한 경우
if i in result:
print(sorted(result))
return sorted(result) # [1, 3, 9] 인 경우
elif num == i:
result.append(num) # 다 못구한 경우 약수 리스트에 추가
else:
result.append(i)
result.append(num)
