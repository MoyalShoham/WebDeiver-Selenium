
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class User:
    created = True  # static data member - check if the user already order from the site (his details are saved)
    shipped = True  # static data member - check if the user already signed up
    @staticmethod
    def set_created():
        User.created = True

    def create_account(self):
        self.wd.get(r'https://magento.softwaretestingboard.com/customer/account/create/')
        self.wd.find_element(By.CSS_SELECTOR, '#firstname').send_keys('Shoham')
        self.wd.find_element(By.CSS_SELECTOR, '#lastname').send_keys('Moyal')
        self.wd.find_element(By.CSS_SELECTOR, '#is_subscribed').click()
        self.wd.find_element(By.CSS_SELECTOR, '#email_address').send_keys('moyalsssshoham@gggmail.com')
        self.wd.find_element(By.CSS_SELECTOR, '#password').send_keys('Sho123456_')
        self.wd.find_element(By.CSS_SELECTOR, '#password-confirmation').send_keys('Sho123456_')
        self.wd.find_element(By.CSS_SELECTOR, '#password-confirmation').submit()

    def log_in(self):
        if User.created:
            self.wd.get(r'https://magento.softwaretestingboard.com/customer/account/login/referer/aHR0cHM6Ly9tYWdlbnRvLnNvZnR3YXJldGVzdGluZ2JvYXJkLmNvbS9jdXN0b21lci9hY2NvdW50L2NyZWF0ZS8%2C/')
            self.wd.find_element(By.CSS_SELECTOR, '#email').send_keys('moyalsssshoham@gggmail.com')
            self.wd.find_element(By.CSS_SELECTOR, '#pass').send_keys('Sho123456_')
            self.wd.find_element(By.CSS_SELECTOR, '#pass').submit()

    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd.get('https://magento.softwaretestingboard.com')
        self.wd.maximize_window()
        self.wd.implicitly_wait(5)
        if User.created == False:
            self.create_account()
            self.set_created()
        self.log_in()

    def buy_two_items(self):
        # self.log_in()
        self.wd.get('https://magento.softwaretestingboard.com/men/tops-men/jackets-men.html')
        self.wd.find_element(By.XPATH, '//*[@id="maincontent"]/div[3]/div[1]/div[3]/ol/li[1]/div/div/strong/a').click()
        self.wd.find_element(By.XPATH, '//*[@id="option-label-size-143-item-167"]').click()  # small size
        self.wd.find_element(By.XPATH, '//*[@id="option-label-color-93-item-49"]').click()   # dark color
        self.wd.find_element(By.XPATH, '//*[@id="product-addtocart-button"]/span').click()  # submit button
        self.wd.implicitly_wait(100)
        self.wd.get('https://magento.softwaretestingboard.com/men/bottoms-men.html')
        self.wd.find_element(By.XPATH, '//*[@id="maincontent"]/div[3]/div[1]/div[3]/ol/li[1]/div/div/strong/a').click()
        self.wd.find_element(By.XPATH, '//*[@id="option-label-size-143-item-175"]').click()
        self.wd.find_element(By.XPATH, '//*[@id="option-label-color-93-item-49"]').click()  # small size
        self.wd.find_element(By.XPATH, '//*[@id="product-addtocart-button"]/span').click()  # submit button
        self.wd.implicitly_wait(100)
        # go to check out

    def fill_shipping_details(self):
        self.wd.find_element(By.XPATH, '//*[@id="maincontent"]/div[1]/div[2]/div/div/div/a').click()
        self.wd.find_element(By.XPATH, '//*[@id="maincontent"]/div[3]/div/div[2]/div[1]/ul/li[1]/button').click()
        if User.shipped:
            self.wd.implicitly_wait(100)
        else:
            self.wd.find_element(By.NAME, 'street[0]').send_keys('Mikve Israel')
            self.wd.find_element(By.NAME, 'city').send_keys('Ashdod')
            select_button = Select(self.wd.find_element(By.NAME, 'region_id'))
            select_button.select_by_visible_text('Texas')
            self.wd.find_element(By.NAME, 'postcode').send_keys('12345')
            select_button = Select(self.wd.find_element(By.NAME, 'country_id'))
            select_button.select_by_visible_text('Morocco')
            self.wd.find_element(By.NAME, 'telephone').send_keys('0535258055')
            # self.wd.find_element(By.NAME, 'ko_unique_1').click()
            self.wd.find_element(By.NAME, 'ko_unique_3').click()
            self.wd.find_element(By.XPATH, '//*[@id="shipping-method-buttons-container"]/div/button').click()
            User.shipped = True
        self.wd.get('https://magento.softwaretestingboard.com/checkout/#payment')

    def check_out(self):
        # self.wd.find_element(By.CLASS_NAME, 'action primary checkout').click()
        self.wd.find_element(By.XPATH, '/html/body/div[3]/main/div[2]/div/div[2]/div[4]/ol/li[3]/div/form/fieldset/div[1]/div/div/div[2]/div[2]/div[4]/div/button').click()



if __name__ == "__main__":
    def run():
        u = User()
        u.buy_two_items()
        u.wd.implicitly_wait(10)
        u.fill_shipping_details()
        u.check_out()
        return 0






