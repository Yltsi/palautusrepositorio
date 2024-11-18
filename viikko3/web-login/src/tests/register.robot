*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  newuser
    Set Password  newpass123
    Set Password Confirmation  newpass123
    Submit Registration
    Registration Should Succeed

Register With Too Short Username
    Set Username  a
    Set Password  validpass123
    Set Password Confirmation  validpass123
    Submit Registration
    Registration Should Fail With Message  Username must be at least 3 characters long

Register With Invalid Username
    Set Username  user123
    Set Password  validpass123
    Set Password Confirmation  validpass123
    Submit Registration
    
Login After Successful Registration
    Set Username  newuser
    Set Password  newpass123
    Set Password Confirmation  newpass123
    Submit Registration
    Registration Should Succeed
    Go To Ohtu Page
    Click Button  Logout    # tai voimme käyttää Submit Logout -avainsanaa
    Go To Login Page
    Set Username  newuser
    Set Password  newpass123
    Submit Login
    Main Page Should Be Open

Login After Failed Registration
    Set Username  ab
    Set Password  newpass123
    Set Password Confirmation  newpass123
    Submit Registration
    Registration Should Fail With Message  Username must be at least 3 characters long
    Go To Login Page
    Set Username  ab
    Set Password  newpass123
    Submit Login
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Reset Application And Go To Register Page
    Reset Application
    Go To Register Page

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Submit Registration
    Click Button  Register

Registration Should Succeed
    Welcome Page Should Be Open

Registration Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Login
    Click Button  Login

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}
Go To Ohtu Page
    Go To  ${HOME_URL}/ohtu
