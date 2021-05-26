a, m, d, n = map(int, input().split())
a = int(a)  # 시작 값
m = int(m)  # 곱할 값
d = int(d)  # 더할 값
n = int(n)  # 몇 번째

answer = 0
if n-1 == 0:
    print(n)
else:
    for i in range(n-1):
        answer = a * m + d
        a = answer
    print(answer)