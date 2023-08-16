# Logs Manager API

SVIT IT Logs Manager API Python Task by Babilia Oleksandr

## Technologies Used

- Backend: Python with FastAPI for building the server-side logic.
- Database: SQLite for storing user and log information.
- Authentication and Authorization: JSON Web Token (JWT) for secure user authentication and authorization.
- Testing: PyTest for writing and running backend tests, ensuring code reliability.
- Additional Tools: Docker for containerization

## Getting Started

### Run Server

1. Build the images and run the containers:

    `$ docker-compose up -d --build`

2. You can make api calls through SwaggerUI at http://0.0.0.0:8000/docs:

3. Test it out at http://0.0.0.0:8000. The "app" folder is mounted into the container and your code changes apply automatically.

#### Running Tests in Development 

`$ docker-compose exec api pytest`
    
NOTE: Before you execute the command above. The containers must me up an running.

## API Features

1. Authentication
2. Upload logs in .txt files
3. Upload logs in .zip archives
4. Get logs by keyword
5. Get logs by time
6. Get logs by keyword and time

## API Endpoints

Some endpoints require a token for authentication. The API call should have the token in Authorization header.

    `{'Authorization': 'Bearer': <token>}`


| EndPoint                                        |                            Functionality |
| ------------------------------------------------|----------------------------------------: |
| GET /api/users/                                 |                         Get all users    |
| GET /api/users/:id/                             |                    Get one user by id    |
| POST /api/auth/signup/                          |                           Signup user    |
| POST /api/auth/login                            |                            Login user    |
| GET /api/logs/                                  |  Get logs by keyword or/and timestamp    |
| POST /api/logs/upload/                          |                            Upload Log    |

## Responses

The API responds with JSON data by default.

## Request examples

Request GET /api/logs/

curl -H "Authorization: Bearer <your_token>" -H "Content-Type: application/json" https://0.0.0.0:8000/api/logs/


