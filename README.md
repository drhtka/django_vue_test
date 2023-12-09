##  Full Stack Developer Test Task

### Functionality

1. **Login Page:**
    - Create a simple login page (registration not needed).
    - The authentication solution is up to you.

2. **Task List Page:**
    - Develop a one-page application to display a list of tasks.
    - Include a simple form for adding new tasks.
        - Each task should have a caption and a body for a description.

### Technical Requirements

1. **Backend:**
    - Use Django for the backend.

2. **Frontend:**
    - Use Vue.js for the frontend.
    - Choose between:
        - Django Templates + Vue.js
        - Django Rest API + separate Vue.js frontend

3. **Database:**
    - Persist tasks into a database of your choice.

4. **Docker Container:**
    - Package the solution into a Docker container for easy deployment.


5. **Git Repository:**
    - Provide access to the Git repository with the final solution.


###  Submission Guidelines




### Create settings your IP http://your_IP:8000

```sh
settings.py

CORS_ORIGIN_WHITELIST = [
    ...
    'http://your_IP:8000',
    'http://your_IP:8080',
]
```

### Create settings your IP http://your_IP:8000

```sh
App.vue

    return {
        baseUrl: "http://your_IP:8000",
        posts: [],
    };
```
### Running the Project

1. Navigate to the project root in the command line.

2. Execute the following command to create and start the containers:
```bash
docker-compose up --build -d
```
3. Open the Application
   Click here to open the application on your ip  http://your_ip:8000.