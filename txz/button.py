import pygame
#按钮类
class button:
    next_bu = pygame.image.load("img/next.png")
    next_bu_click = pygame.image.load("img/next_click.png")
    last_bu = pygame.image.load("img/last.png")
    last_bu_click = pygame.image.load("img/last_click.png")
    restart_bu = pygame.image.load("img/restart.png")
    restart_bu_click = pygame.image.load("img/restart_click.png")
    guoguan_img = pygame.image.load("img/guoguan.png")
    reback_bu_click = pygame.image.load("img/reback_click.png")

    def __init__(self,window,level):
        self.window = window
        self.level = level
     #按钮贴图
    def display(self):
        self.window.blit(self.restart_bu,(322,182))
        #如果当前关卡不是第一个就贴上一关,否则贴按下的上一关
        if self.level!=1:
            self.window.blit(self.last_bu,(322,122))
        else:
            self.window.blit(self.last_bu_click,(322,122))
        #如果不是最后一关，就贴下一关，否则贴按下的下一关
        if self.level < 10:
            self.window.blit(self.next_bu,(322,62))
        else:
             self.window.blit(self.next_bu_click,(322,62))
    #根据鼠标位置按钮更新贴图
    def upplay(self,pos):
        mouse_x = pos[0]
        mouse_y = pos[1]
        if 322< mouse_x <372:
            if 122 < mouse_y < 155:
                self.window.blit(self.last_bu_click,(322,122))
            elif 182 < mouse_y < 215:
                self.window.blit(self.restart_bu_click,(322,182))
            elif 62 < mouse_y < 95:
                self.window.blit(self.next_bu_click,(322,62))
            elif 242 < mouse_y < 275:
                self.window.blit(self.reback_bu_click,(322,242))