import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_should_see_link_add_to_basket(browser):
    browser.get(link)
    time.sleep(10)
    assert browser.find_elements_by_css_selector(".btn-add-to-basket"), 'Кнопка отсутствует'
