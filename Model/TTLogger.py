from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time


class TTLogger:

    DELAY = 10
    DRIVER = None

    def __init__(self, driver, delay=10):
        self.DELAY = delay
        self.DRIVER = driver
    
    def login(self):
        self.login_to_google()
        self.login_to_tiktok()


    def login_to_google(self):
        username = "TTScanMail"
        password = "UyF-bJ3-RaJ-mu4"
        self.DRIVER.get(R"https://accounts.google.com/signin/oauth/identifier?client_id=717762328687-iludtf96g1hinl76e4lc1b9a82g457nn.apps.googleusercontent.com&scope=profile%20email&redirect_uri=https%3A%2F%2Fstackauth.com%2Fauth%2Foauth2%2Fgoogle&state=%7B%22sid%22%3A1%2C%22st%22%3A%2259%3A3%3ABBC%2C16%3A9b15b0994c6df9fc%2C10%3A1591711286%2C16%3A66b338ce162d6599%2Ca78a0c663f0beb12c0559379b61a9f5d62868c4fbd2f00e46a86ac26796507a1%22%2C%22cdl%22%3Anull%2C%22cid%22%3A%22717762328687-iludtf96g1hinl76e4lc1b9a82g457nn.apps.googleusercontent.com%22%2C%22k%22%3A%22Google%22%2C%22ses%22%3A%22921f8f04441041069683cc2377152422%22%7D&response_type=code&o2v=1&as=NCQvtBXI4prkLLDbn4Re0w&flowName=GeneralOAuthFlow")
        
        # Ввод логина
        try:
            elem = WebDriverWait(self.DRIVER, self.DELAY).until(
                EC.element_to_be_clickable((By.ID, "identifierId")))
        except Exception:
            raise Exception("Registration wasnt loaded")
        elem.send_keys(username)
        elem.send_keys(Keys.RETURN)

        # Ввод пароля
        try:
            elem = WebDriverWait(self.DRIVER, self.DELAY).until(
                EC.element_to_be_clickable((By.NAME, "Passwd")))
        except Exception:
            raise Exception("Registration wasnt loaded")
        elem.send_keys(password)
        elem.send_keys(Keys.RETURN)
        # Подтверждение входа
        try:
            elem = WebDriverWait(self.DRIVER, self.DELAY).until(
                EC.element_to_be_clickable((By.XPATH, "//span[text()='Continue']")))
        except Exception:
            raise Exception("Registration wasnt loaded")
        elem.click()

        #Убеждаемся что вход прошёл
        try:
            WebDriverWait(self.DRIVER, self.DELAY).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "s-topbar--container")))
        except Exception:
            raise Exception("Registration wasnt loaded")
        










        
        

    def login_to_tiktok(self):

        self.DRIVER.get("https://www.tiktok.com/")
        try:
            WebDriverWait(self.DRIVER, self.DELAY).until(
                EC.presence_of_element_located((By.CLASS_NAME, "e10win0d2")))
        except Exception:
            raise Exception("Registration wasnt loaded")


        
        # Уже выпало меню входа в аккаунт?
        loginMenuLoaded = True
        time.sleep(20) #TODO: Капчаааа
        try:
            WebDriverWait(self.DRIVER, self.DELAY).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "css-7u35li-DivBoxContainer")))
        except Exception:
            loginMenuLoaded = False

        elems = self.DRIVER.find_elements(By.CLASS_NAME, "css-7u35li-DivBoxContainer")
        original_window = self.DRIVER.current_window_handle
        numOfWins = len(self.DRIVER.window_handles)
        elems[3].click()
            
        # Wait for the new window or tab
        
        try:
            WebDriverWait(self.DRIVER, self.DELAY).until(EC.number_of_windows_to_be(numOfWins+1))
        except Exception:
            raise Exception("Registration wasnt loaded")

        # Loop through until we find a new window handle
        for window_handle in self.DRIVER.window_handles:
            if window_handle != original_window:
                self.DRIVER.switch_to.window(window_handle)
                break

        
        #Выбираем наш гугл аккаунт
        try:
            elem = WebDriverWait(self.DRIVER, self.DELAY).until(
                EC.presence_of_element_located((By.XPATH, "//div[text()='ttscanmail@gmail.com']")))
        except Exception:
            raise Exception("Registration wasnt loaded")
        elem.click()


        # Подтверждение входа
        try:
            elem = WebDriverWait(self.DRIVER, self.DELAY).until(
                EC.presence_of_element_located((By.XPATH, "//span[text()='Continue']")))
        except Exception:
            raise Exception("Registration wasnt loaded")
        elem.click()
        self.DRIVER.switch_to.window(original_window)

        try:
            WebDriverWait(self.DRIVER, self.DELAY*2).until(
                EC.presence_of_element_located((By.CLASS_NAME, "etvrc4k0")))
        except TimeoutException:
            raise Exception("NOT LOADED!")
        
        #TODO: Может не пустить за попытки входа, надо отлавливать