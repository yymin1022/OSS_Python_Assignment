import gui_core as gui
import random

w = gui.Window(title='타이핑 게임', width=800, height=600, interval=1 / 60, printKeyInfos=True)

words = ["hello", "world", "apple", "banana"]
active_words = []
life_cnt = 3
score = 0

last_spawn_time = 0
spawn_interval = 2
input_view = None
input_word = ""


def spawn_word():
    word = random.choice(words)
    x = random.randint(50, w.internals얘는안봐도돼요.canvas.winfo_width() - 150)
    y = -20
    obj_id = w.newText(x, y, width=100, text=word, fill_color='black', anchor='nw')
    active_words.append({'text': word, 'id': obj_id, 'x': x, 'y': y})


def initialize(timestamp):
    global last_spawn_time, life_cnt, score, active_words, input_view
    last_spawn_time = timestamp
    life_cnt = 3
    score = 0
    active_words.clear()
    w.setTitle('Typing Game')
    input_view = w.newText(10, 10, width=400, text=f"입력: {input_word}")


def update(timestamp):
    global last_spawn_time, spawn_interval, life_cnt, score, input_view, input_word

    if timestamp - last_spawn_time > spawn_interval:
        spawn_word()
        last_spawn_time = timestamp

    for word_info in active_words[:]:
        word_info['y'] += 1
        w.moveObject(word_info['id'], word_info['x'], word_info['y'])
        if word_info['y'] > w.internals얘는안봐도돼요.canvas.winfo_height():
            life_cnt -= 1
            w.setTitle(f'타이핑 게임 - 목숨: {life_cnt}')
            w.deleteObject(word_info['id'])
            active_words.remove(word_info)
            if life_cnt <= 0:
                w.setTitle(f'타이핑 게임 - 게임 오버! 점수: {score}')
                w.stop()
                return

    w.setText(input_view, f"입력: {input_word}")

    for key in list(w.keys.keys()):
        if w.keys[key]:
            w.keys[key] = False

            if key == "Return":
                for word_info in active_words[:]:
                    if word_info['text'] == input_word:
                        score += 10
                        w.deleteObject(word_info['id'])
                        active_words.remove(word_info)
                        break
                input_word = ""
            elif key == "BackSpace":
                input_word = input_word[:-1]
            elif key == "Escape":
                exit(0)
            elif len(key) == 1:
                input_word += key


w.initialize = initialize
w.update = update

w.start()
