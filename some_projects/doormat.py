num = input().split()
neck = list(map(int,num))
n = neck[0]
m = neck[1]
c = '.|.'

for i in range(n//2):
    print((c*i).rjust(m//2,'-') + c + (c*i).ljust(m//2,'-'))
print('WELCOME'.center(2*m//2 + 2,'-'))
for i in range(n//2):
    print((c*(n//2-1-i)).rjust(m//2,'-') + c + (c*(n//2-1-i)).ljust(m//2,'-'))

