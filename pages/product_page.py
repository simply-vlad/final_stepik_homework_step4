from .base_page import BasePage
from .locators import ProductPageLocators

import time


class ProductPage(BasePage):
    def click_add_to_basket_form(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_FORM), "Add to backet form is not presented"
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_FORM)
        button.click()
        self.solve_quiz_and_get_code()

    def check_name_product(self):
        product_in_basket_name = self.browser.find_element(*ProductPageLocators.PRODUCT_IN_BASKET_NAME)
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        print(f'\n{product_in_basket_name.text}\n{product_name.text}')
        assert product_name.text == product_name.text, "Product names do not match:("
        time.sleep(1)

    def check_price_product(self):
        product_in_basket_price = self.browser.find_element(*ProductPageLocators.PRODUCT_IN_BASKET_PRICE)
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        print(f'\n{product_in_basket_price.text}\n{product_price.text}')
        assert product_price.text == product_price.text, "Product price do not match:("
        time.sleep(1)
