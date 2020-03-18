from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.webdriver.common.by import By


class BasketPage(BasePage):

    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
           "Basket is empty"

    def should_be_basket_empty_text(self):
        assert self.is_element_present(*BasketPageLocators.BACSKET_EMPTY), \
           "Basket is empty"