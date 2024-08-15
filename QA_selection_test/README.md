# Test QA Suite
Demo test for new QA's.

The test consists of executing an automation script towards the URL specified in the .env.example.

For init the project you must copy .env.example to .env

it will be valued to do all the test case.

In this project you got all you need for the test with docker :).

You must have install docker and docker-compose in your computer for use this skeleton.

- more information docker [here](https://www.docker.com/).
- more information docker-compose [here](https://docs.docker.com/compose/)

### If you don't know docker, please still do the test and us will valorated your code. I'll Appreciate so much docs and writen brief explanation with details that you consider importants 


## Points to consider in the evaluation:
- It'll be considered to use page object model pattern.
- It's recomended to validate error cases, for example: wrong Login, field with specific formats entered wrongly.
- test's segmentation.


## Getting started

Use this project to run the automated test in docker.
Commands:

### example command
docker compose exec app python3 -m pytest -rP test/test_demo.py

## Test Cases

- Case 1: Fill out all fields of the "Practice Form" with random values.  

- Case 2: Fill out all the form fields to create a new user with random values.  

- Case 3: In the section Widgets/Select Menu, select the next values:  
    - Option Select Value: A root option  
    - Option Select One:  Ms.  
    - Option Old Style Select Menu: Indigo  
    - Option Multiselect drop down: Blue and Red,   
    - Option Standard multi select: Volvo and Opel.  

- Case 4: In the section Elements/Web Tables:  
    - Add a new element with random values.  
    - Edit the new element.  
    - Delete the new element.  

- Case 5: In the section Elements/Web Tables fill the new element form with incorrect format and empty fields.  
