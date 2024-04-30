*** Settings ***
Library    SeleniumLibrary
Documentation    inside settings

*** Variables ***
${Browser}    Chrome
${URL}    https://qa-pegasus2-hns.figmd.com/signup/login

*** Test Cases ***
Execution TC01
    open browser   ${URL}    ${Browser}
    input text