'''
7. .wav 파일 재생 방법 소개

- 중간중간 F5를 눌러 interactive를 켜 둔 다음 진행하면
  IDLE이 함수 호출식 적을 때마다 적당한 툴팁을 읽어 보여줄 거예요
'''

import gui_core as gui


w = gui.Window('눌러보세요', 265, 265)


def initialize(timestamp):
    w.data.filename_normal = 'button.png'
    w.data.filename_pressed = 'button_pressed.png'

    w.data.filename_audio = 'sample.wav'
    w.data.audio_duration = 1.093
    w.data.audio_last_start_time = 0

    w.data.number = w.newImage(0, 0, w.data.filename_normal)


def update(timestamp):
    if w.keys['Escape']:
        w.stop()
        return

    if ( w.mouse_buttons[1] and # 마우스 왼쪽 버튼을 누르고 있고
         
         w.mouse_position_x >= 0 and # 마우스 포인터 위치가 '화면 안'이면
         w.mouse_position_x < 265 and
         w.mouse_position_y >= 0 and
         w.mouse_position_y < 265):
        
        # 마지막으로 음원을 재생한 이후로 일정 시간이 경과한 경우 재생 시작
        if timestamp > w.data.audio_last_start_time + w.data.audio_duration:
            w.setImage(w.data.number, w.data.filename_pressed)
            w.data.audio_last_start_time = timestamp
            w.playSound(w.data.filename_audio)
            
    elif timestamp > w.data.audio_last_start_time + w.data.audio_duration:
        w.setImage(w.data.number, w.data.filename_normal)

w.initialize = initialize
w.update = update

w.start()
