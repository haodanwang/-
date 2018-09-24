import pygame
import  sys
import  time
import  random
from pygame.locals import  *


#初始化pygame
pygame.init()
fpsClock=pygame.time.Clock()

#创建pygame显示层
playSurface=pygame.display.set_mode((640,480))
#定义标题
pygame.display.set_caption('Snake go!')
#加载资源图片,game.ico包含在最后的文件里面
image=pygame.image.load('game.ico')
pygame.display.set_icon(image)
