class hero:
    def __init__(self,p_img,p_c_img,b_img,r_img,t,r,window):
        self.p_img = p_img #人的图片
        self.b_img = b_img #空白地接图
        self.p_c_img = p_c_img #人经过的正确点贴图
        self.r_img = r_img #正确点的贴图
        self.x = t[0]
        self.y = t[1]
        self.r = r
        self.window = window
    def move_left(self):
        self.x -=1
        if (self.x,self.y) in self.r:
            self.window.blit(self.p_c_img,((self.x+1)*30,(self.y+1)*30))
        else:
            self.window.blit(self.p_img,((self.x+1)*30,(self.y+1)*30))
        self.window.blit(self.b_img,((self.x+2)*30,(self.y+1)*30))
        if (self.x+1,self.y) in self.r:
            self.window.blit(self.r_img,((self.x+2)*30,(self.y+1)*30))


    def move_right(self):
        self.x +=1
        if (self.x,self.y) in self.r:
            self.window.blit(self.p_c_img,((self.x+1)*30,(self.y+1)*30))
        else:
            self.window.blit(self.p_img,((self.x+1)*30,(self.y+1)*30))
        self.window.blit(self.b_img,(self.x*30,(self.y+1)*30))
        if (self.x-1,self.y) in self.r:
            self.window.blit(self.r_img,(self.x*30,(self.y+1)*30))

    def move_up(self):
        self.y -=1
        if (self.x,self.y) in self.r:
            self.window.blit(self.p_c_img,((self.x+1)*30,(self.y+1)*30))
        else:
            self.window.blit(self.p_img,((self.x+1)*30,(self.y+1)*30))
        self.window.blit(self.b_img,((self.x+1)*30,(self.y+2)*30))
        if (self.x,self.y+1) in self.r:
            self.window.blit(self.r_img,((self.x+1)*30,(self.y+2)*30))

    def move_down(self):
        self.y +=1
        if (self.x,self.y) in self.r:
            self.window.blit(self.p_c_img,((self.x+1)*30,(self.y+1)*30))
        else:
            self.window.blit(self.p_img,((self.x+1)*30,(self.y+1)*30))
        self.window.blit(self.b_img,((self.x+1)*30,self.y*30))
        if (self.x,self.y-1) in self.r:
            self.window.blit(self.r_img,((self.x+1)*30,self.y*30))


