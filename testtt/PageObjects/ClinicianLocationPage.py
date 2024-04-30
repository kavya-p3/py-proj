import re
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait
from selenium.webdriver.support import expected_conditions
from PageObjects.AgreementPage import AgreementPage
from TestData.ClinicianLocationData import ClinicianLocationData
from TestData.OrganizationData import OrganizationData
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys



class ClinicianLocationPage:
    def __init__(self, dr, reg, location):
        self.dr = dr
        self.reg = reg
        self.filelocation = location + '\\'

    add_clinician_button = (By.XPATH, '//span[text()="ADD CLINICIAN"]')
    clinician_npi = (By.XPATH,
                     '//label[text()="Clinician NPI "]/ancestor::div[@class="MuiFormControl-root input-field__container MuiFormControl-fullWidth"]/div/input')
    clinician_first_name = (By.XPATH,'//label[text()="First Name"]/ancestor::div[@class="MuiFormControl-root input-field__container MuiFormControl-fullWidth"]//input')
    clinician_middle_name = (By.XPATH,'//label[text()="Middle Name"]/ancestor::div[@class="MuiFormControl-root input-field__container MuiFormControl-fullWidth"]//input')
    clinician_last_name = (By.XPATH,'//label[text()="Last Name"]/ancestor::div[@class="MuiFormControl-root input-field__container MuiFormControl-fullWidth"]//input')
    clinician_memberid = (By.XPATH,
                          '//label[contains(text(),"Member ID ")]/ancestor::div[@class="MuiFormControl-root input-field__container MuiFormControl-fullWidth"]/div/input')
    clinician_DOB = (By.XPATH,
                     '//label[text()="Date of Birth"]/ancestor::div[@class="MuiFormControl-root MuiTextField-root"]//div/input')
    clinician_email_address = (By.XPATH,
                               '//label[contains(text(),"Email Address")]/ancestor::div[@class="MuiFormControl-root input-field__container MuiFormControl-fullWidth"]/div/input')
    clinician_phone_number = (By.XPATH,
                              '//label[text()="Phone No"]/ancestor::div[@class="MuiFormControl-root input-field__container MuiFormControl-fullWidth"]//div[@fieldname="Phone"]')
    clinician_phone_extn = (By.XPATH,
                            '//label[text()="Phone No Extn"]/ancestor::div[@class="MuiFormControl-root input-field__container MuiFormControl-fullWidth"]//div/input')
    clinician_alternate_phone_number = (By.XPATH,
                                        '//label[text()="Alternate Phone No"]/ancestor::div[@class="MuiFormControl-root input-field__container MuiFormControl-fullWidth"]//div/input')
    clinician_alternate_phone_extn = (By.XPATH,
                                      '//label[text()="Alternate Phone No Extn"]/ancestor::div[@class="MuiFormControl-root input-field__container MuiFormControl-fullWidth"]//div/input')
    clinician_type = (By.XPATH,
                      '//div[text()="Select Clinician type"]/ancestor::div[@class="select__value-container css-1hwfws3"]//div/input')
    clinician_designation = (By.XPATH,
                             '//div[text()="Select Designation Title"]/ancestor::div[@class="select__value-container css-1hwfws3"]//div/input')
    clinician_save = (By.XPATH, '//span[text()="Save"]')
