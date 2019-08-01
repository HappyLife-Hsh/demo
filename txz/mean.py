import sys
import pygame
#导入我写的类
from all_project.txz.leavel import lev
from all_project.txz.hero import  hero
from all_project.txz.button import button

#设置窗体高和宽
window_height = 300
window_width = 400
#初始化pygame
pygame.init()
#加载撤销的图片
reback_bu = pygame.image.load("img/reback.png")
reback_bu_click = pygame.image.load("img/reback_click.png")
#创建窗口,,,,set_mode((尺寸 宽*高))
window = pygame.display.set_mode((window_width,window_height))
#设置标题
pygame.display.set_caption('推箱子')
#窗口填充颜色
window.fill((12,95,53))
#创建文字提示的字体
font =  pygame.font.Font("./font/simkai.ttf",18)
#游戏主函数
def main():
    #设立关卡
    level = lev(1,window)
    #游戏关卡贴图 #记录正确点的位置
    li = level.display()
    #创建英雄
    person = hero(lev.person,lev.person_coss,lev.blank,lev.box_right,level.get_person(),li,window)
    #状态标识（判断是过关状态True还是游戏状态False）
    card = False
    #显示文字
    dis_font()
    #按钮贴图
    but = button(window,level.level)
    but.display()
    dis_back()
    while True:
        #窗口更新
        pygame.display.update()
        #判断过关
        if level.istrue(li):
            if not card:
                window.blit(button.guoguan_img,(30,90))
                window.blit(button.next_bu,(180,160))
                window.blit(button.restart_bu,(75,160))
                card = True
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    pygame.quit()
                elif event.type == pygame.MOUSEMOTION:
                    window.blit(button.next_bu,(180,160))
                    window.blit(button.restart_bu,(75,160))
                    pos = pygame.mouse.get_pos()
                    mouse_x = pos[0]
                    mouse_y = pos[1]
                    if 160< mouse_y <195:
                        if 75 < mouse_x < 130:
                            window.blit(button.restart_bu_click,(75,160))
                        elif 180 < mouse_x < 235:
                            window.blit(button.next_bu_click,(180,160))
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos_click = pygame.mouse.get_pos()
                    mouse_x = pos_click[0]
                    mouse_y = pos_click[1]
                    if 160< mouse_y <195:
                        if 75 < mouse_x < 130:
                            level = lev(level.level,window)
                            window.fill((12,95,53))
                            li=level.display()
                            person = hero(lev.person,lev.person_coss,lev.blank,lev.box_right,level.get_person(),li,window)
                            card = False
                            dis_font(level.level)
                            but = button(window,level.level)
                            but.display()
                            dis_back()
                        elif 180 < mouse_x < 235:
                            if level.level < 10:
                                level = lev(level.level+1,window)
                                window.fill((12,95,53))
                                li=level.display()
                                person = hero(lev.person,lev.person_coss,lev.blank,lev.box_right,level.get_person(),li,window)
                                card = False
                                dis_font(level.level)
                                but = button(window,level.level)
                                but.display()
                                dis_back()
        else:
            #捕获事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    pygame.quit()
                #按键事件
                elif event.type ==pygame.KEYDOWN:
                    if event.key ==pygame.K_LEFT or event.key ==pygame.K_a:
                        o_j = level.operate(person.x,person.y,3,li)
                        if o_j==1:
                            person.move_left()
                        elif o_j==2:
                            box_move(3,person.x-1,person.y,lev.box,lev.box_right,li)
                            person.move_left()
                    elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        o_j = level.operate(person.x,person.y,4,li)
                        if o_j==1:
                            person.move_right()
                        elif o_j==2:
                            box_move(4,person.x+1,person.y,lev.box,lev.box_right,li)
                            person.move_right()
                    elif event.key == pygame.K_UP or event.key == pygame.K_w:
                        o_j = level.operate(person.x,person.y,1,li)
                        if o_j==1:
                            person.move_up()
                        elif o_j==2:
                            box_move(1,person.x,person.y-1,lev.box,lev.box_right,li)
                            person.move_up()
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        o_j = level.operate(person.x,person.y,2,li)
                        if o_j==1:
                            person.move_down()
                        elif o_j==2:
                            box_move(2,person.x,person.y+1,lev.box,lev.box_right,li)
                            person.move_down()
                    #撤销按钮贴图
                    dis_back(level.que.is_empty())
                #鼠标移动事件
                elif event.type == pygame.MOUSEMOTION:
                    but.display()
                    dis_back(level.que.is_empty())
                    #获取鼠标当前坐标
                    pos = pygame.mouse.get_pos()
                    but.upplay(pos)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                     #获取点击鼠标当前坐标
                    pos_click = pygame.mouse.get_pos()
                    mouse_x = pos_click[0]
                    mouse_y = pos_click[1]
                    if 322< mouse_x <372:
                        if 122 < mouse_y < 155:
                            if level.level != 1:
                                level = lev(level.level-1,window)
                                window.fill((12,95,53))
                                li=level.display()
                                person = hero(lev.person,lev.person_coss,lev.blank,lev.box_right,level.get_person(),li,window)
                                card = False
                                dis_font(level.level)
                                but = button(window,level.level)
                                but.display()
                                dis_back()
                        elif 62 < mouse_y < 95:
                            if level.level < 10:
                                level = lev(level.level+1,window)
                                window.fill((12,95,53))
                                li=level.display()
                                person = hero(lev.person,lev.person_coss,lev.blank,lev.box_right,level.get_person(),li,window)
                                card = False
                                dis_font(level.level)
                                but = button(window,level.level)
                                but.display()
                                dis_back()
                        elif 182 < mouse_y < 215:
                            level = lev(level.level,window)
                            window.fill((12,95,53))
                            li=level.display()
                            person = hero(lev.person,lev.person_coss,lev.blank,lev.box_right,level.get_person(),li,window)
                            card = False
                            dis_font(level.level)
                            but = button(window,level.level)
                            but.display()
                            dis_back()
                        elif 242 < mouse_y < 375:
                            re_li = level.que.remove()
                            if re_li != None:
                                window.fill((12,95,53))
                                level.li = re_li
                                level.display()
                                dis_font(level.level)
                                tut = level.get_person()
                                person.x = tut[0]
                                person.y = tut[1]
                                but.display()
                                dis_back()




