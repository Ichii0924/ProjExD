from random import randint
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


class img():#画像表示
    def __init__(self, img, zoom, xy):
        sfc = pg.image.load(img) 
        self.sfc = pg.transform.rotozoom(sfc, 0, zoom)
        self.rct = self.sfc.get_rect()
        self.rct.center = xy

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)


class Shot:#スペースを押したら
    def __init__(self,file):
        pg.mixer.init() #初期化
        pg.mixer.music.load(file) #読み込み

    def sound(self):#音を鳴らす
        pg.mixer.music.play(1) #再生
        time.sleep(1)
        pg.mixer.music.stop() #終了


def main():
    scr = Screen("刹那test", (700, 600), "fig/yuyake.png")
    fight = img("fig/fight.png", 0.9, (350, 300))
    tori = img("fig/9.png", 2.0, (550, 450))
    blue_tori = img("fig/bluebird.png", 0.2, (170, 450))
    kanban = img("fig/kanban.png", 0.5, (10,0))
    cong_time = 0 
    diley_frame = randint(2500,5000)# ms 2.5秒～5.0秒
    clock = pg.time.Clock()
    flag = 0
    while True:
        scr.blit()
        tori.blit(scr)
        blue_tori.blit(scr)
        #print (pg.time.get_ticks()) #デバッグ用
        if pg.time.get_ticks() >= diley_frame:
            time_sta = time.perf_counter()
            if cong_time == 0:
                cong_time = pg.time.get_ticks() # びっくりの瞬間を保存
            fight.blit(scr)#びっくりを表示
            CPU = cong_time + randint(270,300) # CPU設定
            flag = 1 #フラグ1にする
            if pg.time.get_ticks() >= CPU:
                push_time = pg.time.get_ticks()
                kanban.blit(scr)#時間を表示する看板
                fonto = pg.font.Font(None, 60)
                txt = fonto.render(f"time:{push_time - cong_time}ms", True, (0,0,0))
                txt2 = fonto.render("CPU WIN", True, (0,0,0))
                scr.sfc.blit(txt, (30,250))
                scr.sfc.blit(txt2, (0,35))
                pg.display.update()
                print(f"time:{push_time - cong_time}ms" )
                print("CPU WIN") # 敗北用
                #kkt_l.blit(scr)
                time.sleep(3)
                return
        key_states = pg.key.get_pressed() # キーを検出
        if key_states[pg.K_SPACE]: # スペースキーが検出
            push_time = pg.time.get_ticks()
            if flag == 1: # ちゃんとびっくりの後に押したら
                #勝利時間の画面表示
                fonto = pg.font.Font(None, 60)
                kanban.blit(scr)#時間を表示する看板
                txt = fonto.render(f"time:{push_time - cong_time}ms", True, (0,0,0))
                txt2 = fonto.render("YOU WIN", True, (0,0,0))
                scr.sfc.blit(txt, (30,250))
                scr.sfc.blit(txt2, (0,35))
                pg.display.update()
                #ターミナルに表示(確認用)
                print(f"time:{push_time - cong_time}ms" ) # おした瞬間の時間
                print("1P WIN") # 勝利用
                ds=Shot("fig/stabbing.mp3")
                ds.sound()
                #kkt_w.blit(scr)
                time.sleep(3)
                return
            if flag == 0: # びっくりの前に押したら
                fonto = pg.font.Font("font/ipaexg.ttf", 80)
                txt = fonto.render("おてつき!!!!", True, (0,0,0))
                scr.sfc.blit(txt, (170,250))
                pg.display.update()
                print("1P おてつき!")
                #kkt_u.blit(scr)
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