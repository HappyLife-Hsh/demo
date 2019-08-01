import copy

import pygame

from all_project.txz.back_queue import back_queue


#关卡
class lev:
    #关卡字典
    dit = {
            1:[
                [9,9,1,1,1,9,9,9],
                [9,9,1,4,1,9,9,9],
                [9,9,1,0,1,1,1,1],
                [1,1,1,2,0,2,4,1],
                [1,4,0,2,3,1,1,1],
                [1,1,1,1,2,1,9,9],
                [9,9,9,1,4,1,9,9],
                [9,9,9,1,1,1,9,9]
            ],
        2:[
            [9,9,1,1,1,1,9,9],
            [9,9,1,4,4,1,9,9],
            [9,1,1,0,4,1,1,9],
            [9,1,0,0,2,4,1,9],
            [1,1,0,2,3,0,1,1],
            [1,0,0,1,2,2,0,1],
            [1,0,0,0,0,0,0,1],
            [1,1,1,1,1,1,1,1]
        ],
        3:[
            [9,9,1,1,1,1,9,9],
            [9,1,1,0,0,1,9,9],
            [9,1,3,2,0,1,9,9],
            [9,1,1,2,0,1,1,9],
            [9,1,1,0,2,0,1,9],
            [9,1,4,2,0,0,1,9],
            [9,1,4,4,6,4,1,9],
            [9,1,1,1,1,1,1,9]

        ],
        4:[

            [1,1,1,1,1,9,9,9,9],
            [1,0,0,0,1,1,1,1,1],
            [1,2,1,0,1,0,0,0,1],
            [1,0,0,0,0,0,2,0,1],
            [1,4,5,1,2,1,2,1,1],
            [1,4,2,0,0,0,0,1,9],
            [1,4,4,0,0,1,1,1,9],
            [1,1,1,1,1,1,9,9,9]

        ],

        5:[
            [9,1,1,1,1,1,9,9],
            [9,1,4,0,0,1,9,9],
            [9,1,0,1,2,1,9,9],
            [9,1,0,0,0,1,9,9],
            [9,1,0,1,0,1,1,1],
            [9,1,4,0,2,0,0,1],
            [9,1,0,0,5,2,0,1],
            [9,1,1,1,1,1,1,1]
        ],

        6:[
            [9,1,1,1,1,1,1,9,9],
            [9,1,0,0,0,0,1,1,9],
            [1,1,4,1,1,0,0,1,9],
            [1,0,6,5,0,0,0,1,9],
            [1,0,0,1,2,2,0,1,9],
            [1,0,0,0,0,1,1,1,9],
            [1,1,1,1,1,1,9,9,9],
            [9,9,9,9,9,9,9,9,9]

        ],
        7:[
            [9,1,1,1,1,1,9,9,9],
            [9,1,0,3,0,1,1,1,9],
            [1,1,0,1,2,0,0,1,9],
            [1,0,6,4,0,4,0,1,9],
            [1,0,0,2,2,0,1,1,9],
            [1,1,1,0,1,4,1,9,9],
            [9,9,1,0,0,0,1,9,9],
            [9,9,1,1,1,1,1,9,9]

        ],
        8:[
            [1,1,1,1,1,1,1,9],
            [1,4,4,2,4,4,1,9],
            [1,4,4,1,4,4,1,9],
            [1,0,2,2,2,0,1,9],
            [1,0,0,2,0,0,1,9],
            [1,0,2,2,2,0,1,9],
            [1,0,0,1,3,0,1,9],
            [1,1,1,1,1,1,1,9]


        ],
        9:[
            [1,1,1,1,1,1,9,9],
            [1,0,0,0,0,1,9,9],
            [1,0,4,6,0,1,1,1],
            [1,0,4,2,4,2,0,1],
            [1,1,0,2,0,0,0,1],
            [9,1,1,1,1,0,3,1],
            [9,9,9,9,1,1,1,1],
            [9,9,9,9,9,9,9,9]
        ],
        10:[
            [9,9,1,1,1,1,1,9,9],
            [9,1,1,0,3,0,1,1,9],
            [9,1,0,0,6,2,0,1,9],
            [9,1,2,0,4,0,2,1,9],
            [9,1,4,4,1,4,4,1,9],
            [1,1,2,0,6,0,0,1,1],
            [1,0,2,0,1,0,2,0,1],
            [1,0,0,0,1,0,0,0,1],
            [1,1,1,1,1,1,1,1,1]
        ]
    }
    #关卡图
    block = pygame.image.load("img/block.png")
    box = pygame.image.load("img/box.png")
    blank = pygame.image.load("img/blank.png")
    box_right = pygame.image.load("img/box_right.png")
    person = pygame.image.load("img/person.png")
    box_coss = pygame.image.load("img/box_coss.png")
    person_coss = pygame.image.load("img/person_coss.png")
    def __init__(self,level,window):
        self.window = window
        self.level = level
        self.li = copy.deepcopy(lev.dit[self.level])
        #创建队列，记录撤销
        self.que = back_queue()
    #贴图字典
    @classmethod
    def p_dict(cls):
        dic = {
            1:cls.block,0:cls.blank,2:cls.box,3:cls.person,4:cls.box_right,
            5:cls.person_coss,6:cls.box_coss}
        return dic
    #得到人对象的x和y值
    def get_person(self):
        for y in range(len(self.li)):
            for x in range(len(self.li[y])):
                if self.li[y][x]==3 or self.li[y][x]==5:
                    return (x,y)
    #关卡贴图
    def display(self):
        dic = lev.p_dict()
        #记录下正确的点的列表
        li = list()
        for y in range(len(self.li)):
            for x in range(len(self.li[y])):
               # print(self.li[y][x],end=',')
               if self.li[y][x]==4:
                   li.append((x,y))
                   self.window.blit(self.blank,(30*(x+1),30*(y+1)))
                   self.window.blit(dic[4],(30*(x+1),30*(y+1)))
               elif self.li[y][x]!=9:
                   if self.li[y][x]==6 or self.li[y][x]==5:
                       li.append((x,y))
                   self.window.blit(dic[self.li[y][x]],(30*(x+1),30*(y+1)))
            # print()
        return li
    #矩阵操作维护
    def operate(self,y,x,f,tu):
        if f == 1:
           if (self.li[x-1][y]==2 or self.li[x-1][y]==6) and x>1 and (self.li[x-2][y] == 0 or self.li[x-2][y]==4):
               self.que.add(copy.deepcopy(self.li))
               if (y,x) in tu:
                   self.li[x][y]=4
               else:self.li[x][y]=0
               if (y,x-1) in tu:
                   self.li[x-1][y]=5
               else:self.li[x-1][y]=3
               if (y,x-2) in tu:
                   self.li[x-2][y]=6
               else:self.li[x-2][y]=2
               return 2
           elif self.li[x-1][y] == 0 or self.li[x-1][y] == 4:
               self.que.add(copy.deepcopy(self.li))
               if (y,x) in tu:
                   self.li[x][y]=4
               else:self.li[x][y]=0
               if (y,x-1) in tu:
                   self.li[x-1][y]=5
               else:self.li[x-1][y]=3
               return 1
        elif f == 2:
           if (self.li[x+1][y]==2 or self.li[x+1][y]==6) and x<6 and (self.li[x+2][y] == 0 or self.li[x+2][y]==4):
               self.que.add(copy.deepcopy(self.li))
               if (y,x) in tu:
                   self.li[x][y]=4
               else:self.li[x][y]=0
               if (y,x+1) in tu:
                   self.li[x+1][y]=5
               else:self.li[x+1][y]=3
               if (y,x+2) in tu:
                   self.li[x+2][y]=6
               else:self.li[x+2][y]=2
               return 2
           elif self.li[x+1][y] == 0 or self.li[x+1][y] == 4:
               self.que.add(copy.deepcopy(self.li))
               if (y,x) in tu:
                   self.li[x][y]=4
               else:self.li[x][y]=0
               if (y,x+1) in tu:
                   self.li[x+1][y]=5
               else:self.li[x+1][y]=3
               return 1
        if f == 3:
           if (self.li[x][y-1]==2 or self.li[x][y-1]==6) and y>1 and (self.li[x][y-2] == 0 or self.li[x][y-2]==4):
               self.que.add(copy.deepcopy(self.li))
               if (y,x) in tu:
                   self.li[x][y]=4
               else:self.li[x][y]=0
               if (y-1,x) in tu:
                   self.li[x][y-1]=5
               else:self.li[x][y-1]=3
               if (y-2,x) in tu:
                   self.li[x][y-2]=6
               else:self.li[x][y-2]=2
               return 2
           elif self.li[x][y-1] == 0 or self.li[x][y-1] == 4:
               self.que.add(copy.deepcopy(self.li))
               if (y,x) in tu:
                   self.li[x][y]=4
               else:self.li[x][y]=0
               if (y-1,x) in tu:
                   self.li[x][y-1]=5
               else:self.li[x][y-1]=3
               return 1
        elif f == 4:
           if (self.li[x][y+1]==2 or self.li[x][y+1]==6) and y<6 and (self.li[x][y+2] == 0 or self.li[x][y+2]==4):
               self.que.add(copy.deepcopy(self.li))
               if (y,x) in tu:
                   self.li[x][y]=4
               else:self.li[x][y]=0
               if (y+1,x) in tu:
                   self.li[x][y+1]=5
               else:self.li[x][y+1]=3
               if (y+2,x) in tu:
                   self.li[x][y+2]=6
               else:self.li[x][y+2]=2
               return 2
           elif self.li[x][y+1] == 0 or self.li[x][y+1] == 4:
               self.que.add(copy.deepcopy(self.li))
               if (y,x) in tu:
                   self.li[x][y]=4
               else:self.li[x][y]=0
               if (y+1,x) in tu:
                   self.li[x][y+1]=5
               else:self.li[x][y+1]=3
               return 1
    #判断是否过关
    def istrue(self,li):
        for i in li:
            if self.li[i[1]][i[0]] != 6:
                return False
        return True











