n = int(input())    # 번호를 부른 횟수
k = input().split() # 부른 번호들

k.reverse()

for i in range(n):
    print(k[i], end=" ")