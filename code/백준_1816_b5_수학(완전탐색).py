
tc = int(input())

for j in range(tc):
    number = int(input())

    for i in range(2,1000001):
        if number % i == 0:
            print("NO")
            break

        if i == 1000000:
            print("YES")