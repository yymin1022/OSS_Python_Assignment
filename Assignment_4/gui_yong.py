"""
소프트웨어학부 20194094 유용민 (https://github.com/yymin1022)
Typo Game

How To
- 실행한 뒤, Enter (혹은 Return)를 누르면 게임이 시작됩니다
- 하늘에서 내려오는 단어들을 입력한 뒤, Enter (혹은 Return)를 누르면 해당 단어가 사라집니다
- 단어 하나가 사라질 때마다 10점씩 가산되며, 100점이 모이면 해당 단계를 클리어해 다음 단계로 이동합니다.
- 단계가 오를 떄마다 속도가 증가합니다.
- 단어를 입력하지 못해 바닥에 닿게 되면 목숨이 줄어들며, 3개의 목숨이 모두 줄어들게 되면 게임이 끝나게됩니다.
- 게임 도중에 hellocheat 를 입력할 경우, Cheat Mode로 전환되어 10초간 단어가 내려오지 않고 멈춥니다.
"""

import gui_core as gui
import random

window_height = 600
window_width = 800

w = gui.Window(title='타이핑 게임', width=window_width, height=window_height, interval=1 / 60, printKeyInfos=True)

words_active = []
words_pool = [
    'apple', 'ball', 'cat', 'dog', 'elephant',
    'fish', 'grape', 'house', 'ice', 'juice',
    'kite', 'lion', 'monkey', 'nose', 'orange',
    'pencil', 'queen', 'rabbit', 'sun', 'tree',
    'umbrella', 'van', 'water', 'xylophone', 'yarn',
    'zebra', 'book', 'chair', 'door', 'egg'
]

cur_stage = 1
game_started = False
life_cnt = 3
score_current = 0
score_total = 0

cheat_enabled = False
cheat_enabled_time = 0
cheat_time = 10
cheat_word = 'hellocheat'

word_last_spawn_time = 0
word_spawn_interval = 1

cheat_status_view = None
img_bg_view = None
input_view = None
life_view = None
score_current_view = None
score_total_view = None
stage_view = None

input_word = ""


def is_alpha(key):
    return key in 'abcdefghijklmnopqrstuvwxyz'


def spawn_word():
    global words_active

    word_new = random.choice(words_pool)
    x = random.randint(150, window_width - 150)
    y = -20
    obj_id = w.newText(x, y, width=100, text=word_new, fill_color='black', anchor='center')
    words_active.append({'text': word_new, 'id': obj_id, 'x': x, 'y': y})


def start_game(timestamp):
    global cheat_enabled, game_started, score_current, words_active, word_last_spawn_time, \
        input_view

    cheat_enabled = False
    score_current = 0

    words_active.clear()
    word_last_spawn_time = timestamp

    update_text()
    game_started = True


def stop_game():
    global game_started, score_current, score_total, input_view

    score_total += score_current
    score_current = 0

    for word_info in words_active:
        w.deleteObject(word_info['id'])
    words_active.clear()

    update_text()
    game_started = False


def reset_game():
    global cur_stage, life_cnt, score_current, score_total

    cur_stage = 1
    life_cnt = 3
    score_current = 0
    score_total = 0


def update_text():
    global cheat_enabled, game_started, \
        cheat_status_view, input_view, life_view, score_current_view, score_total_view, stage_view

    if game_started:
        w.setText(input_view, input_word)
    else:
        w.setText(input_view, 'Press Return to Start')

    if cheat_enabled:
        w.setText(cheat_status_view, 'CHEAT MODE')
    else:
        w.setText(cheat_status_view, "")

    w.setText(life_view, f'Life Remained: {life_cnt}')
    w.setText(score_current_view, f'Current Score: {score_current}')
    w.setText(score_total_view, f'Total Score: {score_total}')
    w.setText(stage_view, f'Current Stage: {cur_stage}')


def init_view(_):
    global cur_stage, game_started, life_cnt, score_current, score_total, \
        words_active, word_last_spawn_time, \
        cheat_status_view, img_bg_view, input_view, life_view, score_current_view, score_total_view, stage_view
    w.setTitle(f'Typing Game')

    img_bg_view = w.newImage(-5, -5, 'img_bg.png', new_width=window_width + 5, new_height=window_height + 5)
    input_view = w.newText(window_width / 2, window_height - 50, width=400, text='Press Return to Start',
                           anchor='center', fill_color='white')

    cheat_status_view = w.newText(window_width - 20, 20, width=200, text="", anchor='ne', fill_color='white')
    life_view = w.newText(40, 60, width=200, text=f'Life Remained: {life_cnt}', anchor='nw')
    score_current_view = w.newText(40, 80, width=200, text=f'Current Score: {score_current}', anchor='nw')
    score_total_view = w.newText(40, 100, width=200, text=f'Total Score: {score_total}', anchor='nw')
    stage_view = w.newText(40, 40, width=200, text=f'Current Stage: {cur_stage}', anchor='nw')


def update_view(timestamp):
    global cheat_enabled, cheat_enabled_time, cheat_time, cheat_word, \
        game_started, input_word, life_cnt, cur_stage, score_current, \
        words_active, word_last_spawn_time, word_spawn_interval, \
        input_view, life_view, score_current_view, score_total_view, stage_view

    update_text()

    if not game_started:
        for key in list(w.keys.keys()):
            if w.keys[key]:
                w.keys[key] = False
                if key == 'Return':
                    start_game(timestamp)
                elif key == 'Escape':
                    w.stop()
    else:
        if timestamp - cheat_enabled_time > cheat_time:
            cheat_enabled = False
            cheat_enabled_time = 0

        if not cheat_enabled:
            if timestamp - word_last_spawn_time > word_spawn_interval:
                spawn_word()
                word_last_spawn_time = timestamp

            for word_info in words_active:
                word_info['y'] += 1.5 * cur_stage
                w.moveObject(word_info['id'], word_info['x'], word_info['y'])
                if word_info['y'] > window_height - 110:
                    life_cnt -= 1
                    words_active.remove(word_info)
                    w.deleteObject(word_info['id'])
                    if life_cnt <= 0:
                        reset_game()
                        stop_game()

        if score_current >= 100:
            cur_stage += 1
            stop_game()

        for key in list(w.keys.keys()):
            if w.keys[key]:
                w.keys[key] = False

                if len(key) == 1 and is_alpha(key):
                    input_word += key
                elif key == 'Return':
                    if input_word == cheat_word:
                        cheat_enabled = True
                        cheat_enabled_time = timestamp
                    else:
                        for word_info in words_active:
                            if word_info['text'] == input_word:
                                score_current += 10
                                words_active.remove(word_info)
                                w.deleteObject(word_info['id'])
                                break
                    input_word = ""
                elif key == 'BackSpace':
                    input_word = input_word[:-1]
                elif key == 'Escape':
                    w.stop()


w.initialize = init_view
w.update = update_view

w.start()