#APTA
    clinician_apta_member = (By.XPATH,'//div[text()="Are you an APTA Member?"]/ancestor::div[@class="select__value-container css-1hwfws3"]//input')

    # Location
    location_add_button = (By.XPATH, '//span[text()="ADD LOCATION"]')
    location_name = (By.XPATH,
                     '//label[text()="Location Name"]/ancestor::div[@class="MuiFormControl-root input-field__container MuiFormControl-fullWidth"]/div/input')
    location_ID = (By.XPATH,
                   '//label[text()="Location ID"]/ancestor::div[@class="MuiFormControl-root input-field__container MuiFormControl-fullWidth"]/div/input')
    location_area = (By.XPATH, '//div[text()="Area"]/ancestor::div[@class="select__value-container css-1hwfws3"]//input')
    location_type_full = (By.XPATH, '//p[contains(text(),"Full Time")]')
    location_type_part = (By.XPATH, '//p[text()="Part Time"]')
    location_number_street = (By.XPATH,
                              '//label[text()="Number & Street"]/ancestor::div[@class="MuiFormControl-root input-field__container MuiFormControl-fullWidth"]/div/input')
    location_building_suite_floor = (By.XPATH,
                                     '//label[text()="Building/Suite/Floor"]/ancestor::div[@class="MuiFormControl-root input-field__container MuiFormControl-fullWidth"]/div/input')
    location_zip = (By.XPATH,
                    '//label[text()="Zip Code"]/ancestor::div[@class="MuiFormControl-root input-field__container MuiFormControl-fullWidth"]/div/input')
    location_tin = (By.XPATH,
                    '//div[text()="Select Tax Identification Number"]/ancestor::div[@class="select__value-container css-1hwfws3"]//div/input')
    location_save = (By.XPATH, '//span[text()="Save"]')

    success_mesg = (By.XPATH, '//div[contains(text(),"Data")]')
    data = ClinicianLocationData()
    next = (By.XPATH, '//span[text()="Next"]')

    def add_clinician(self):

        wait2 = wait.WebDriverWait(self.dr, 15)
        wait2.until(expected_conditions.presence_of_element_located((ClinicianLocationPage.add_clinician_button)))
        self.dr.find_element(*ClinicianLocationPage.add_clinician_button).click()
        wait2.until(expected_conditions.presence_of_element_located(ClinicianLocationPage.clinician_npi))
        self.dr.find_element(*ClinicianLocationPage.clinician_npi).send_keys(ClinicianLocationPage.data.clinician['NPI'])
        fn = self.dr.find_element(*ClinicianLocationPage.clinician_first_name).get_attribute("value")





        self.dr.find_element(*ClinicianLocationPage.clinician_phone_extn).send_keys(ClinicianLocationPage.data.clinician['phoneextn'])
        if self.reg in ['apta']:
            self.dr.find_element(*ClinicianLocationPage.clinician_DOB).send_keys(ClinicianLocationPage.data.clinician['DOB'])
            self.dr.find_element(*ClinicianLocationPage.clinician_apta_member).send_keys('No')
            act = ActionChains(self.dr)
            act.key_down(Keys.ENTER).perform()
            self.dr.find_element(*ClinicianLocationPage.clinician_type).send_keys('Occupational')
            act = ActionChains(self.dr)
            act.key_down(Keys.ENTER).perform()
        if self.reg in ['hns', 'aan']:
            self.dr.find_element(*ClinicianLocationPage.clinician_memberid).send_keys(ClinicianLocationPage.data.clinician['memeberID'])
        wait2.until((expected_conditions.presence_of_element_located((ClinicianLocationPage.clinician_email_address))))
        self.dr.find_element(*ClinicianLocationPage.clinician_email_address).send_keys(ClinicianLocationPage.data.clinician['email'])


        self.dr.find_element(*ClinicianLocationPage.clinician_save).click()
        wait2.until((expected_conditions.presence_of_element_located((ClinicianLocationPage.success_mesg))))
        self.dr.get_screenshot_as_file(self.filelocation + 'ClinicianPage.png')
        assert ClinicianLocationPage.success_mesg

    def add_location(self):
        wait2 = wait.WebDriverWait(self.dr, 15)
        wait2.until(expected_conditions.presence_of_element_located(ClinicianLocationPage.location_add_button))
        time.sleep(2)
        self.dr.find_element(*ClinicianLocationPage.location_add_button).click()
        wait2.until(expected_conditions.presence_of_element_located(ClinicianLocationPage.location_name))
        self.dr.find_element(*ClinicianLocationPage.location_name).send_keys(ClinicianLocationPage.data.location['name'])
        self.dr.find_element(*ClinicianLocationPage.location_ID).send_keys(ClinicianLocationPage.data.location['id'])
        self.dr.find_element(*ClinicianLocationPage.location_number_street).send_keys(ClinicianLocationPage.data.location['number'])
        self.dr.find_element(*ClinicianLocationPage.location_building_suite_floor).send_keys(ClinicianLocationPage.data.location['building'])
        self.dr.find_element(*ClinicianLocationPage.location_zip).send_keys(ClinicianLocationPage.data.location['zipcode'])
        self.dr.find_element(*ClinicianLocationPage.location_area).send_keys(ClinicianLocationPage.data.location['area'])
        act = ActionChains(self.dr)
        act.key_down(Keys.ENTER).perform()
        if ClinicianLocationPage.data.location['type'] == 'Full Time':
            self.dr.find_element(*ClinicianLocationPage.location_type_full).click()
        else:
            self.dr.find_element(*ClinicianLocationPage.location_type_part).click()

        time.sleep(2)
        self.dr.find_element(*ClinicianLocationPage.location_save).click()
        wait2.until((expected_conditions.presence_of_element_located((ClinicianLocationPage.success_mesg))))
        self.dr.get_screenshot_as_file(self.filelocation + 'Location.png')
        assert ClinicianLocationPage.success_mesg

    def clickNext(self):
        time.sleep(10)
        self.dr.find_element(*ClinicianLocationPage.next).click()
        agreement = AgreementPage(self.dr,self.reg,self.filelocation)
        return agreement


