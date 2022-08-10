import cv2
# Import LCD library
from RPLCD import i2c

# Import sleep library
from time import sleep

# constants to initialise the LCD
lcdmode = 'i2c'
cols = 20
rows = 4
charmap = 'A00'
i2c_expander = 'PCF8574'

# Generally 27 is the address;Find yours using: i2cdetect -y 1
address = 0x27
port = 1  # 0 on an older Raspberry Pi

# Initialise the LCD
lcd = i2c.CharLCD(i2c_expander, address, port=port, charmap=charmap,
                  cols=cols, rows=rows)


input_video_path = '4032.mp4'

cap = cv2.VideoCapture(input_video_path)

length = int(cap. get(cv2. CAP_PROP_FRAME_COUNT))
print(length)

frmn = 1

nowblock = 1

while (cap.isOpened()):
    ret, frame = cap.read()
    print(frmn)

    if ret:

        # cv2.imshow("frame", frame)
        # cv2.waitKey(1)

        # for x in range(0, 31):
        #     for y in range(0, 99):
        #         if frame[x, y, 0] > 100 and frame[x, y, 1] > 100 and frame[x, y, 2] > 100:
        #             print(1, end="")
        #         else:
        #             print(0, end="")

        #     print()
        # print("------------------------------")

        block = []  # 1 full block
        temp = []  # 1 block row

        for x in range(0, 32, 8):
            for y in range(0, 40, 5):
                block = block = [
                    [not (frame[x+0, y+0, 0] > 100 and frame[x+0, y+0, 1] > 100 and frame[x+0, y+0, 2] > 100), not (frame[x+0, y+1, 0] > 100 and frame[x+0, y+1, 1] > 100 and frame[x+0, y+1, 2] > 100), not (frame[x+0, y+2, 0] > 100 and frame[x+0,
                                                                                                                                                                                                                                                 y+2, 1] > 100 and frame[x+0, y+2, 2] > 100), not (frame[x+0, y+3, 0] > 100 and frame[x+0, y+3, 1] > 100 and frame[x+0, y+3, 2] > 100), not (frame[x+0, y+4, 0] > 100 and frame[x+0, y+4, 1] > 100 and frame[x+0, y+4, 2] > 100)],
                    [not (frame[x+1, y+0, 0] > 100 and frame[x+1, y+0, 1] > 100 and frame[x+1, y+0, 2] > 100), not (frame[x+1, y+1, 0] > 100 and frame[x+1, y+1, 1] > 100 and frame[x+1, y+1, 2] > 100), not (frame[x+1, y+2, 0] > 100 and frame[x+1,
                                                                                                                                                                                                                                                 y+2, 1] > 100 and frame[x+1, y+2, 2] > 100), not (frame[x+1, y+3, 0] > 100 and frame[x+1, y+3, 1] > 100 and frame[x+1, y+3, 2] > 100), not (frame[x+1, y+4, 0] > 100 and frame[x+1, y+4, 1] > 100 and frame[x+1, y+4, 2] > 100)],
                    [not (frame[x+2, y+0, 0] > 100 and frame[x+2, y+0, 1] > 100 and frame[x+2, y+0, 2] > 100), not (frame[x+2, y+1, 0] > 100 and frame[x+2, y+1, 1] > 100 and frame[x+2, y+1, 2] > 100), not (frame[x+2, y+2, 0] > 100 and frame[x+2,
                                                                                                                                                                                                                                                 y+2, 1] > 100 and frame[x+2, y+2, 2] > 100), not (frame[x+2, y+3, 0] > 100 and frame[x+2, y+3, 1] > 100 and frame[x+2, y+3, 2] > 100), not (frame[x+2, y+4, 0] > 100 and frame[x+2, y+4, 1] > 100 and frame[x+2, y+4, 2] > 100)],
                    [not (frame[x+3, y+0, 0] > 100 and frame[x+3, y+0, 1] > 100 and frame[x+3, y+0, 2] > 100), not (frame[x+3, y+1, 0] > 100 and frame[x+3, y+1, 1] > 100 and frame[x+3, y+1, 2] > 100), not (frame[x+3, y+2, 0] > 100 and frame[x+3,
                                                                                                                                                                                                                                                 y+2, 1] > 100 and frame[x+3, y+2, 2] > 100), not (frame[x+3, y+3, 0] > 100 and frame[x+3, y+3, 1] > 100 and frame[x+3, y+3, 2] > 100), not (frame[x+3, y+4, 0] > 100 and frame[x+3, y+4, 1] > 100 and frame[x+3, y+4, 2] > 100)],
                    [not (frame[x+4, y+0, 0] > 100 and frame[x+4, y+0, 1] > 100 and frame[x+4, y+0, 2] > 100), not (frame[x+4, y+1, 0] > 100 and frame[x+4, y+1, 1] > 100 and frame[x+4, y+1, 2] > 100), not (frame[x+4, y+2, 0] > 100 and frame[x+4,
                                                                                                                                                                                                                                                 y+2, 1] > 100 and frame[x+4, y+2, 2] > 100), not (frame[x+4, y+3, 0] > 100 and frame[x+4, y+3, 1] > 100 and frame[x+4, y+3, 2] > 100), not (frame[x+4, y+4, 0] > 100 and frame[x+4, y+4, 1] > 100 and frame[x+4, y+4, 2] > 100)],
                    [not (frame[x+5, y+0, 0] > 100 and frame[x+5, y+0, 1] > 100 and frame[x+5, y+0, 2] > 100), not (frame[x+5, y+1, 0] > 100 and frame[x+5, y+1, 1] > 100 and frame[x+5, y+1, 2] > 100), not (frame[x+5, y+2, 0] > 100 and frame[x+5,
                                                                                                                                                                                                                                                 y+2, 1] > 100 and frame[x+5, y+2, 2] > 100), not (frame[x+5, y+3, 0] > 100 and frame[x+5, y+3, 1] > 100 and frame[x+5, y+3, 2] > 100), not (frame[x+5, y+4, 0] > 100 and frame[x+5, y+4, 1] > 100 and frame[x+5, y+4, 2] > 100)],
                    [not (frame[x+6, y+0, 0] > 100 and frame[x+6, y+0, 1] > 100 and frame[x+6, y+0, 2] > 100), not (frame[x+6, y+1, 0] > 100 and frame[x+6, y+1, 1] > 100 and frame[x+6, y+1, 2] > 100), not (frame[x+6, y+2, 0] > 100 and frame[x+6,
                                                                                                                                                                                                                                                 y+2, 1] > 100 and frame[x+6, y+2, 2] > 100), not (frame[x+6, y+3, 0] > 100 and frame[x+6, y+3, 1] > 100 and frame[x+6, y+3, 2] > 100), not (frame[x+6, y+4, 0] > 100 and frame[x+6, y+4, 1] > 100 and frame[x+6, y+4, 2] > 100)],
                    [not (frame[x+7, y+0, 0] > 100 and frame[x+7, y+0, 1] > 100 and frame[x+7, y+0, 2] > 100), not (frame[x+7, y+1, 0] > 100 and frame[x+7, y+1, 1] > 100 and frame[x+7, y+1, 2] > 100), not (frame[x+7, y+2, 0] > 100 and frame[x+7,
                                                                                                                                                                                                                                                 y+2, 1] > 100 and frame[x+7, y+2, 2] > 100), not (frame[x+7, y+3, 0] > 100 and frame[x+7, y+3, 1] > 100 and frame[x+7, y+3, 2] > 100), not (frame[x+7, y+4, 0] > 100 and frame[x+7, y+4, 1] > 100 and frame[x+7, y+4, 2] > 100)]

                ]
                printblock = ()

                for i in range(0, 8):
                    res = 0
                    for ele in block[i]:
                        res = (res << 1) | ele
                    block[i] = int(str(res))

                if nowblock == 9:
                    nowblock = 1

                    lcd.clear()

                if nowblock == 1:
                    lcd.create_char(0, tuple(block))
                    lcd.cursor_pos = (((x+1)//8), ((y+1)//5))
                    lcd.write_string("\x00")
                elif nowblock == 2:
                    lcd.create_char(1, tuple(block))
                    lcd.cursor_pos = (((x+1)//8), ((y+1)//5))
                    lcd.write_string("\x01")
                elif nowblock == 3:
                    lcd.create_char(2, tuple(block))
                    lcd.cursor_pos = (((x+1)//8), ((y+1)//5))
                    lcd.write_string("\x02")
                elif nowblock == 4:
                    lcd.create_char(3, tuple(block))
                    lcd.cursor_pos = (((x+1)//8), ((y+1)//5))
                    lcd.write_string("\x03")
                elif nowblock == 5:
                    lcd.create_char(4, tuple(block))
                    lcd.cursor_pos = (((x+1)//8), ((y+1)//5))
                    lcd.write_string("\x04")
                elif nowblock == 6:
                    lcd.create_char(5, tuple(block))
                    lcd.cursor_pos = (((x+1)//8), ((y+1)//5))
                    lcd.write_string("\x05")
                elif nowblock == 7:
                    lcd.create_char(6, tuple(block))
                    lcd.cursor_pos = (((x+1)//8), ((y+1)//5))
                    lcd.write_string("\x06")
                elif nowblock == 8:
                    lcd.create_char(7, tuple(block))
                    lcd.cursor_pos = (((x+1)//8), ((y+1)//5))
                    lcd.write_string("\x07")
                nowblock += 1

    else:
        break

    frmn += 1


cap.release()
cv2.destroyAllWindows()
