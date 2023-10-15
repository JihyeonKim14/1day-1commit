def solution(phone_number):
    last4 = phone_number[-4:]
    front = len(phone_number[:-4]) * '*'
    answer = front + last4
    return answer