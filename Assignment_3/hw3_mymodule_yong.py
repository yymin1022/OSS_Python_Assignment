# hw3_mymodule_yong.py
#
# 핵심 주의사항:
#     - import문, print() 호출식, input() 호출식이 들어 있으면 '무조건' 0점으로 간주돼요.
#       특히 import문을 적을 수 없다는 점을 꼭 유의해 주세요.
#
#     - Python interpreter, 운영체제, 컴퓨터를 공격하려는 '명백한' 시도가 발견되면 0점이 되고 강사의 전화 연락을 받게 될 거예요.
#
#     - 능력치가 같은 캐릭터들은 반드시 '이웃 순위'에 위치하도록 만들어야 해요.
#       (3등, 5등이 능력치가 같은데 사이에 낀 4등이 다르거나 하면 안 돼요)
#       능력치가 같을 때만 이름을 고려하도록 실행 흐름을 구성하면 이 규칙은 걱정 안 해도 돼요.
#
#     - 이번 과제는 제출 가능! 메시지를 보는 것이 좀 어려울 수 있어요. 미리 종이에 적거나 그려 가며 생각해 보고 오는 것을 권장해요.
#       그렇게 해도 몇몇 국면에서는 실패를 겪을 수밖에 없도록 강사가 의도해 놨는데,
#       그 때 미리 적어 둔 종이 내용이 없다면 자칫 전체 코드를 다 다시 짜는 불상사가 생길 수 있어요.
#       (강사도 core 모듈 내용 적을 때 종이에 노트해 가며 진행했어요. 이건 스킬이지 부끄러운 일이 아니에요)


def duel(left, right):
    powerLeft = left[1] * 100000 + left[2] * 10000 + left[3] * 1000 + left[4] * 100 + left[5] * 10 + left[6]
    powerRight = right[1] * 100000 + right[2] * 10000 + right[3] * 1000 + right[4] * 100 + right[5] * 10 + right[6]

    if powerLeft != powerRight:
        return -1 if powerLeft > powerRight else 1
    if left[0] == "Dev. LR":
        return -1
    if right[0] == "Dev. LR":
        return 1
    return -1 if left[0] < right[0] else 1