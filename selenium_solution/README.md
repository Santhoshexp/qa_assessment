# Selenium-Based Web Page Content Testing

This repository contains a Python script for automated testing of web page content using Selenium. The script verifies that a specific text is present on a web page.

## Modules Used

- **Selenium**: For browser automation.
- **pytest**: For running the test cases.
- **webdriver_manager**: For downloading the latest webdriver automatically.

## Steps to execute

- pytest --browser <browser names> .
- Brower names - chrome (default) , edge , firefox
- Sample command - pytest --browser edge test_problem1.py

## Sample output

![image](https://github.com/user-attachments/assets/9f35fbff-a95e-4d47-9d5f-0d835e9d93e2)


## Note

Replace the url of the frontend service in the conftest file at line 26
   
