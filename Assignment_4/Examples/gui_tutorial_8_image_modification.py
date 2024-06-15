'''
8. 그림을 픽셀 단위로 다루는 방법 소개

- 주의:
    이 기능은 아직 완전하지 않아요.
    내 GUI 프로젝트에서 이 기능을 사용하고 싶다면 미리 강사와 상담해 주세요
    
- 중간중간 F5를 눌러 interactive를 켜 둔 다음 진행하면
  IDLE이 함수 호출식 적을 때마다 적당한 툴팁을 읽어 보여줄 거예요
'''

import gui_core as gui


w = gui.Window('선택한 픽셀 수: 0', 320, 320)


def initialize(timestamp):
    # 인수들 중 filename은 None으로 지정하고 width와 height를 직접 지정하면
    # 임의의 크기를 갖는 무색 그림을 만들어 사용할 수 있어요
    w.data.number = w.newImage(0, 0, None, 320, 320)

    w.data.red_selected = 0
    w.data.green_selected = 0
    w.data.blue_selected = 0xFF
    
    w.data.count_pixels_selected = 0


def update(timestamp):
    if w.keys['Escape']:
        w.stop()
        return

    if ( w.mouse_buttons[1] and
         w.mouse_position_x >= 0 and
         w.mouse_position_x < 320 and
         w.mouse_position_y >= 0 and
         w.mouse_position_y < 320 ):

        # w.getPixelColor()를 사용하여 그림의 특정 픽셀의 색상 값을 확인할 수 있어요
        red, green, blue = w.getPixelColor(w.data.number, w.mouse_position_x, w.mouse_position_y)

        if ( red != w.data.red_selected or
             green != w.data.green_selected or
             blue != w.data.blue_selected):
            w.setPixelColor(
                w.data.number,
                w.mouse_position_x, w.mouse_position_y,
                w.makeColorCode(w.data.red_selected, w.data.green_selected, w.data.blue_selected),
                False)
            w.data.count_pixels_selected += 1
            w.setTitle(f'선택한 픽셀 수: {w.data.count_pixels_selected}')
        

w.initialize = initialize
w.update = update

w.start()
