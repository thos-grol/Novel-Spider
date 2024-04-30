from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options

import time
import pyautogui

class Driver(metaclass=Singleton):
    
    def __init__(self):
        o = webdriver.EdgeOptions()
        o.add_experimental_option('prefs', {
            'translate_whitelists': {'zh': 'en'},
            'translate': {'enabled': 'true'}
        })
        self.driver = webdriver.Edge(options=o)
        self.novel_id = 0

        self.is_ready_to_interact = False

    #called fns
    def goTo(self, url):
        self.driver.get(url)

    def find_element(self, dict):
        ret = None
        init = True
        for key in dict:
            if init:
                ret = self.driver.find_element(self._get_BY(key), dict[key])
                init = False
            else:
                ret = ret.find_element(self._get_BY(key), dict[key])

        return ret
    
    def translate_page(self, is_button_pressed=False, translate_interval=1):
        #wait so default browser pop ups don't break the spider
        if not self.is_ready_to_interact:
            time.sleep(2)
            self.is_ready_to_interact = True

        if not is_button_pressed:
            pyautogui.click(x=300, y=300, button='right')
            time.sleep(1)
            button_translate = pyautogui.locateOnScreen(PATH_BUTTON_TRANSLATE, confidence=0.9)
            pyautogui.click(button_translate.left, button_translate.top)

        time.sleep(translate_interval)
        self.driver.execute_script('window.scrollTo(0,document.body.scrollHeight/2);')
        time.sleep(translate_interval)
        self.driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
        time.sleep(translate_interval)

    


    #getters and setters
    def get_novel_id(self):
        return self.novel_id
    
    def set_novel_id(self, id):
        self.novel_id = id
    

    #helper
    def _get_BY(self, method):
        if method == 'XPATH':
            return By.XPATH
        elif method == 'CLASS_NAME':
            return By.CLASS_NAME
        elif method == 'TAG_NAME':
            return By.TAG_NAME
        return None

