import time

from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait
from selenium.webdriver.support import expected_conditions

from PageObjects.AgreementPage import AgreementPage
from PageObjects.ClinicianLocationPage import ClinicianLocationPage
from TestData.OrganizationData import OrganizationData
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from Utilities.BaseClass import BaseClass


class TechnicalSurveyPage:
    def __init__(self, dr,reg,location):
        self.dr = dr
        self.reg = reg
        self.filelocation = location+ '\\'
    org_data_titile = (By.XPATH,'//h5[text()="HOW WOULD YOU LIKE TO SUBMIT YOUR ORGANIZATION\'S DATA?"]')
    dataentry_electronic = (By.XPATH,'//input[@value="Electronic Data Pull Push"]')
    dataentry_manual = (By.XPATH,'//input[@value="Manual Data Entry"]')
    ehr_Pull_radiobutton = (By.XPATH,'//input[@value="EHR Electronic Data Pull"]')
    ehr_name = (By.XPATH, '//div[text()="Name of EHR System"]/ancestor::div[@class="select__value-container css-1hwfws3"]/div/div/input')
    ehr_version = (By.XPATH,"//label[text()='Version of EHR System']/ancestor::div[@class='MuiFormControl-root input-field__container MuiFormControl-fullWidth']/div/input")
    ehr_hosting = (By.XPATH,'//span[text()="EHR Hosting"]/ancestor::div[@class="MuiFormControl-root input-field__container MuiFormControl-fullWidth"]//div[@style="display: inline-block;"]/input')
    ehr_vendor_account = (By.XPATH,'//input[@class="MuiInputBase-input MuiInput-input MuiInputBase-inputAdornedEnd"]')
    ehr_CEHRT_Yes = (By.XPATH,"//p[text()='Is your EHR a complete 2015 certified EHR Technology (CEHRT)? ']/ancestor::div[@class='MuiFormControl-root input-field__container MuiFormControl-fullWidth']//p[text()='Yes']")

#PM System fields
    pm_Pull_radiobutton = (By.XPATH,'//input[@value="PM Electronic Data Pull"]')
    pm_name = (By.XPATH,'//span[text()="Name of PM System"]/ancestor::div[@class="MuiFormControl-root input-field__container MuiFormControl-fullWidth"]//div/input')
    pm_version = (By.XPATH,'//label[text()="Version of PM System"]/ancestor::div[@class="MuiFormControl-root input-field__container MuiFormControl-fullWidth"]//div/input')

    save_submit_orgdata = (By.XPATH,'//h6[text()="ELECTRONIC HEALTH RECORD (EHR)"]/ancestor::div[@class="MuiGrid-root accordion-content__container undefined MuiGrid-item MuiGrid-grid-lg-12"]//span[text()="SAVE"]')
    save_alert = (By.XPATH,'//span[text()="Yes"]')
    success_mesg= (By.XPATH, '//div[contains(text(),"Data")]')


#Tell us more section
    tell_us_section = (By.XPATH,"//h5[text()='TELL US MORE TO KNOW YOUR ORGANIZATION BETTER']")
    hns_IsYourOrgPartOfAco_Yes = (By.XPATH,"//p[text()='Is your organization part of ACO?']/ancestor::div[@class='MuiFormControl-root input-field__container MuiFormControl-fullWidth']//p[text()='Yes']")

    group_reporting = (By.XPATH,"//p[text()='Group']")
    save_submit_tellus = (By.XPATH,'//h5[text()="TELL US MORE TO KNOW YOUR ORGANIZATION BETTER"]/ancestor::div[@class="MuiPaper-root MuiExpansionPanel-root accordion_master-wrapper  Mui-expanded MuiExpansionPanel-rounded MuiPaper-elevation1 MuiPaper-rounded"]//span[text()="SAVE"]')

