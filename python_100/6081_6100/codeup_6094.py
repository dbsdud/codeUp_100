n = int(input())    # 번호를 부른 횟수
k = input().split() # 부른 번호들

for i in range(n):
    k[i] = int(k[i])

k.sort()
print(k[0])