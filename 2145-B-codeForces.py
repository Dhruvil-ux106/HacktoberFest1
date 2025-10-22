t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input().strip()

    cnt0 = s.count('0')
    cnt1 = s.count('1')
    cnt2 = s.count('2')

    res = ['?'] * n

    for i in range(cnt0):
        res[i] = '-'
    for i in range(n - cnt1, n):
        res[i] = '-'
    for i in range(cnt0 + cnt2, n - cnt1 - cnt2):
        res[i] = '+'

    print(''.join(res))
