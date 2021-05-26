n = int(input())    # 바둑판에 올려 놓을 흰 돌의 개수
k = []  # 바둑판 생성을 위한 변수 선언

# 빈 바둑판 생성
for i in range(20):
    k.append([])
    for j in range(20):
        k[i].append(0)

# 바둑돌이 올라갈 자리
for i in range(n):
    x, y = input().split()
    k[int(x)][int(y)] = 1

# 바둑돌이 올라간 자리 출력
for i in range(1, 20):
    for j in range(1, 20):
        print(k[i][j], end=" ")
    print()