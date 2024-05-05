# hw3_core.py
#
# 과제#3의 제출 전 테스트, 제출 후 최종 프로그램 제작에 사용할 코어 모듈입니다.
# core 모듈에만 적혀 있는 내용은 시험에 절대 안 나오니 이 파일 아래에 적혀 있는 코드는 하나도 안 읽어도 돼요.
#
# 주의: 여러분의 모듈을 import하기 위한 부분을 제외하면 이 파일의 내용은 여러분이 절대로 고치면 안 돼요!



# --------------------------------------------------------
# 여러분의 모듈을 import하기 위한 부분
#

# TODO#3: 방금 바꾼 파일 이름을 아래의 hw3_mymodule 자리에 바꾸어 적어 주세요.
#         TODO#4는 여기서 약 20줄 아래에 적혀 있어요.

import hw3_mymodule_yong

modules = [hw3_mymodule]







# --------------------------------------------------------
# 주의: 이 아래 내용은 절대로 고치면 안 돼요!



# 여기에는 여러분이 과제#2에서 제출했던 '내 캐릭터' 정보들이 담겨 있어요.
# 주: 여기 적혀 있는 순서는 최종 결투에 전혀 영향을 주지 않으니 걱정 안 해도 돼요.
#
# TODO#4: 내 캐릭터가 싸우게 될 상대방들이 대강 어떻게 생겨먹었나 구경해 보면서
#         혹시 내 캐릭터 이름이 바뀌지는 않았나도 확인해 보세요.
#         (오늘 이전에 제출하지 않은 친구들 자리는 강사가 임의로 이름과 능력치를 정해 채워 두었어요)
#         TODO#5는 옆 파일의, 함수 duel()에 대한 함수 정의 안에 적혀 있어요.
stats = [
    ['\x00', 90, 5, 2, 2, 1, 0],
    ['\x01', 14, 15, 16, 17, 18, 20],
    [' ', 0, 20, 20, 20, 20, 20],
    ['!!', 16, 16, 17, 17, 17, 17],
    ['!14', 0, 0, 0, 0, 0, 100],
    ['!61', 20, 20, 20, 20, 20, 0],
    ['100벌고 싶은 문현승', 100, 0, 0, 0, 0, 0],
    ['4의악마', 8, 12, 16, 20, 20, 24],
    ['A16', 40, 40, 40, 40, 40, -100],
    ['A36', 0, 0, 0, 0, 0, 100],
    ['A53', 50, 50, 0, 0, 0, 0],
    ['A97', 100, 0, 0, 0, 0, 0],
    ['AAA', 0, 100, 0, 0, 0, 0],
    ['ABC', 100, 0, 0, 0, 0, 0],
    ['A_Hero', 20, 20, 20, 20, 10, 10],
    ['A_ljw', 40, 60, 0, 0, 0, 0],
    ['Aaa', 5, 15, 5, 25, 30, 20],
    ['Aaaz', 100, 0, 0, 0, 0, 0],
    ['Aceline', 10, 20, 15, 25, 10, 20],
    ['Acter', 17, 18, 15, 20, 15, 15],
    ['AiSKdud', 5, 5, 20, 20, 30, 20],
    ['Alex', 1, 1, 3, 5, 10, 80],
    ['Amy', 15, 37, 3, 17, 18, 10],
    ['Anonymous', 0, 0, 0, 100, 0, 0],
    ['Antitled', 10, 20, 10, 10, 20, 30],
    ['B', 35, 35, 5, 5, 5, 15],
    ['Bada', 10, 20, 5, 10, 15, 40],
    ['Blitz', 0, 30, 40, 0, 0, 30],
    ['BoSeok', 95, 1, 1, 1, 1, 1],
    ['Boho', 10, 15, 30, 20, 20, 5],
    ['CHO', 50, 30, 10, 5, 4, 1],
    ['ChaeChae', 10, 25, 15, 10, 25, 15],
    ['Chocol', 20, 30, 0, 25, 10, 15],
    ['Choi', 10, 20, 15, 30, 25, 0],
    ['Chungy', 10, 20, 10, 10, 10, 40],
    ['CutiYoshi', 20, 20, 20, 10, 10, 20],
    ['CutiePPOJJAKK', 16, 8, 20, 14, 10, 32],
    ['DT', 15, 5, 15, 30, 17, 18],
    ['DUK', 15, 15, 15, 15, 25, 15],
    ['Dallae', 17, 17, 17, 16, 16, 17],
    ['Denise', 30, 20, 10, 20, 10, 10],
    ['Dev. LR', 100, 0, 0, 0, 0, 0],
    ['Dohyeon', 5, 20, 15, 20, 20, 20],
    ['Dorang', 100, 0, 0, 0, 0, 0],
    ['FIRE', 15, 10, 10, 20, 20, 25],
    ['FULLSUN', 10, 15, 20, 0, 20, 35],
    ['GAM3 BO1', 20, 30, 30, 10, 5, 5],
    ['Gallant', 17, 17, 17, 17, 16, 16],
    ['Got_Charming_Appearance_so_She_can_Capivate_anyone_and_it_is_her_weapon_Univeversity_Woman', 0, 0, 0, 0, 0, 100],
    ['Helen', 10, 35, 5, 15, 20, 15],
    ['Helios', 0, 0, 0, 0, 0, 100],
    ['Hero', 16, 17, 17, 16, 17, 17],
    ['Hero_name', 15, 19, 17, 15, 16, 18],
    ['HopER', 30, 35, 10, 10, 10, 5],
    ['IDLE', 0, 0, 0, 0, 0, 100],
    ['IceCreamWarrior', 0, 100, 0, 0, 0, 0],
    ['ImTheMain', 95, 1, 1, 1, 1, 1],
    ['Iris', 0, 0, 0, 0, 100, 0],
    ['JEN', 0, 0, 0, 0, 0, 100],
    ['JIS', 30, 20, 10, 30, 5, 5],
    ['JIYO', 0, 0, 0, 0, 0, 100],
    ['JJ75', 100, 0, 0, 0, 0, 0],
    ['JJ76', 10, 20, 20, 20, 15, 15],
    ['JOONG', 20, 20, 20, 10, 15, 15],
    ['Jay', 15, 10, 5, 30, 10, 30],
    ['Jimmy', 10, 50, 10, 10, 10, 10],
    ['JuJu', 0, 100, 0, 0, 0, 0],
    ['Justry', 0, 21, 21, 16, 11, 31],
    ['King', 20, 20, 20, 20, 10, 10],
    ['King_20241383', 100, 0, 0, 0, 0, 0],
    ['Lee_Unha', 10, 20, 30, 35, 0, 5],
    ['LimeTree', 1300, 1000, 700, 400, 100, -3400],
    ['Lucy', 16, 17, 17, 16, 17, 17],
    ['ME', 10, 30, 5, 25, 25, 5],
    ['MIN', 40, 30, 5, 5, 10, 10],
    ['Mickey', 0, 0, 0, 0, 0, 100],
    ['Minnnn', 20, 20, 20, 20, 10, 10],
    ['Minsiki2', 0, 0, 0, 0, 0, 100],
    ['Munchicken', 0, 0, 0, 100, 0, 0],
    ['MyCharacter', 20, 20, 20, 10, 10, 20],
    ['NKYJ', 17, 17, 17, 17, 16, 16],
    ['Na', 5, 10, 15, 30, 30, 10],
    ['NaJjangSsem', 7, 15, 13, 25, 15, 25],
    ['Newjeans_Hanni', 0, 0, 0, 0, 0, 100],
    ['OJW', 15, 10, 5, 20, 0, 50],
    ['Orlando', 50, 15, 20, 0, 10, 5],
    ['PUANG', 30, 20, 15, 5, 20, 10],
    ['Pjh', 1, 54, 20, 15, 3, 7],
    ['Player', 55, 5, 10, 10, 10, 10],
    ['PythonChobo', 100, 0, 0, 0, 0, 0],
    ['RKJ', 0, 100, 0, 0, 0, 0],
    ['RV', 15, 25, 5, 15, 35, 5],
    ['Racin', 17, 17, 17, 16, 16, 17],
    ['ReSinon', 20, 10, 20, 10, 20, 20],
    ['Retr0', 0, 0, 100, 0, 0, 0],
    ['Rimyu', 0, 100, 0, 0, 0, 0],
    ['Rom', 100, 0, 0, 0, 0, 0],
    ['Ronaldo', 100, 0, 0, 0, 0, 0],
    ['Rullu', 0, 25, 50, 25, 0, 0],
    ['STR_ALL_IN', 100, 0, 0, 0, 0, 0],
    ['SangYunLee', 10, 20, 20, 20, 20, 10],
    ['Seol', 16, 16, 17, 17, 17, 17],
    ['Song', 0, 100, 0, 0, 0, 0],
    ['Sundo', 2, 2, 2, 2, 90, 2],
    ['Sunny', 10, 20, 30, 10, 20, 10],
    ['THIISISME', 15, 15, 20, 15, 15, 20],
    ['TastyPotato245', 100, 0, 0, 0, 0, 0],
    ['Titled', 100, 0, 0, 0, 0, 0],
    ['TwoS', 100, 0, 0, 0, 0, 0],
    ['Untitled00', 17, 18, 15, 17, 16, 17],
    ['Untitled01', 0, 100, 0, 0, 0, 0],
    ['Untitled03', 0, 100, 0, 0, 0, 0],
    ['Untitled21', 0, 100, 0, 0, 0, 0],
    ['Untitled47', 2, 98, 0, 0, 0, 0],
    ['Untitled61', 0, 100, 0, 0, 0, 0],
    ['Untitled69', 0, 100, 0, 0, 0, 0],
    ['Untitled81', 0, 100, 0, 0, 0, 0],
    ['WOW', 100, 0, 0, 0, 0, 0],
    ['Warrior', 30, 20, 26, 10, 10, 4],
    ['WiJi', 3, 3, 5, 5, 80, 4],
    ['Willy', 5, 10, 0, 50, 30, 5],
    ['Winner', 0, 0, 0, 0, 1, 99],
    ['YD', 40, 10, 25, 15, 5, 5],
    ['YU', 10, 10, 10, 30, 30, 10],
    ['Yamin', 31, 4, 9, 18, 16, 22],
    ['Yeri', 10, 30, 5, 15, 35, 5],
    ['Yoonis', 10, 20, 30, 10, 20, 10],
    ['Young', 20, 10, 5, 15, 35, 15],
    ['YoungQ', 50, 50, 0, 0, 0, 0],
    ['Yunbin', 100, 0, 0, 0, 0, 0],
    ['Yunsung', 30, 10, 10, 20, 20, 10],
    ['ZZZZZZ', 30, 25, 20, 15, 10, 0],
    ['Zamhee', 5, 0, 10, 0, 35, 50],
    ['Zo', 16, 17, 16, 17, 17, 17],
    ['a07', 100, 0, 0, 0, 0, 0],
    ['a81', 72, 2, 3, 5, 7, 11],
    ['aaa', 1, 1, 1, 1, 1, 95],
    ['abc', 20, 15, 25, 10, 15, 15],
    ['ace', 0, 0, 0, 0, 0, 100],
    ['alwaysWin', 95, 1, 1, 1, 1, 1],
    ['asdf1234', 20, 30, 15, 15, 10, 10],
    ['bdk', 0, 0, 0, 0, 0, 100],
    ['bean', 17, 17, 17, 17, 16, 16],
    ['cando', 10, 10, 10, 10, 10, 50],
    ['chan', 45, 45, 0, 0, 5, 5],
    ['chanchen', 15, 30, 20, 10, 10, 15],
    ['cheolsu', 30, 50, 10, 5, 5, 0],
    ['chlrlals', 10, 15, 10, 40, 15, 10],
    ['choi', 30, 30, 10, 10, 10, 10],
    ['clenbier', 1, 95, 1, 1, 1, 1],
    ['coals', 10, 30, 5, 15, 35, 5],
    ['cookiz', 100, 0, 0, 0, 0, 0],
    ['dahee', 10, 20, 10, 25, 15, 20],
    ['daniel', 17, 17, 17, 17, 17, 15],
    ['dhld', 1, 1, 1, 1, 1, 95],
    ['dlwldnjs', 100, 0, 0, 0, 0, 0],
    ['doodoo', 0, 100, 0, 0, 0, 0],
    ['duck', 100, 0, 0, 0, 0, 0],
    ['duduzi', 5, 10, 15, 20, 20, 30],
    ['eunji', 20, 20, 20, 20, 10, 10],
    ['ewha', 10, 10, 25, 20, 10, 25],
    ['flyingcorgi', 0, 0, 0, 0, 0, 100],
    ['garden', 100, 0, 0, 0, 0, 0],
    ['gunwoo', 5, 5, 10, 10, 35, 35],
    ['gyurie', 20, 20, 20, 15, 15, 10],
    ['gyuriyo', 30, 25, 10, 15, 10, 10],
    ['gyuwon', 15, 15, 15, 15, 15, 25],
    ['halim', 10, 10, 20, 20, 20, 20],
    ['halland', 25, 30, 15, 10, 15, 5],
    ['harin', 10, 10, 10, 10, 10, 50],
    ['hmm', 30, 0, 10, 30, 0, 30],
    ['hodong', 30, 10, 25, 5, 27, 3],
    ['hpp', 35, 20, 9, 21, 5, 10],
    ['huey', 100, 0, 0, 0, 0, 0],
    ['hw2_jjeong', 5, 25, 30, 15, 5, 20],
    ['hyeyoon', 25, 20, 20, 15, 10, 10],
    ['hyorin', 20, 20, 5, 5, 30, 20],
    ['hyun', 30, 20, 15, 15, 10, 10],
    ['iGeonHo', 1, 1, 1, 95, 1, 1],
    ['insang', 100, 0, 0, 0, 0, 0],
    ['integralPark', 314159, 897932, 26535, -897932, -314159, -26435],
    ['jaemin', 100, 0, 0, 0, 0, 0],
    ['junn', 15, 5, 30, 10, 25, 15],
    ['king', 16, 16, 16, 16, 16, 20],
    ['kpt', 30, 20, 17, 13, 11, 9],
    ['lee', 100, 0, 0, 0, 0, 0],
    ['leeSSol', 0, 0, 98, 1, 0, 1],
    ['machaksa', 100, 0, 0, 0, 0, 0],
    ['marin', 10, 20, 30, 20, 10, 10],
    ['me', 20, 20, 20, 20, 15, 5],
    ['min', 0, 0, 0, 100, 0, 0],
    ['minho', 20, 20, 20, 10, 10, 20],
    ['minjun', 100, 0, 0, 0, 0, 0],
    ['minyeong', 30, 27, 10, 10, 20, 3],
    ['mkim', 30, 20, 20, 15, 5, 10],
    ['mldljyh', 100, 0, 0, 0, 0, 0],
    ['monkey', 15, 5, 10, 30, 5, 35],
    ['myang', 99, 1, 0, 0, 0, 0],
    ['myhomework', 15, 30, 5, 20, 9, 21],
    ['nayeonkim', 10, 10, 30, 10, 10, 30],
    ['nine', 10, 20, 15, 30, 20, 5],
    ['park', 100, 0, 0, 0, 0, 0],
    ['paryeomi', 0, 0, 0, 0, 0, 100],
    ['pikachu', 10, 15, 20, 25, 30, 0],
    ['pilgi_min', 0, 0, 0, 0, 0, 100],
    ['pineapple', 9, 9, 9, 9, 19, 45],
    ['potato', 20, 20, 15, 15, 15, 15],
    ['s', 100, 0, 0, 0, 0, 0],
    ['sebin', 20, 30, 20, 10, 10, 10],
    ['sehwan', 0, 0, 0, 0, 0, 100],
    ['seob', 40, 25, 15, 10, 5, 5],
    ['shawnnie', 10, 30, 5, 15, 35, 5],
    ['shin', -3, 0, -90, -512, -1024, 1729],
    ['smile', 0, 100, 0, 0, 0, 0],
    ['soyul', 0, 0, 0, 0, 0, 100],
    ['steven', 0, 0, 0, 0, 0, 100],
    ['sulgy', 0, 0, 0, 0, 0, 100],
    ['sun', 15, 15, 15, 25, 15, 15],
    ['suzzang', 0, 0, 0, 20, 30, 50],
    ['swim', 15, 10, 15, 20, 20, 20],
    ['uzin', 20, 20, 10, 20, 20, 10],
    ['watchlover', 0, 0, 0, 0, 1, 99],
    ['wgw', 15, 20, 20, 45, 0, 0],
    ['won', 10, 15, 20, 30, 10, 15],
    ['woochan', 0, 7, 3, 5, 15, 70],
    ['xxdura', 10, 20, 35, 10, 20, 5],
    ['yeji', 16, 16, 17, 17, 17, 17],
    ['yejin', 99, 1, 0, 0, 0, 0],
    ['yellow', 0, 40, 0, 3, 50, 7],
    ['yeonji', 0, 0, 0, 100, 0, 0],
    ['yewon', 0, 0, 0, 0, 0, 100],
    ['yogurt', 1, 1, 1, 1, 1, 95],
    ['yoobin', 20, 20, 20, 20, 20, 0],
    ['zhang', 15, 15, 20, 20, 15, 15],
    ['ziwony', 10, 20, 10, 20, 20, 20],
    ['zl존검사짱짱맨이다123', 1, 3, 7, 21, 17, 51],
    ['zzcc3210', 40, 30, 15, 5, 5, 5],
    ['\x7f', 0, 100, 0, 0, 0, 0],
    ['龜Turtle', 0, 100, 0, 0, 0, 0],
    ['강력한 청년.', 20, 20, 20, 20, 10, 10],
    ['곽다현', 50, 3, 30, 5, 5, 7],
    ['김춘봉', 0, 20, 20, 20, 20, 20],
    ['내캐릭터', 100, 0, 0, 0, 0, 0],
    ['뇽22', 0, 100, 0, 0, 0, 0],
    ['뇽뇽', 20, 20, 12, 35, 8, 5],
    ['민희현', 17, 17, 17, 17, 16, 16],
    ['볼리베어', 40, 20, 15, 10, 10, 5],
    ['새벽3시', 10, 20, 30, 20, 10, 10],
    ['숑숑', 20, 15, 24, 17, 22, 2],
    ['수민', 0, 0, 0, 0, 0, 100],
    ['아뵤뵹', 0, 0, 0, 0, 0, 100],
    ['예스윤서', 0, 30, 50, 0, 20, 0],
    ['와장창', 0, 0, 0, 0, 0, 100],
    ['이승현', 20, 40, 20, 20, 0, 0],
    ['장학문', 15, 0, 20, 15, 10, 40],
    ['주인공44', 0, 0, 0, 0, 0, 100],
    ['주인공96', 20, 10, 35, 10, 20, 5],
    ['차나현', 100, 0, 0, 0, 0, 0],
    ['치즈스틱', 10, 50, 15, 15, 5, 5],
    ['칭기즈칸', 0, 0, 0, 0, 0, 100],
    ['티엔청', 20, 20, 20, 20, 20, 0],
    ['하레', 50, 10, 10, 0, 30, 0],
    ['현우진', 1, 4, 20, 30, 30, 15],
    ['흑석동 포이리에', 100, 0, 0, 0, 0, 0],
    ]






