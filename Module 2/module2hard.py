# n = int(input())
# pwd = []
# for i in range(1, n):
#     for j in range(i, n):
#         if n % (i+j) == 0:
#             pwd.append(str(i))
#             pwd.append(str(j))
# print(''.join(pwd))
n = int(input())
pwd = [str(k) for i in range(1, n) for j in range(i, n) if n % (i+j) == 0 for k in (i, j)]
print(''.join(pwd))