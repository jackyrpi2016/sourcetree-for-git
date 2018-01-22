>>> import pyautogui
>>> # screen resolution
>>> pyautogui.size()
(1280, 800)
>>> width, height = pyautogui.size()
>>> width
1280
>>> height
800
>>> 
>>> # current position
>>> pyautogui.position()
(308, 430)
>>> # move to a position
>>> pyautogui.moveTo(10, 10)
>>> # move like a human, slowly
>>> pyautogui.moveTo(10, 10, duration=2)
>>> # move relative to current position
>>> pyautogui.moveRel(20, 50, duration=1)
>>> # move up
>>> pyautogui.moveRel(0, -100, duration=1.5)
>>> 
>>> # click
>>> pyautogui.click(500, 500)
>>> pyautogui.doubleClick(54, 90)
>>> pyautogui.rightClick(66, 444)
>>> pyautogui.middleClick(43, 12)
>>> 
