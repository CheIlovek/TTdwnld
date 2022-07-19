from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class TTLogger:

    DELAY = 0
    DRIVER = None

    def __init__(self, driver, delay=10):
        self.DELAY = delay
        self.DRIVER = driver
    
    def login(self):
        username = "TikTokDWNLD"
        password = "UyF-bJ3-RaJ-mu4"
        loaded = False
        while not loaded:
            try:
                WebDriverWait(self.DRIVER, self.DELAY).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "e13wiwn62")))
                loaded = True
            except Exception:
                self.DRIVER.execute_script("window.scrollBy(0,100)", "")
        button = self.DRIVER.find_element(By.CLASS_NAME, "e13wiwn62")
        button.click()
        try:
            WebDriverWait(self.DRIVER, self.DELAY).until(
                EC.presence_of_element_located((By.XPATH, "//div[text()='Продолжить в Google']")))
        except Exception:
            raise Exception("Registration wasnt loaded")
        button = self.DRIVER.find_element(By.XPATH, "//div[text()='Продолжить в Google']")
        button.click()

        original_window = self.DRIVER.current_window_handle
        # Wait for the new window or tab
        WebDriverWait(self.DRIVER, self.DELAY).until(EC.number_of_windows_to_be(2))

        # Loop through until we find a new window handle
        for window_handle in self.DRIVER.window_handles:
            if window_handle != original_window:
                self.DRIVER.switch_to.window(window_handle)
                break

        try:
            WebDriverWait(self.DRIVER, self.DELAY).until(
                EC.presence_of_element_located((By.ID, "identifierId")))
        except Exception:
            raise Exception("Registration wasnt loaded")
        in_box = self.DRIVER.find_element(By.ID, "identifierId")
        in_box.send_keys(username)
        in_box.send_keys(Keys.RETURN)

        try:
            WebDriverWait(self.DRIVER, self.DELAY).until(
                EC.presence_of_element_located((By.NAME, "password")))
        except Exception:
            raise Exception("Registration wasnt loaded")
        in_box = self.DRIVER.find_element(By.NAME, "password")
        in_box.send_keys(password)
        in_box.send_keys(Keys.RETURN)
        self.DRIVER.switch_to.window(original_window)

        try:
            WebDriverWait(self.DRIVER, self.DELAY*2).until(
                EC.presence_of_element_located((By.CLASS_NAME, "etvrc4k0")))
        except TimeoutException:
            raise Exception("NOT LOADED!")

