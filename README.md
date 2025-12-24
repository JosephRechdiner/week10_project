# Contact Project:

## Purpose:

The final purpose of the project is,
to make clients able to save their contacts in mysql database through their local host using fastapi.

## Set up:

The setup is very simple:
    - Go to your terminal 
    - Make a directory for the program
    - Clone the github URL, "git clone https://github.com/JosephRechdiner/week10_project.git"
    - cd into it
    - Type "docker compose up" (add -d if you want the program to run in the backround)

    Thats it!
    The program is runnig!
    All you have to do next is, go to your browser, type: "127.0.0.1:8000" (add "/docs" if you want to use fastapi swagger) and test the routes!

To stop the program:
    - Go back to your terminal
    - Make sure you're under the correct directory and type "docker compose down".

## Database connection Info:

First we need to initialize connection to the database and use it every time we want to operate somthing in it.
    -"database" - dir
        - create_connection.py - file: has one function to get connection to the database

fastapi has some special method called "Depends()", this function activate the function it recieves and initialize the result into some variable.
fastapi also knows to stop the reading of the file and wait for the result of the above.

## The app container Info:

I decided to divide the whole programing proccess into 3 layers:

    - Application layer ("routes" dir) - responsible for creating fastapi routes the user sees in the browser, and sending the request to the service layer.
        - GET/ : get all contacts
        - POST/ : add contact
        - PUT/ : update contact (by id)
        - DELELE/ : delete contact (by id)

        - obviously HTTP exeption will be raise if needed

    - Service layer ("service" dir) - responsible for sending the request next to the dal layer to make CRUD operations, and returning the right response.
        - status code 200 - the function will send whats relevant.
        - status code 404 - the contact the user is asking to operante is not in the database.
        - status code 409 - the access to the database has failed.

    - Dal layer ("dal" dir) - responsible for making CRUD operations and returning boolean variable for indecate success.

## The db container Info:

Build the containerrom the official mysql image.