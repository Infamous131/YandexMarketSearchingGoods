# coding: utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By


# Узнаём имя новой вкладки и переключаемся на нее
def window_switching(number, browser):
    window_name = browser.window_handles[number]
    browser.switch_to.window(window_name)


# Открытие браузера
def open_browser():
    browser = webdriver.Chrome()
    return browser


# Переход на Маркет с Яндекс поисковика
def yandex_search(browser, link):
    # Открытие браузера
    browser.get(link)
    # Задание неявноого ожидания
    browser.implicitly_wait(10)
    # Поиск и клик по Яндекс.Маркет
    browser.find_element(By.CSS_SELECTOR, 'a[data-id="market"] div.services-new__item-title').click()


# Поиск товара на Яндекс.Маркете
def market_search(browser):
    # Нахождение поисковой строки и ввод искомого наименования
    browser.find_element(By.CSS_SELECTOR, 'input#header-search').send_keys(searching_goods)
    # Поиск и клик по кнопке
    browser.find_element(By.CSS_SELECTOR, 'button[data-r="search-button"]').click()
    # Поиск пятого элемента в выпавшем списке и клик по нему
    browser.find_element(By.CSS_SELECTOR, 'div[data-zone-name="SearchResultsPaged"] > div:nth-child(2) '
                                          'article:nth-of-type(2) h3 > a[target="_blank"]').click()


# Проверка совпадения на странице товара в Яндекс.Маркете
def device_page_on_market(browser, device, brand):
    # Поиск типа устройства
    page_device_type = browser.find_element(By.CSS_SELECTOR, 'dl[id="tip ustroistva"] dd').text
    # Проверка совпадения типа устройства и искомым
    assert page_device_type == device, f'Device type {page_device_type} is different from {device}'
    # Поиск заголовка устройства
    device_header = browser.find_element(By.CSS_SELECTOR, 'div[data-apiary-widget-id="/content/productCardTitle"] '
                                                          'h1').text
    # Проверка бренда устройства с искомым
    assert brand in device_header, f'There is no {brand} brand in the brief ' \
                                   f'description of the device'


# Объявление констант
YANDEX_LINK = "https://yandex.ru/"
SEARCHING_DEVICE_TYPE = 'беспроводные TWS-наушники'
SEARCHING_BRAND = 'Apple'

try:
    # Искомый товар
    searching_goods = SEARCHING_DEVICE_TYPE + ' ' + SEARCHING_BRAND
    # Открытие Chrome браузера
    chrome_browser = open_browser()
    # Действия на Яндекс поисковике
    yandex_search(chrome_browser, YANDEX_LINK)
    # Переключение на вкладку Маркета
    window_switching(1, chrome_browser)
    # Поиск товара на Яндекс.Маркете
    market_search(chrome_browser)
    # Переключение на вкладку товара
    window_switching(2, chrome_browser)
    # Проверка совпадения товара с искомым
    device_page_on_market(chrome_browser, SEARCHING_DEVICE_TYPE, SEARCHING_BRAND)

finally:
    chrome_browser.quit()
