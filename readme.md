The first step is to Setup Docker on your pc:
1. Make sure Docker is installed on your machine as well as Docker compose.
2. Clone the repository and go to the root directory in terminal.
3. Build the Docker image: "docker-compose up --build -d
"
4. You can open browser and navigate to - "http://localhost:5000" to access application and its APIs.
5. To stop the services and remove the associated Docker containers one can use the command -"docker-compose down"


For Testing you can use Postman or any other application
Use Postman to send requests to `http://localhost:5000/users` and other endpoints which are included as follows:
GET /users - Returns a list of all users.
GET /users/<id> - Returns the user with the specified ID.
POST /users - Creates a new user with the specified data.
PUT /users/<id> - Updates the user with the specified ID with the new data.
DELETE /users/<id> - Deletes the user with the specified ID.

for each GET request you will get an id key in response which is to be included at the appropriate place in URL as given above:
