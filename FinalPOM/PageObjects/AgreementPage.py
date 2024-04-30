import time

from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait
from selenium.webdriver.support import expected_conditions
from TestData.OrganizationData import OrganizationData
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common import action_chains


class AgreementPage:
    def __init__(self, dr, reg, location):
        self.dr = dr
        self.reg = reg
        self.filelocation = location + '\\'

    select_signatory = (By.XPATH, '//div[text()="Select Signatory"]')
    esign = (By.XPATH, '//p[text()="E-sign the agreement now"]')
    hns_telephone = (By.XPATH, '//input[@name="telephone"]')
    sign_textbox = (By.XPATH, '//input[@name="echosign_signature"]')
    type_sign_textbox = (By.XPATH, '//input[@placeholder="Type your signature here"]')
    next_required_field = (By.XPATH, '//a[text()=" Next required field "]')
    clear_button = (By.XPATH, '//button[text()="Clear"]')
    apply_button = (By.XPATH, '//button[text()="Apply"]')
    regenarate = (By.XPATH, '//span[text()="Regenerate"]')
    regenerate_ok = (By.XPATH, '//span[text()="Ok"]')
    download_draft = (By.XPATH, '//span[text()="Download Draft"]')

    def signAgreement(self):
        wait2 = wait.WebDriverWait(self.dr, 30)
        wait2.until(expected_conditions.presence_of_element_located(AgreementPage.download_draft))

        try:
            if self.dr.find_element(*AgreementPage.regenarate).is_enabled():
                self.dr.find_element(*AgreementPage.regenarate).click()
                self.dr.find_element(*AgreementPage.regenerate_ok).click()
        except:
            pass
        wait2.until(expected_conditions.presence_of_element_located(AgreementPage.select_signatory))
        k = self.dr.find_element(*AgreementPage.select_signatory)
        self.dr.find_element(*AgreementPage.select_signatory).click()
        act = ActionChains(self.dr)
        act.move_to_element(k)
        act.key_down(Keys.ENTER).perform()
        wait2.until(expected_conditions.presence_of_element_located(AgreementPage.esign))
        self.dr.find_element(*AgreementPage.esign).click()
        wait2.until(expected_conditions.frame_to_be_available_and_switch_to_it((By.ID, 'myId')))
        # self.dr.switch_to.frame("myId")
        wait3 = wait.WebDriverWait(self.dr, 20, poll_frequency=3,
                                   ignored_exceptions=[ElementNotVisibleException, ElementNotInteractableException,
                                                       NoSuchElementException, ElementClickInterceptedException])
        if self.reg == 'hns':
            wait3.until(expected_conditions.presence_of_element_located(AgreementPage.hns_telephone))
            self.dr.find_element(*AgreementPage.hns_telephone).send_keys('1234567890')
            time.sleep(3)
        wait3.until(expected_conditions.presence_of_element_located(AgreementPage.next_required_field))
        self.dr.find_element(*AgreementPage.next_required_field).click()
        n = self.dr.find_elements(*AgreementPage.sign_textbox)
        print('n=', len(n))

        wait3.until(expected_conditions.presence_of_element_located(AgreementPage.sign_textbox))

        act = ActionChains(self.dr)
        act.move_to_element(n[0])
        act.click(n[0])
        act.key_down(Keys.ENTER).perform()
        wait3.until(expected_conditions.presence_of_element_located(AgreementPage.apply_button))

        time.sleep(3)
        sign = self.dr.find_element(*AgreementPage.type_sign_textbox)
        act2 = ActionChains(self.dr)
        act2.move_to_element(sign)
        act2.click()
        act2.send_keys("kavya")
        act2.send_keys(Keys.ENTER).perform()
        if len(n) > 1:
            for i in range(1, len(n)):
                if i < len(n):
                    wait3.until(expected_conditions.presence_of_element_located(AgreementPage.next_required_field))
                    self.dr.find_element(*AgreementPage.next_required_field).click()
                    act = ActionChains(self.dr)
                    act.move_to_element(n[i])
                    act.click(n[i])
                    act.key_down(Keys.ENTER).perform()
                    print('xxxxxxxxxxxxxxxxxx')