#箱子移动
def box_move(f,x,y,b_img,r_img,li):
    if f == 1:
        window.blit(b_img,((x+1)*30,y*30))
        if (x,y-1) in li:
            window.blit(r_img,((x+1)*30,y*30))
    elif f == 2:
        window.blit(b_img,((x+1)*30,(y+2)*30))
        if (x,y+1) in li:
            window.blit(r_img,((x+1)*30,(y+2)*30))
    elif f == 3:
        window.blit(b_img,(x*30,(y+1)*30))
        if (x-1,y) in li:
            window.blit(r_img,(x*30,(y+1)*30))
    elif f == 4:
        window.blit(b_img,((x+2)*30,(y+1)*30))
        if (x+1,y) in li:
            window.blit(r_img,((x+2)*30,(y+1)*30))
#撤销功能贴图
def dis_back(b = True):
    if b:
        window.blit(reback_bu_click,(322,242))
    else :
        window.blit(reback_bu,(322,242))
#提示显示当前关卡
def dis_font(l=1):
    string = "当前是第"+str(l)+"关"
    text = font.render(string,False,(234,244,67))
    window.blit(text,(295,25))
 #窗口鼠标监控函数
def mouse():
    pass
#测试代码，打印矩阵
def da(li):
     for x in range(len(li)):
         for y in range(len(li[x])):
             print(li[x][y],end=',')
         print()

if __name__ == '__main__':
    main()
