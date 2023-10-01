n = int(input())
arr = sorted(list(map(int,input().split())))
m = int(input())
card = list(map(int,input().split()))

for number in card:

    s = 0
    e = n-1
    check = False
    while s <= e:
        mid = (s+e) //2
        if arr[mid] == number:
            check = True
            break
        elif arr[mid] > number:
            e = mid - 1

        else:
            s = mid + 1

    if check == True:
        print(1, end = " ")
    else:
        print(0, end = " ")