# 제출 전 테스트에서 random 모듈을 사용하고 있어요.
import random

# ☆ 우리가 직접 함수 정의를 적어 둔 duel()들을 조금 더 적극적으로 사용하기 위한 기능들이 들어 있어요. 몰라도 돼요.
import functools

# 모듈 모아 테스트에서 time 모듈을 사용하여 모듈별 대결 시간을 재고 있어요.
import time

# 전체 테스트 흐름을 구성하는 함수
def test():
    print('-------------------------------')
    print('    과제#3 테스트용 프로그램')
    print('-------------------------------')
    print('탑재된 모듈(총 ' + str(len(modules)) + '개):')
    for module in modules:
        # ☆ 모듈의 이름 사전에 등재되어 있는 __name__에는 각 모듈의 '진짜 이름'이 담겨 있어요.
        print('    ' + module.__name__)
    print('-------------------------------')

    while True:
        print()
        print('테스트 옵션:')
        print('1. 제출 전 테스트(제출 가능! 뜨면 제출 가능!)')
        print('2. 모듈 모아 테스트(내 캐릭터가 평균 몇 등 뜨는지 확인)')
        print('3. 대결 결과 조회(어떤 모듈이 순위를 어떻게 매기는지 확인)')
        print('4. 테스트 종료')
        choice = input('선택하세요>')

        if choice == '1':
            choice = test_forSubmit
            # ☆ break문을 실행하면 이 break문이 적혀 있는 그 반복 실행 흐름을 중단해요.
            break
        elif choice == '2':
            choice = test_forPlay
            break
        elif choice == '3':
            choice = test_forProof
            break
        elif choice == '4':
            print('테스트 프로그램을 종료합니다.')
            return
        
        print('입력이 유효하지 않습니다.')

    # while문 실행이 끝났는데 아직 함수 내용물 실행이 끝나지 않았다면
    # choice에는 반드시 테스트용 함수가 담겨 있어요.
    print()
    choice()


