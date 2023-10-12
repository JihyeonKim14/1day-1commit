def solution(absolutes, signs):
    answer = 0
    for num, bool_ in zip(absolutes, signs):
        if bool_ == True:
            num = num
        else:
            num = num * (-1)
        answer += num
    return answer