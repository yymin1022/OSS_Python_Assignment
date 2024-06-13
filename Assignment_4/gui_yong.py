import gui_core as gui
import random

w = gui.Window(title='타이핑 게임', width=800, height=600, interval=1 / 60, printKeyInfos=True)

words_active = []
words_pool = ["hello", "world", "apple", "banana"]

life_cnt = 3

high_score = 0
score = 0

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
    x = random.randint(150, w.internals얘는안봐도돼요.canvas.winfo_width() - 150)
    y = -20
    obj_id = w.newText(x, y, width=100, text=word_new, fill_color='black', anchor='nw')
    words_active.append({'text': word_new, 'id': obj_id, 'x': x, 'y': y})


def is_alpha(key):
    return key in "abcdefghijklmnopqrstuvwxyz"


def initialize(timestamp):
    global input_view, life_cnt, score, words_active, word_last_spawn_time
    w.setTitle(f'Typing Game - Life : {life_cnt} | Score : {score}')

    life_cnt = 3
    score = 0

    input_view = w.newText(10, 10, width=400, text=f"입력: {input_word}")

    words_active.clear()
    word_last_spawn_time = timestamp


def update(timestamp):
    global cheat_enabled, cheat_enabled_time, cheat_time, cheat_word, \
        word_last_spawn_time, word_spawn_interval, \
        life_cnt, score, input_view, input_word, \
        words_active

    if timestamp - cheat_enabled_time > cheat_time:
        cheat_enabled = False
        cheat_enabled_time = 0

    if not cheat_enabled:
        if timestamp - word_last_spawn_time > word_spawn_interval:
            spawn_word()
            word_last_spawn_time = timestamp

        for word_info in words_active:
            word_info['y'] += 1
            w.moveObject(word_info['id'], word_info['x'], word_info['y'])
            if word_info['y'] > w.internals얘는안봐도돼요.canvas.winfo_height():
                life_cnt -= 1
                words_active.remove(word_info)
                w.deleteObject(word_info['id'])
                w.setTitle(f'Typing Game - Life : {life_cnt} | Score : {score}')
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
                            score += 10
                            words_active.remove(word_info)
                            w.deleteObject(word_info['id'])
                            w.setTitle(f'Typing Game - Life : {life_cnt} | Score : {score}')
                            break
                input_word = ""
            elif key == "BackSpace":
                input_word = input_word[:-1]
            elif key == "Escape":
                w.stop()


w.initialize = initialize
w.update = update

w.start()
