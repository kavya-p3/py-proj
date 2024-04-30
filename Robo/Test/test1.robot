*** Settings ***
Library     SeleniumLibrary
Library    SeleniumLibrary


*** Test Cases ***
Validate Unsuccessful Login
    open the browser with mortgage payment URL
    fill the login form
    wait until it checks and display error message
#    verify error message is correct


*** Keywords ***
open the browser with mortgage payment URL
    Create Webdriver    Chrome  executable_path=K:/chromedriver.exe
    Go To   https://rahulshettyacademy.com/loginpagePractise/

fill the login form
    input text    name:username     rahulshettyacademy
    input password    id:password   123456
    input text    id:password   123456


wait until it checks and display error message
    click button    signInBtn
    wait until element is visible    css:.alert-danger
    close browser


#verify error message is correct
#    click button    signInBtn
#    click button    signInBtn
#    wait until element is visible    css:.alert alert-danger
#    ${result}=  Get Text    css:.alert alert-danger
#    should be equal as strings    ${result}     Incorrect username/password.