#next button
    next = (By.XPATH,'//span[text()="Next"]')


    def submitOrgData(self):

        wait2 = wait.WebDriverWait(self.dr, 15)
        if self.reg in ['apta','polaris']:
            wait2.until(expected_conditions.presence_of_element_located((TechnicalSurveyPage.dataentry_electronic)))
            self.dr.find_element(*TechnicalSurveyPage.dataentry_electronic).click()

        wait2.until(expected_conditions.presence_of_element_located((TechnicalSurveyPage.ehr_Pull_radiobutton)))

        self.dr.find_element(*TechnicalSurveyPage.ehr_Pull_radiobutton).click()
        wait2 = wait.WebDriverWait(self.dr, 5)
        wait2.until(expected_conditions.presence_of_element_located((TechnicalSurveyPage.ehr_name)))
        self.dr.find_element(*TechnicalSurveyPage.ehr_name).send_keys('Compulink')
        time.sleep(2)
        act1 = ActionChains(self.dr)
        act1.key_down(Keys.ENTER).perform()
        self.dr.find_element(*TechnicalSurveyPage.ehr_version).send_keys('1234')
        self.dr.find_element(*TechnicalSurveyPage.ehr_hosting).send_keys('Cloud')
        act2 = ActionChains(self.dr)
        act2.key_down(Keys.ENTER).perform()
        if self.reg in ['hns']:
            self.dr.find_element(*TechnicalSurveyPage.ehr_vendor_account).send_keys('5899')
        self.dr.find_element(*TechnicalSurveyPage.ehr_CEHRT_Yes).click()
        wait3 = wait.WebDriverWait(self.dr, 5)
        self.dr.get_screenshot_as_file(self.filelocation + 'EHR.png')
        self.dr.find_element(*TechnicalSurveyPage.pm_Pull_radiobutton).click()
        wait3.until(expected_conditions.presence_of_element_located((TechnicalSurveyPage.pm_name)))
        self.dr.find_element(*TechnicalSurveyPage.pm_name).send_keys('Akamai')
        time.sleep(2)
        act3 = ActionChains(self.dr)
        act3.key_down(Keys.ENTER).perform()
        self.dr.find_element(*TechnicalSurveyPage.pm_version).send_keys('4567')
        self.dr.get_screenshot_as_file(self.filelocation + 'PM.png')
        self.dr.find_element(*TechnicalSurveyPage.save_submit_orgdata).click()
        self.dr.get_screenshot_as_file(self.filelocation + 'TechnicalSurvey.png')
        self.dr.find_element(*TechnicalSurveyPage.save_alert).click()
        wait2.until(expected_conditions.presence_of_element_located((TechnicalSurveyPage.success_mesg)))
        assert self.dr.find_element(*TechnicalSurveyPage.success_mesg)


    #Fill TELL US MORE section
    def submitTellUsData(self):
        wait2 = wait.WebDriverWait(self.dr, 15)
        wait2.until(expected_conditions.presence_of_element_located((TechnicalSurveyPage.tell_us_section)))
        wait3 = wait.WebDriverWait(self.dr, 10, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, ElementNotInteractableException])
        if self.reg == 'hns':
            wait3.until(expected_conditions.presence_of_element_located((TechnicalSurveyPage.tell_us_section)))
            self.dr.find_element(*TechnicalSurveyPage.tell_us_section).click()
            wait3.until(expected_conditions.presence_of_element_located(TechnicalSurveyPage.hns_IsYourOrgPartOfAco_Yes))
            self.dr.find_element(*TechnicalSurveyPage.hns_IsYourOrgPartOfAco_Yes).click()
            self.dr.find_element(*TechnicalSurveyPage.save_submit_tellus).click()
            wait3.until(expected_conditions.presence_of_element_located((TechnicalSurveyPage.success_mesg)))
            assert self.dr.find_element(*TechnicalSurveyPage.success_mesg)
        elif 'elixir' in self.reg or self.reg == 'polaris':
            wait3.until(expected_conditions.presence_of_element_located((TechnicalSurveyPage.tell_us_section)))
            self.dr.find_element(*TechnicalSurveyPage.tell_us_section).click()

            wait3.until(expected_conditions.presence_of_element_located((TechnicalSurveyPage.group_reporting)))
            self.dr.find_element(*TechnicalSurveyPage.group_reporting).click()
            self.dr.find_element(*TechnicalSurveyPage.save_submit_tellus).click()
            wait3.until(expected_conditions.presence_of_element_located((TechnicalSurveyPage.success_mesg)))
            assert self.dr.find_element(*TechnicalSurveyPage.success_mesg)


    def clickNext(self):

        wait3 = wait.WebDriverWait(self.dr, 20, poll_frequency=5,
                                   ignored_exceptions=[ElementNotVisibleException, ElementNotInteractableException,ElementClickInterceptedException,NoSuchElementException])

        wait3.until(expected_conditions.visibility_of_all_elements_located(TechnicalSurveyPage.org_data_titile))


        self.dr.find_element(*TechnicalSurveyPage.next).click()


        clinician = ClinicianLocationPage(self.dr, self.reg,self.filelocation)

        return clinician











