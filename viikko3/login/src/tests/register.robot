*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Create Username  mikko
    Create Password  mikko1234
    Password confirmation  mikko1234
    Click  button >> text=Register
    Register Should Succeed

Register With Too Short Username And Valid Password
    Create Username  a
    Create Password  abcd1234
    Password confirmation  abcd1234
    Click  button >> text=Register
    Get Text  body  *=  Too short username


Register With Valid Username And Too Short Password
    Create Username  antti
    Create Password  a
    Password confirmation  a
    Click  button >> text=Register
    Get Text  body  *=  Too short password

Register With Password Consisting Only Of Letters
    Create Username  antti
    Create Password  password
    Password confirmation  password
    Click  button >> text=Register
    Register Should Fail With Message  Password must contain a number

Register With Mismatched Password Confirmation
    Create Username  antti
    Create Password  password1
    Password confirmation  password2
    Click  button >> text=Register
    Register Should Fail With Message  Passwords do not match

Register With Username That Is Already In Use
    Create Username  mikko
    Create Password  apina345
    Password confirmation  apina345
    Click  button >> text=Register
    
    Go To Register Page

    Create Username  mikko
    Create Password  apina345
    Password confirmation  apina345
    Click  button >> text=Register
    Get Text  body  *=  Username already exists


*** Keywords ***
Reset Application Create User And Go To Register Page
    Reset Application
    Go To Register Page

Create Username
    [Arguments]  ${username}
    Fill Text  id=username  ${username}

Create Password
    [Arguments]  ${password}
    Fill Text  id=password  ${password}

Password confirmation
    [Arguments]  ${password}
    Fill Text  id=password_confirmation  ${password}

Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Get Text  body  *=  ${message}
