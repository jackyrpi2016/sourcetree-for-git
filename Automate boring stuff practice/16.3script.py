>>> import pyautogui
>>> # take a screenshot
>>> pyautogui.screenshot()
<PIL.PngImagePlugin.PngImageFile image mode=RGBA size=2560x1600 at 0x10EB3E240>
>>> # take a screenshot, save at a certain position
>>> pyautogui.screenshot('/Users/lichenglong/Desktop/test1.png')
<PIL.PngImagePlugin.PngImageFile image mode=RGBA size=2560x1600 at 0x10EA88400>
>>> 
>>> # recognize a image
>>> pyautogui.locateOnScreen('/Users/lichenglong/Desktop/reference_digit.png')
>>> pyautogui.locateOnScreen('/Users/lichenglong/Desktop/reference_digit.png')
(1582, 456, 114, 98)
>>> # x, y, width, height
>>> pyautogui.locateCenterOnScreen('/Users/lichenglong/Desktop/reference_digit.png')
(1639, 505)
>>> # center position
>>> 
>>> # moveTo(), tuple or separate digits are ok
>>> pyautogui.moveTo((1639, 505), duration=1)
>>> pyautogui.moveTo((1639, 505), duration=1)
>>> pyautogui.moveTo(1639, 505, duration=1)
>>> pyautogui.click(1639, 505)
>>> 