# 과제 제출 전에 내 모듈이 올바르게 동작하고 있는지 테스트하는 함수
def test_forSubmit():
    print('제출 전 테스트 시작.')

    while True:
        print()
        print('테스트할 모듈 선택:')
        
        for idx_module in range(len(modules)):
            print(str(idx_module) + '. ' + modules[idx_module].__name__)
            
        choice = input('숫자를 입력하세요(그냥 엔터 치면 0번 골라줌)>')

        if choice == '':
            choice = 0
        else:
            choice = int(choice)

        if choice >= 0 and choice < len(modules):
            module = modules[idx_module]
            break

        print('입력이 유효하지 않습니다.')


    print()
    print('1차 테스트: 두 캐릭터 사이의 대결을 일관성 있게 수행하는지 검사합니다. (총 ' + str(len(stats) * (len(stats) - 1)) + '회 수행)')
    input('시작하려면 엔터 키를 쳐요>')


    # 캐릭터를 하나씩 집고...
    for stat_from in stats:
        copied_from = stat_from[:]

        if check(stat_from) == False:
            print('어? 캐릭터 정보가 규칙에 안 맞는게 끼어 있어요.')
            print('여러분이 수정한 게 아니면 강사에게 꼭 알려 주세요.')
            print('적발된 캐릭터 이름: ' + str(stat_from[0]))
            return

        print(stat_from[0] + ' vs 다른 캐릭터들. . .', end=' ')

        # 또 캐릭터를 하나씩 집고...
        for stat_to in stats:
            # ☆ ...나서 보니 양손에 든 캐릭터가 동일하면 이번 반복 내용물 실행을 스킵해요(바로 조건식 계산 단계로 돌아가요)
            if stat_from is stat_to:
                continue
            
            copied_to = stat_to[:]

            # duel(from, to) 수행
            result_from = module.duel(copied_from, copied_to)

            # 이 케이스는 return문을 만나지 못한 채 duel()이 끝나버렸을 가능성이 높아요.
            if result_from == None:
                print('실패!')
                print('duel() 결과에 해당하는 return값을 지정하지 않았습니다.')
                print(' left: ' + str(stat_from))
                print('right: ' + str(stat_to))
                print('강사의 예측: 분기 흐름이 목표대로 구성되어 있지 않은 것 같아요. return문을 적당한 곳에 적어 두었는지, 들여쓰기가 밀려 있지 않는지, return문을 잘 적어 두었는지 확인해 주세요.')
                return

            if type(result_from) != int or result_from == 0:
                print('실패!')
                print('duel()이 규칙에 맞지 않는 값을 return했습니다. 0이 아닌 int 형식 값을 return해야 해요!')
                print(' left: ' + str(stat_from))
                print('right: ' + str(stat_to))
                print('return값: ' + str(result_from) + ' (' + str(type(result_from)) + ' 형식)')
                print('강사의 예측: 수학적인 방법을 사용하다 float 형식 값을 그대로 return했을 가능성,')
                print('             또는 실수로 캐릭터의 이름(str 형식 값)을 return했을 가능성이 존재해요.')
                print('             return int(result)와 같이 명백하게 int 형식 값을 return하도록 적어 두면 보통은 문제가 풀릴 거예요.')
                return
                
            # 이 케이스는 실수로 할당문을 실행해버렸거나 해서 캐릭터 정보를 변경하면 걸려요.
            if stat_from != copied_from:
                print('실패!')
                print('duel()이 left 능력치 값을 변경했습니다.')
                print('호출 전 left: ' + str(stat_from))
                print('호출 후 left: ' + str(copied_from))
                print('강사의 예측: 인수로 보내주는 list에 담긴 값은 변경하지 말아주세요. 만약 필요하다면 사본을 만들어 계산에 활용해 주세요.')
                return

            # 이 케이스도, 실수로 할당문을 실행해버렸거나 해서 캐릭터 정보를 변경하면 걸려요.
            if stat_to != copied_to:
                print('실패!')
                print('duel()이 right 능력치 값을 변경했습니다.')
                print('호출 전 right: ' + str(stat_to))
                print('호출 후 right: ' + str(copied_to))
                print('강사의 예측: 인수로 보내주는 list에 담긴 값은 변경하지 말아주세요. 만약 필요하다면 사본을 만들어 계산에 활용해 주세요.')
                return


            # duel(to, from) 수행
            result_to = module.duel(copied_to, copied_from)

            if result_to == None:
                print('실패!')
                print('duel() 결과에 해당하는 return값을 지정하지 않았습니다.')
                print(' left: ' + str(stat_to))
                print('right: ' + str(stat_from))
                print('강사의 예측: 분기 흐름이 목표대로 구성되어 있지 않은 것 같아요. return문을 적당한 곳에 적어 두었는지, 들여쓰기가 밀려 있지 않는지 확인해 주세요.')
                return

            if type(result_to) != int or result_to == 0:
                print('실패!')
                print('duel()이 규칙에 맞지 않는 값을 return했습니다. 0이 아닌 int 형식 값을 return해야 해요!')
                print(' left: ' + str(stat_to))
                print('right: ' + str(stat_from))
                print('return값: ' + str(result_to) + ' (' + str(type(result_to)) + ' 형식)')
                print('강사의 예측: 수학적인 방법을 사용하다 float 형식 값을 그대로 return했을 가능성,')
                print('             또는 실수로 이름(str 형식 값)을 return했을 가능성이 존재해요.')
                print('             return int(result)와 같이 명백하게 int 형식 값을 return하도록 적어 두면 보통은 문제가 풀릴 거예요.')
                return
            
            if stat_to != copied_to:
                print('실패!')
                print('duel()이 left 능력치 값을 변경했습니다.')
                print('호출 전 left: ' + str(stat_to))
                print('호출 후 left: ' + str(copied_to))
                print('강사의 예측: 인수로 보내주는 list에 담긴 값은 변경하지 말아주세요. 만약 필요하다면 사본을 만들어 계산에 활용해 주세요.')
                return
            
            if stat_from != copied_from:
                print('실패!')
                print('duel()이 right 능력치 값을 변경했습니다.')
                print('호출 전 right: ' + str(stat_from))
                print('호출 후 right: ' + str(copied_from))
                print('강사의 예측: 인수로 보내주는 list에 담긴 값은 변경하지 말아주세요. 만약 필요하다면 사본을 만들어 계산에 활용해 주세요.')
                return


            # duel(from, to)와 duel(to, from)은 결과가 서로 대칭이어야 해요.
            # 우리가 제출한 캐릭터 정보들은 모두 다 다르므로(적어도 이름은 다 다름) 무승부는 절대 일어나지 않아요!
            # 따라서 이 케이스에 해당한다는 것은 이겼는데 패배에 해당하는 분기에 진입했거나 했을 가능성이 높아요.
            if result_from * result_to >= 0:
                print('실패!')
                print('duel()의 return값이 일관적이지 않습니다.')
                print(' left: ' + str(stat_from))
                print('right: ' + str(stat_to))
                print('duel(left, right) 결과: ' + str(result_from))
                print('duel(right, left) 결과: ' + str(result_to))
                print('--> 둘 중 하나는 음수, 하나는 양수가 나와야만 해요!')
                print('강사의 예측: 승리/패배 중 한 쪽에 해당하는 분기에서 적절한 return문을 실행해서 함수 내용물 실행을 끝내버려야 하는데 그렇지 않았을 가능성이 있어요. return문이 적재적소에 적혀 있나 확인해 주세요.')
                return
                
        print('완벽!')

    print('1차 테스트 통과!')



    print()
    print('2차 테스트: 캐릭터 40명을 뽑아 임의의 순서로 나열해 놓고 대결시켰을 때')
    print('           언제나 동일한 결과가 나오나 확인합니다. (10샘플, 샘플당 20게임 수행)')
    input('시작하려면 엔터 키를 쳐요>')

    # 총 10번 샘플링 수행
    for count_sample in range(10):
        print(str(count_sample) + '번째 샘플. . .', end=' ')

        # 각 샘플마다 검사용 원본을 먼저 만들어 두어요.

        # ☆ random.sample()은 시퀀스에서 주어진 갯수만큼 값을 꺼내 담은 새로운 list를 return해요.
        stats_selected = random.sample(stats, 40)

        # 이 부분이 실제 '게임'을 진행하는 부분이에요.
        
        # ☆ list.sort()는 주어진 함수를 가지고 list의 내용을 쫙 줄세우기해요.
        result_origin = stats_selected[:]
        result_origin.sort(key=functools.cmp_to_key(module.duel))

        # 원본은 특별히, 능력치가 같은 캐릭터들이 결과 list에서 서로 이웃하고 있는지 추가로 확인해요.
        # 능력치가 다르다면 반드시 능력치만 가지고 승부를 내야 하는데,
        # 이 규칙을 지키지 않았다면 이 부분에서 걸리게 돼요.
        #
        # 주: 이 부분은 지금 당장은 납득하기 어려울 수 있으니 안 읽는 것을 추천해요.
        idx_from = 0
        
        while idx_from < 9:
            isDifferentStatFound = False

            for idx_to in range(idx_from + 1, len(stats_selected)):
                if isSameStat(result_origin[idx_from], result_origin[idx_to]):
                    if isDifferentStatFound:
                        print('실패!')
                        print('능력치가 동일한 캐릭터들이 비슷한 등수를 차지하지 못했습니다.')
                        for idx in range(idx_to + 1):
                            print(str(idx) + '등: ' + str(result_origin[idx]))
                        print('여기서 ' + str(idx_from) + '등과 ' + str(idx_to) + '등 사이에 다른 능력치를 가진 캐릭터가 끼어 있어요.')
                        print('강사의 예측: 능력치가 서로 다름에도 불구하고 이름을 가지고 승부를 냈을 가능성이 있어요. 여섯 능력치를 모두 잘 검사하고 있나 확인해 주세요.')
                        return

                    idx_from = idx_to
                else:
                    isDifferentStatFound = True

            idx_from += 1
            

        # 샘플의 순서를 섞어가며 총 20게임을 진행해요(검사용 원본 게임을 방금 했으니 19번만 더 하면 됨)
        for count_game in range(19):

            # ☆ random.shuffle()은 주어진 list의 순서를 마구 섞어요.
            new_selected = stats_selected[:]
            random.shuffle(new_selected)
            
            # 이 부분이 실제 '게임'을 진행하는 부분이에요.

            # ☆ list.sort()는 주어진 함수를 가지고 list의 내용을 쫙 줄세우기해요.
            result_new = new_selected[:]
            result_new.sort(key=functools.cmp_to_key(module.duel))

            # 셔플 후 다시 게임을 진행해도 원본과 동일한 결과가 나와야 해요!
            if result_origin != result_new:
                print('실패!')
                print('게임 결과가 일관적이지 않습니다.')
                print(' 0번 게임 전: [ ', end=' ')
                for stat in stats_selected:
                    print(stat[0], end=' ')
                print(']')
                print(' 0번 게임 후: [ ', end=' ')
                for stat in result_origin:
                    print(stat[0], end=' ')
                print(']')
                print('이번 게임 전: [ ', end=' ')
                for stat in new_selected:
                    print(stat[0], end=' ')
                print(']')
                print('이번 게임 후: [ ', end=' ')
                for stat in result_new:
                    print(stat[0], end=' ')
                print(']')
                print('--> 동일 샘플에 대해서는 나열 순서가 달라도 언제나 동일한 결과를 내야 해요.')
                print('강사의 예측: 이름 비교를 할 때 단순히 이름 길이만 가지고 승부를 냈다면 여기서 걸릴 수 있어요. 이름 길이가 같을 때에는 각 이름 글자들을 감안해서라도 정확히 승부를 매겨야 해요.')
                return

        print('완벽!')

    print('2차 테스트 통과!')



    print()
    print('최종 테스트: 모든 캐릭터 정보를 임의의 순서로 나열해 놓고 대결시켰을 때')
    print('            언제나 동일한 결과가 나오나 확인합니다. (20게임 수행)')
    input('시작하려면 엔터 키를 쳐요>')

    # 매 게임마다 전체 캐릭터 목록을 셔플하며 게임을 진행해요.

    print('0번째 게임. . .', end=' ')
    
    # 일단 첫 게임은 검사용 원본이에요.
    result_origin = stats[:]
    random.shuffle(result_origin)
    result_origin.sort(key=functools.cmp_to_key(module.duel))

    # 원본은 특별히, 능력치가 같은 캐릭터들이 결과 list에서 서로 이웃하고 있는지 추가로 확인해요.
    # 능력치가 다르다면 반드시 능력치만 가지고 승부를 내야 하는데,
    # 이 규칙을 지키지 않았다면 이 부분에서 걸리게 돼요.
    #
    # 주: 이 부분은 지금 당장은 납득하기 어려울 수 있으니 안 읽는 것을 추천해요.
    idx_from = 0
    
    while idx_from < len(stats) - 1:
        isDifferentStatFound = False

        for idx_to in range(idx_from + 1, len(stats)):
            if isSameStat(result_origin[idx_from],result_origin[idx_to]):
                if isDifferentStatFound:
                    print('실패!')
                    print('능력치가 동일한 캐릭터들이 비슷한 등수를 차지하지 못했습니다.')
                    for idx in range(idx_from, idx_to + 1):
                        print(str(idx) + '등: ' + str(result_origin[idx]))
                    print('여기서 ' + str(idx_from) + '등과 ' + str(idx_to) + '등 사이에 다른 능력치를 가진 캐릭터가 끼어 있어요.')
                    print('강사의 예측: 능력치가 다름에도 불구하고 이름을 가지고 승부를 냈을 가능성이 있어요. 여섯 능력치를 모두 잘 검사하고 있나 확인해 주세요.')
                    return

                idx_from = idx_to
            else:
                isDifferentStatFound = True

        idx_from += 1

    print('완벽!')
    
    # 순서를 섞어가며 총 20게임을 진행해요(검사용 원본 게임을 방금 했으니 19번만 더 하면 됨)
    for count_game in range(1, 20):
        print(str(count_game) + '번째 게임. . .', end=' ')
        
        result_new = stats[:]
        random.shuffle(result_new)
        result_new.sort(key=functools.cmp_to_key(module.duel))
        
        # 셔플 후 다시 게임을 진행해도 원본과 동일한 결과가 나와야 해요!
        if result_origin != result_new:
            print('실패!')
            print('게임 결과가 일관적이지 않습니다.')
            print('오류 내용을 출력하기에는 너무 Data가 많으니, 2차 테스트를 몇 번 더 수행해 보는 것이 좋겠어요.')
            print('--> 나열 순서가 달라도 언제나 동일한 결과를 내야 해요.')
            print('강사의 예측: 이름 비교를 할 때 단순히 이름 길이만 가지고 승부를 냈다면 여기서 걸릴 수 있어요. 이름 길이가 같을 때에는 각 이름 글자들을 감안해서라도 정확히 승부를 매겨야 해요.')
            return

        print('완벽!')


    print('최종 테스트 통과!')

    # 최종 테스트까지 전부 통과하면 과제 성공이에요!
    print('제출 가능!')
    


