"""
 Pygame 模板程式
 
"""
# 匯入pygame模組
import random
import pygame
from snake import SnakeBody,Food

# 定義一些會用到的顏色
# 常數使用大寫
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)
        

    

# 初始化pygame
pygame.init()

# 創造一個pygame視窗並設定大小及標題
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("我的遊戲")

# 設定一個開關供迴圈使用
done = False

# 創造一個clock控制畫面更新速度
clock = pygame.time.Clock()
snake = SnakeBody(5, size)
foodGroup = pygame.sprite.Group()

def addfood():
    x = random.randrange(size[0])
    y = random.randrange(size[1])
    x -= x % 20
    y -= y % 20
    food = Food(WHITE, x, y)
    
    foodGroup.add(food)

for _ in range(5):
    addfood()
# -------- 主要的程式迴圈 -----------
while not done:
    # --- 事件迴圈 event loop
    for event in pygame.event.get(): # 從事件list中抓取事件
        if event.type == pygame.QUIT: # 當使用者按下結束
            done = True # 將done變數設為True-->while迴圈將會結束
            
    
    # --- 程式的運算與邏輯
    pressed = pygame.key.get_pressed()
    snake.move(pressed)
    
    if snake.isOutOfRange() or snake.collideSelf():
        done = True 
    
    if len(foodGroup) < 10:
        addfood()
    snake.Eating(foodGroup)   

    

    
    # --- 繪圖的程式碼
    #       先將畫面塗滿底色(將原有畫面清掉)
    #       繪圖的程式要寫在這行後面，不然會被這行清掉9
    screen.fill(BLACK)
    snake.group.draw(screen)
    foodGroup.draw(screen)
    #sprite.draw(screen)
    # --- 更新畫面
    pygame.display.flip()

    # --- 每秒鐘60個frame
    clock.tick(10)

# 關閉式窗並離開程式w
pygame.quit()
exit()
