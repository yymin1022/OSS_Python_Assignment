import gui_core as gui
import random

window_height = 600
window_width = 800

w = gui.Window(title='타이핑 게임', width=window_width, height=window_height, interval=1 / 60, printKeyInfos=True)

words_active = []
words_pool = ["hello", "world", "apple", "banana"]

life_cnt = 3

cur_stage = 1
game_started = False
score_current = 0
score_high = 0
score_total = 0

cheat_enabled = False
cheat_enabled_time = 0
cheat_time = 10
cheat_word = "hellocheat"

word_last_spawn_time = 0
word_spawn_interval = 1

input_view = None
input_word = ""


def spawn_word():
    global words_active
    word_new = random.choice(words_pool)
    x = random.randint(150, window_width - 150)
    y = -20
    obj_id = w.newText(x, y, width=100, text=word_new, fill_color='black', anchor='nw')
    words_active.append({'text': word_new, 'id': obj_id, 'x': x, 'y': y})


def is_alpha(key):
    return key in "abcdefghijklmnopqrstuvwxyz"


def initialize(timestamp):
    global cur_stage, game_started, input_view, life_cnt, score_current, score_high, score_total, words_active, word_last_spawn_time
    w.setTitle(f'Typing Game - Life : {life_cnt} | score_current : {score_current}')

    life_cnt = 3

    cur_stage = 1
    game_started = False
    score_current = 0
    score_high = 0
    score_total = 0

    words_active.clear()
    word_last_spawn_time = timestamp

    input_view = w.newText(10, 10, width=400, text=f"입력: {input_word}")


def update(timestamp):
    global cheat_enabled, cheat_enabled_time, cheat_time, cheat_word, \
        words_active, word_last_spawn_time, word_spawn_interval, \
        game_started, life_cnt, score_current, input_view, input_word

    if not game_started:
        for key in list(w.keys.keys()):
            if w.keys[key]:
                w.keys[key] = False
                if key == "Return":
                    game_started = True
                elif key == "Escape":
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
                if word_info['y'] > window_height:
                    life_cnt -= 1
                    words_active.remove(word_info)
                    w.deleteObject(word_info['id'])
                    w.setTitle(f'Typing Game - Life : {life_cnt} | score_current : {score_current}')
                    if life_cnt <= 0:
                        w.stop()
                        return

        w.setText(input_view, f"입력: {input_word}")

        for key in list(w.keys.keys()):
            if w.keys[key]:
                w.keys[key] = False

                if len(key) == 1 and is_alpha(key):
                    input_word += key
                elif key == "Return":
                    if input_word == cheat_word:
                        cheat_enabled = True
                        cheat_enabled_time = timestamp
                    else:
                        for word_info in words_active:
                            if word_info['text'] == input_word:
                                score_current += 10
                                words_active.remove(word_info)
                                w.deleteObject(word_info['id'])
                                w.setTitle(f'Typing Game - Life : {life_cnt} | score_current : {score_current}')
                                break
                    input_word = ""
                elif key == "BackSpace":
                    input_word = input_word[:-1]
                elif key == "Escape":
                    w.stop()


w.initialize = initialize
w.update = update

w.start()
