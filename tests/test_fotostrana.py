import pytest
from selene.support.shared import browser
from selene import have, be


def test_submit_homepage():
    browser.open('https://fotostrana.ru/')
    browser.should(have.title('Фотострана: сайт знакомств без регистрации, фото девушек и парней'))
    browser.execute_script(
        'document.querySelectorAll("iframe._js-placement-target-signup").forEach(element => element.remove())')
    browser.element('.signup-top__link--news').should(have.text('Новости'))
    browser.element('.signup-top__link--meeting').should(have.text('Встречи'))
    browser.element('.signup-top__link--games').should(have.text('Игры'))
    browser.element('.signup-top__link--people').should(have.text('Знакомства'))
    browser.element('div .newmain__top-link--signup').click()
    browser.all('.login-form input').should(have.size(4))
    browser.element('div #user_email').type('email123@gmail.com')
    browser.element('button#loginPopupSubmitButton').click()
    browser.element('input#user_password').type('123qweddsVFGFFDdds5541')
    browser.element('div.signup-forms__back').click()
    browser.element('//*[@class="signup-sex__button"][@data-sex="m"]').click()
    browser.element('#userName').type('Evgeniy')
    browser.element('#btnRegister').click()
