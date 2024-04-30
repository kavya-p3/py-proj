*** Settings ***
Library    SeleniumLibrary
Documentation    inside settings
Resource    ../Resources/Resouce1.robot

*** Variables ***
${Browser}    Chrome
${URL}    https://qa-pegasus2-hns.figmd.com/signup/login

*** Test Cases ***
TC_001 Browser start and close
    [Documentation]    inside testcase
    ${val} =    this is test resource   ${URL}  ${Browser}
    log    ${val}
    create folder using os lib    Kavya    Pra
    LOG    "ABC"
    LOG    ABC

