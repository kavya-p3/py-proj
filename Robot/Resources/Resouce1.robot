*** Settings ***
Library    ../ExternalKeywords/UserDefined.py


*** Variables ***



*** Keywords ***
this is test resource
    [Arguments]    ${URL}   ${Browser}
    open browser     ${URL}    ${Browser}
    wait until element is visible    name:TextField
    input text    name:TextField    reg_auto
    input text    name:password     Abcd1234#
    click element    xpath://button/span[text()="Login"]
    ${res}=     get title
    [return]    ${res}


create folder using os lib
    #create_folder
    [arguments]    ${val1}    ${val2}
    ${res}=    concatenate    ${val1}    ${val2}
    log    ${res}