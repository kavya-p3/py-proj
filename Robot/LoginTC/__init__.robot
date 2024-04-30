*** Settings ***

suite setup    Before exe
suite teardown    After exe

*** Keywords ***
Before exe
    log    started execution

After exe
    log    executiopn ending