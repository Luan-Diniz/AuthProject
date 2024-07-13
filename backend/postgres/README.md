Testing the service with Docker (No volumes are created):

    docker build -t auth-postgres .
    docker run --name postauthcontainer -e POSTGRES_USER=postgres_user -e POSTGRES_PASSWORD=password -e POSTGRES_DB=mydb -dp 5432:5432 auth-postgres
    # Acessing the container with psql
    psql -h localhost -p 5432 -U postgres_user mydb

