
import pygame as pg
import sys
from random import randint
import time

def check_bound(obj_rect, scr_rect): #obj_rectはこうかとんrectまたは爆弾_rect,scr_rectはスクリーンrect

    yoko, tate = +1, +1
    if obj_rect.left < scr_rect.left or scr_rect.right < obj_rect.right:
        yoko = -1
    if obj_rect.top < scr_rect.top or scr_rect.bottom < obj_rect.bottom:
        tate = -1
        
    return yoko, tate


def main():
    # 練習1
    pg.display.set_caption("逃げろ！こうかとん")
    scrn_sfc = pg.display.set_mode((1600, 900))
    scrn_rect = scrn_sfc.get_rect()
    bg_sfc = pg.image.load("fig/pg_bg.jpg")
    bg_rct = bg_sfc.get_rect()

    #練習3
    tori_sfc = pg.image.load("fig/tracer.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 0.5)
    tori_rect = tori_sfc.get_rect()
    tori_rect.center = 900, 400

    #練習5
    bomb_sfc = pg.Surface((20,20))
    bomb_sfc.set_colorkey((0,0,0))
    pg.draw.circle(bomb_sfc, (255,0,0), (10,10), 10)#円を書く
    bomb_rect = bomb_sfc.get_rect()
    bomb_rect.centerx = randint(0, scrn_rect.width)
    bomb_rect.centery = randint(0, scrn_rect.height)
    
    #爆弾２個目
    second_bomb_sfc = pg.Surface((20,20))
    second_bomb_sfc.set_colorkey((0,0,0))
    pg.draw.circle(second_bomb_sfc, (255,0,0), (10,10), 10)
    second_bomb_rect = second_bomb_sfc.get_rect()
    second_bomb_rect.centerx = randint(0, scrn_rect.width)
    second_bomb_rect.centery = randint(0, scrn_rect.height)

    #爆弾３つ目
    third_bomb_sfc = pg.Surface((20,20))
    third_bomb_sfc.set_colorkey((0,0,0))
    pg.draw.circle(third_bomb_sfc, (255,0,0), (10,10), 10)
    third_bomb_rect = third_bomb_sfc.get_rect()
    third_bomb_rect.centerx = randint(0, scrn_rect.width)
    third_bomb_rect.centery = randint(0, scrn_rect.height)



    #練習6
    vx, vy = +1.5, +1.5
    s_vx, s_vy = -1.5, -1.5
    t_vx, t_vy = +1.5, -1.5


    clock = pg.time.Clock() # 練習1
    while True:
        scrn_sfc.blit(bg_sfc, bg_rct) # 練習2
        for event in pg.event.get(): # 練習2
            if event.type == pg.QUIT:
                return

        key_statas = pg.key.get_pressed()
        if key_statas[pg.K_UP] or key_statas[pg.K_w]: 
            tori_rect.centery -= 1 #こうかとんの縦座標を+1
        if key_statas[pg.K_DOWN] or key_statas[pg.K_s]:
            tori_rect.centery += 1
        if key_statas[pg.K_LEFT] or key_statas[pg.K_a]:
            tori_rect.centerx -= 1
        if key_statas[pg.K_RIGHT] or key_statas[pg.K_d]:    
            tori_rect.centerx += 1

        #ブリンク
        if key_statas[pg.K_UP] and key_statas[pg.K_e]: 
            tori_rect.centery -= 2 
        if key_statas[pg.K_DOWN] and key_statas[pg.K_e]:
            tori_rect.centery += 2
        if key_statas[pg.K_LEFT] and key_statas[pg.K_e]:
            tori_rect.centerx -= 2
        if key_statas[pg.K_RIGHT] and key_statas[pg.K_e]:    
            tori_rect.centerx += 2

        yoko, tate = check_bound(tori_rect, scrn_rect)
        if yoko == -1 :
            if key_statas[pg.K_LEFT]:
                tori_rect.centerx += 1
            if key_statas[pg.K_RIGHT]:
                tori_rect.centerx -= 1
        if tate == -1 :
            if key_statas[pg.K_UP]:
                tori_rect.centery += 1
            if key_statas[pg.K_DOWN]:
                tori_rect.centery -= 1
        scrn_sfc.blit(tori_sfc, tori_rect)

        yoko, tate = check_bound(bomb_rect, scrn_rect)
        vx *= yoko
        vy *= tate
        yoko, tate = check_bound(second_bomb_rect, scrn_rect)
        s_vx *= yoko
        s_vy *= tate
        yoko, tate = check_bound(third_bomb_rect, scrn_rect)
        t_vx *= yoko
        t_vy *= tate

        bomb_rect.move_ip(vx, vy)
        second_bomb_rect.move_ip(s_vx, s_vy)
        third_bomb_rect.move_ip(t_vx, t_vy)
        scrn_sfc.blit(bomb_sfc, bomb_rect)
        scrn_sfc.blit(second_bomb_sfc, second_bomb_rect)
        scrn_sfc.blit(third_bomb_sfc, third_bomb_rect)

        #練習8
        if tori_rect.colliderect(bomb_rect) or tori_rect.colliderect(second_bomb_rect) or tori_rect.colliderect(third_bomb_rect):
            fonto = pg.font.Font(None, 80)
            txt = fonto.render("you so bad", True, (0, 0, 0))
            scrn_sfc.blit(txt, (tori_rect.centerx-140, tori_rect.centery-110))
            pg.display.update()
            time.sleep(1)
            return
            

        pg.display.update()#練習2
        clock.tick(1000)


   


if __name__ == "__main__":
    pg.init() # 初期化
    main() # ゲームの本体
    pg.quit() # 初期化の解除
    sys.exit()