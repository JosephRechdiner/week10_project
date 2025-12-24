# Contact Project

## Purpose
The final purpose of the project is to allow clients to save their contacts in a MySQL database through their localhost using FastAPI.

## Setup
The setup is very simple:

1. Open your terminal.
2. Make a directory for the program.
3. Clone the GitHub repository:
   ```bash
   git clone https://github.com/JosephRechdiner/week10_project.git
   ```
4. Change into the project directory:
   ```bash
   cd week10_project
   ```
5. Start the containers:
   ```bash
   docker compose up
   ```
   Add `-d` if you want the program to run in the background.

The program is now running!  
- Go to your browser and type `127.0.0.1:8000`.  
- Add `/docs` to the URL if you want to use FastAPI Swagger to test the routes.

To stop the program:
```bash
docker compose down
```

## Database Connection Info
We need to initialize a connection to the database and use it every time we want to operate on it.

- `database` directory
  - `create_connection.py` — contains one function to get a connection to the database.

FastAPI has a special method called `Depends()`, which activates the function it receives and initializes the result into a variable. FastAPI also waits for the result before continuing execution.

## App Container Info
The project is divided into three layers:

1. **Application Layer (`routes` directory)**  
   Responsible for creating FastAPI routes visible to the user and sending requests to the service layer.  
   Routes:
   - `GET /` — get all contacts
   - `POST /` — add contact
   - `PUT /` — update contact by ID
   - `DELETE /` — delete contact by ID  

   HTTP exceptions will be raised if needed.

2. **Service Layer (`service` directory)**  
   Responsible for sending requests to the DAL layer to perform CRUD operations and returning appropriate responses:  
   - Status code 200 — returns relevant data
   - Status code 404 — contact not found in the database
   - Status code 409 — database access failed

3. **DAL Layer (`dal` directory)**  
   Responsible for making CRUD operations and returning boolean values to indicate success.

## DB Container Info
Built from the official MySQL image.

