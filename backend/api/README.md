Running it with Docker:\
Note: Your CWD is supposed to be insite the /api directory.\
Build the image: 

    docker build -t auth-api .

Run the container:

    docker run --name auth-api -dp 127.0.0.1:5000:5000 auth-api

Access http://localhost:5000/ and see the welcome

Some useful Docker commands:

    docker ps -a                            # Lists all containers.
    docker images                           # Lists all images.
    docker start <container_id_or_name>     # Start a stopped container.
    docker stop <container_id_or_name>      # Try to stop a container.
    docker kill <container_id_or_name>      # Kill a container. (Force it to stop).
    docker rm <container_id_or_name>        # Remove a container
    docker image rm <container_id_or_name>  # Remove a image

    # Gets a shell inside a running container.
    docker exec -it <container_id_or_name> /bin/bash 

Running it with Python's virtual environment (without Docker):

    python -m venv venv                 # If python fails, try python3 instead.
    source venv/bin/activate (Linux) OR venv\Scripts\activate (Windows)
    pip install -r requirements.txt     # If pip fails, try pip3 instead.     
    deactivate                          # To exit the virtual environment.

To VSCode recognize your venv (if it didn't do that automatically):

    When using venv type 'which python3'    # Or 'which python'
    Copy the path.
    In VSCode, press Ctrl + Shift + P
    select 'Python: Select Interpreter', then
    'Enter interpreter path...'
    and paste the path to venv's python interpreter, then press enter.