# 여러 모듈을 모은 다음 실행하면 내 캐릭터가 평균 몇 등을 기록하는지 확인할 수 있는 함수
# 친구들이 만든 모듈을 가져와서 등록하면 친선전을 해 볼 수 있어요!
#
# 주: 이 함수 안에는 우리가 안 배운 것들이 가득 들어 있으니 안 읽는 것을 권장해요.
def test_forPlay():
    print('모듈 모아 테스트 시작.')
    print('주의: 일단 각 모듈들에 대해 제출 전 테스트를 돌려보고 오는 게 좋아요.')
    print('      테스트에 통과하지 않은 모듈을 섞어 쓰는 경우 결과가 이상하게 나올 수 있어요!')
    print()

    # ☆ 빈 사전을 하나 준비했어요.
    scores = {}

    # ☆ 사전에 캐릭터 이름들을 등재하면서, 그 옆 칸은 전부 0을 담고 있어요.
    for stat in stats:
        scores[stat[0]] = 0

    # 모듈 list에서 모듈을 하나씩 꺼내서 게임을 진행해요.    
    for module in modules:
        print(module.__name__ + '.duel()을 사용하여 게임 진행. . .', end=' ')

        copied_stats = stats[:]

        # 줄세우기를 진행하고, 걸리는 시간을 재요.
        startTime = time.perf_counter()
        copied_stats.sort(key=functools.cmp_to_key(module.duel))
        elapsedTime = time.perf_counter() - startTime

        # ☆ 여기를 읽고 있다니... 그러면 아래 코드에 대한 주석 설명 읽기도 한 번 도전해 봐요.
        #
        #    이 아래 코드의 목적은 각 캐릭터의 등수를 확인해서 scores 사전을 갱신하는 거예요.
        #    이 때, 예를 들어 3, 4, 5등이 동일한 능력치를 가지고 있다면 셋 다 '공동 3등'으로 간주해 주려 해요.

        # 일단 0등부터 확인 시작
        idx_from = 0
        
        while idx_from < len(stats):
            # 이번 등수 값을 빽껍해 둠
            idx_from_backup = idx_from

            # ☆ 일단 이 캐릭터의 등수는 고정이므로 바로 사전 갱신
            scores[copied_stats[idx_from][0]] += idx_from

            # 이제 이 캐릭터와 동일한 능력치를 가진 다른 캐릭터가 존재하는지 확인
            # (제출 전 테스트를 통과했다면 능력치가 같은 캐릭터들은 반드시 한 곳에 몰려 있어요)
            for idx_to in range(idx_from + 1, len(stats)):
                # 다른 능력치를 가진 캐릭터를 발견하면 반복 중단
                if not isSameStat(copied_stats[idx_from], copied_stats[idx_to]):
                    break

                # 반복이 중단되지 않았다는 것은 얘 능력치도 동일하다는 의미이므로 위에 빽껍해 둔 등수 값을 가지고 사전 갱신
                scores[copied_stats[idx_to][0]] += idx_from_backup

                # 방금 얘의 갱신을 끝냈으므로 다음에 또 얘를 다루지 않도록 idx 값을 보정해 둠
                idx_from = idx_to

            # 종종 봐 왔던 '다음 반복 준비' 부분
            idx_from += 1

        print('끝! - {0:13.10f}초 걸림!'.format(elapsedTime))

    print()
    print('합산 결과:')
    
    # ☆ dict.items()는 사전에 등재된 각 항목들을 [(왼쪽0, 오른쪽0), (왼쪽1, 오른쪽1), ...]과 같은 느낌으로 담아서 제공해요.
    result = list(scores.items())

    # ☆ lambda 연산자를 써서 list 줄세우기의 대결 조건을 정하고 있어요.
    #    여기엔 강사의 덕심이 강하게 반영되어 있으니 설명을 듣고 싶은 친구들은 갠톡 ㄱㄱ해 주세요.
    result.sort(key=functools.cmp_to_key(lambda left, right: left[1] - right[1]))

    # ☆ 보다 깔끔하게 통계 결과를 보여줄 수 있도록 str.format()을 쓰고 있어요.
    #    이건 지금 당장 살펴 보기에는 좀 많이 번거로우니 후반부를 기약해 봅시다.
    for idx in range(len(stats)):
        print('{0:3}등({1:5}점): {2}'.format(idx, result[idx][1], result[idx][0]))
        

