from random import randint
import os
import sys
import time
import pygame as pg


class Screen:
    def __init__(self, title, wh, bgimg):
        pg.display.set_caption(title) 
        self.sfc = pg.display.set_mode(wh) #(1600, 900)
        self.rct = self.sfc.get_rect()
        self.bgi_sfc = pg.image.load(bgimg) #"fig/pg_bg.jpg"
        self.bgi_rct = self.bgi_sfc.get_rect()
        
    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)


class img:#こうかとん表示
    def __init__(self, img, zoom, xy):
        sfc = pg.image.load(img) # "fig/6.png"
        self.sfc = pg.transform.rotozoom(sfc, 0, zoom) # 2.0
        self.rct = self.sfc.get_rect()
        self.rct.center = xy # 900, 400

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)






#class Mode:
#    def __init__(self,level):
#        self.level = level
#
#    def title(): # level変更機能
#        pg.init() 
#        pg.display
#        screen.fill
#        level = 1
#        while(True):
#            key_states = pg.key.get_pressed()
#            if key_states[pg.K_UP]: level += 1
#            if level == 6: level = 5
#            if key_states[pg.K_DOWN]: level -= 1
#            if level == 0: level = 1
#            
#            if key_states[pg.K_SPACE]:
#                return level




def main():
    scr = Screen("刹那test", (900, 600), "fig/pg_bg.jpg")
    fight = img("fig/cat.png", 0.1, (450, 300))
    tori = img("fig/9.png", 2.0, (700, 450))
    blue_tori = img("fig/bluebird.png", 0.2, (200, 450))
    diley_frame = randint(2500,5000)# ms 2.5秒～5.0秒
    clock = pg.time.Clock()
    flag = 0
    cong_time = 0
    while True:
        scr.blit() # 背景表示
        tori.blit(scr)
        blue_tori.blit(scr)
        if cong_time == 0:
            cong_time = pg.time.get_ticks()
            fight.blit(scr)
            CPU = cong_time + randint(270,300)
            flag = 1 #フラグ1にする
            if pg.time.get_ticks() >= CPU:
                push_time = pg.time.get_ticks()
                print(f"time:{push_time - cong_time}ms" )
                print("CPU WIN") # 敗北用
                #kkt_l.blit(scr)
                time.sleep(1)
                return
        #print (pg.time.get_ticks()) #デバッグ用
        if pg.time.get_ticks() >= diley_frame:
            cong_time = 0
            fight.blit(scr)
            flag = 1 #フラグ1にする
        key_states = pg.key.get_pressed()
        if key_states[pg.K_SPACE]:
            push_time = pg.time.get_ticks()
            if flag == 1:
                fonto = pg.font.Font(None, 80)
                txt = fonto.render(f"time:{push_time - cong_time}ms", True, (0, 0, 0))
                txt2 = fonto.render("1P WIN", True, (0, 0, 0))
                scr.sfc.blit(txt, (30, 250))
                scr.sfc.blit(txt2, (0,0))
                pg.display.update()
                #print(f"time:{push_time - cong_time}ms" ) # 推した瞬間の時間
                print("1P WIN") # 勝利用
                #kkt_w.blit(scr)
                time.sleep(5)
                return
            if flag == 0:
                fonto = pg.font.Font(None, 80)
                txt = fonto.render("not yet", True, (0, 0, 0))
                scr.sfc.blit(txt, (350, 250))
                pg.display.update()
                time.sleep(1)

                return 

        for event in pg.event.get(): 
            if event.type == pg.QUIT:
                return

        pg.display.update()
        clock.tick(1000)
        

        


if __name__ == "__main__":
    pg.init() # 初期化
    main()    # ゲームの本体
    pg.quit() # 初期化の解除
    sys.exit()