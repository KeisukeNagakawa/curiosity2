# -*- coding: utf-8 -*-
import time
import RPi.GPIO as G


# 左右モータのピン設定
RPHASE=19
RENABL=21
LPHASE=23
LENABL=22


class PWM:
    # Pulse Width Modulation
    def __init__(self):
        # すべての初期設定
        G.setwarnings(False)
        G.setmode(G.BOARD)
        G.setup(RPHASE, G.OUT)
        G.setup(RENABL, G.OUT)
        G.setup(LPHASE, G.OUT)
        G.setup(LENABL, G.OUT)

        # PWM制御用チャンネル
        # 右
        self.right_pwm = G.PWM(RPHASE, 100)
        self.right_pwm.start(0)
        self.right_pwm.ChangeDutyCycle(0)
        # 左
        self.left_pwm = G.PWM(LPHASE, 100)
        self.left_pwm.start(0)
        self.left_pwm.ChangeDutyCycle(0)

    def __del__(self):
        G.output(RPHASE, 0)
        G.output(RENABL, 0)
        G.output(LPHASE, 0)
        G.output(LENABL, 0)
        self.right_pwm.stop()
        self.left_pwm.stop()
        G.cleanup()

    def cdc(self, x, LorR):
        print('cdc function is called')
        if LorR=='R':
            if x>=0:
                G.output(RENABL, 0)
                self.right_pwm.ChangeDutyCycle(x)
            else:
                G.output(RENABL, 1)
                # xはマイナスであることに注意
                self.right_pwm.ChangeDutyCycle(100+x)
        else :
            if x>=0:
                G.output(LENABL, 0)
                self.left_pwm.ChangeDutyCycle(x)
            else:
                G.output(LENABL, 1)
                # xはマイナスであることに注意
                self.left_pwm.ChangeDutyCycle(100+x)