# 이 함수를 통해 어떤 모듈이 각 캐릭터를 정확히 몇 등으로 간주하는지 확인해 볼 수 있어요.
#
# 주: 이 함수는 비교적 간단하게 구성해 두었으니 읽을만 할 거예요.
def test_forProof():
    print('대결 결과 조회 시작.')
    print('주의: 일단 조회할 모듈에 대해 제출 전 테스트를 돌려보고 오는 게 좋아요.')
    print('      테스트에 통과하지 않은 모듈을 쓰는 경우 결과가 이상하게 나올 수 있어요!')
    print()

    # 대결 결과 조회는 한 번 실행할 때 여러 모듈을 한 번씩 돌려보고 싶을 가능성이 있으므로
    # 전체 내용을 큰 반복문으로 감싸 두었어요(다 끝나고 0 누르면 재선택 가능)
    while True:
        
        while True:
            print()
            print('조회할 모듈 선택:')
            
            for idx_module in range(len(modules)):
                print(str(idx_module) + '. ' + modules[idx_module].__name__)
                
            choice = input('숫자를 입력하세요(그냥 엔터 치면 0번 골라줌)>')

            if choice == '':
                choice = 0
            else:
                choice = int(choice)

            if choice >= 0 and choice < len(modules):
                module = modules[idx_module]
                break

            print('입력이 유효하지 않습니다.')

        # ☆ 결과 출력할 때 이름만 볼 지 능력치도 같이 볼 지 결정
        #    이건 지금 당장 살펴 보기에는 좀 많이 번거로우니 후반부를 기약해 봅시다.
        if input('각 캐릭터의 능력치를 함께 조회하려면 0을 입력하세요>') == '0':
            result_format = '{0:3}등: {1}, {2}'
        else:
            result_format = '{0:3}등: {1}'
            


        print('대결 진행. . .', end=' ')
        copied_stats = stats[:]
        copied_stats.sort(key=functools.cmp_to_key(module.duel))
        print('끝!')

        
        for idx in range(len(stats)):
            # ☆ 보다 깔끔하게 통계 결과를 보여줄 수 있도록 str.format()을 쓰고 있어요.
            #    이건 지금 당장 살펴 보기에는 좀 많이 번거로우니 후반부를 기약해 봅시다.
            print(result_format.format(idx, copied_stats[idx][0], copied_stats[idx][1:]))

        print()
        print('주#1: Interactive에서도 Ctrl + F 눌러서 내 캐릭터 이름을 찾아볼 수 있어요.')
        print()
        print('주#2: 테스트를 통과했다면 능력치가 동일한 캐릭터들은 항상 비슷한 등수를 갖게 되며,')
        print('      모듈 모아 테스트에서는 이들이 모두 공동 순위로 간주돼요.')
        print('      예) 3, 4, 5등이 능력치가 같다면 모두 3등으로 간주됨')
        print()

        # 이번 모듈에 대한 결과 조회가 끝나고 나면 반복을 그만 둘 것인지 물어봐요.
        if input('다른 모듈도 테스트해 보려면 0을 입력하세요>') != '0':
            break

# 캐릭터 정보가 규칙에 맞는지 확인하는 함수
# 1차 테스트 과정에서 살짝 돌려보고 있어요.
def check(stat):
    hab = stat[1] + stat[2] + stat[3] + stat[4] + stat[5] + stat[6]

    # 능력치 값의 형식 및 길이, 이름의 형식, 각 능력치의 형식, 능력치 합이 100인지를 모두 체크해서
    # 이들 중 하나라도 어긋나면 규칙 위반이 됨
    return type(stat) == list and len(stat) == 7 and type(stat[0]) == str and type(hab) == int and hab == 100



# 두 캐릭터의 능력치가 동일한지 여부를 return하는 함수
# 뭐하는거지 싶을 수 있는데 이 버전이 성능은 가장 좋았어요.
def isSameStat(left, right):
    # left 이름을 빽껍해 두고 left 이름 자리에 right 이름을 담음
    name_backup = left[0]
    left[0] = right[0]

    # left와 right가 모든 칸에 동일한 값을 담고 있는지 확인
    result = left == right

    # 확인이 끝나면 빽껍해 둔 left 이름을 복원
    left[0] = name_backup

    # 방금 확인했던 결과를 return
    return result


test()
