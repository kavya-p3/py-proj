*** Settings ***
Library    SeleniumLibrary
Documentation    inside settings

*** Variables ***
${Browser}    Chrome
${URL}    https://qa-pegasus2-apta.figmd.com/signup/login

*** Test Cases ***
Execution TC02
    open browser   ${URL}    ${Browser}
    click element
    e