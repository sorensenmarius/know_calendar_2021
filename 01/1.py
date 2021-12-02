f = open('tall.txt', 'r', encoding="utf-8")
number = f.readline()
norwegianNumbers = ['en', 'to', 'tre', 'fire', 'fem', 'seks', 'sju', 'åtte', 'ni', 'ti', 
                    'elleve', 'tolv', 'tretten', 'fjorten', 'femten', 'seksten', 'sytten', 'atten', 'nitten', 
                    ('tjue', 20), ('tretti', 30), ('førti', 40), ('femti', 50)]

sum = 0
for num in norwegianNumbers[::-1]:
    n, val = (num[0], num[1]) if type(num) == tuple else (num, norwegianNumbers.index(num) + 1)
    count = number.count(n)
    sum += count * val
    number = number.replace(n, "")
print(sum)