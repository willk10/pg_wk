import pyautogui as pg
import time

pg.hotkey('ctrl', 'winleft', 'd')
pg.hotkey('winleft')
pg.typewrite('chrome\n', .4)
time.sleep(4)
pg.hotkey('winleft', 'up')
pg.typewrite('espn.com\n', .15)
time.sleep(2)

pg.moveTo(1266, 170, 5.5 )
pg.click()
pg.typewrite('Aaron Rodgers\n', .5)

