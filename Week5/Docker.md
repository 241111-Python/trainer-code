# Docker
## The fastest you've ever created and destroyed something.

Docker is a containerization tool. It allows us to bundle up and transport not just source code, or an executable, but the entire environment that an application may need to run. Dependencies, runtime environment, even an opperating system.

Docker uses some basic concepts to get things rolling, and gets more complicated the more you want to do.
- Dockerfile: A Dockerfile is the scripted set of commands that we develop to instruct Docker how to build an image. This can be simple (leveraging existing images that we can get from a repository) or complex (like building from the ground up), but generally is done from the perspective of "my computer is brand new out of the box. What do I need to run my application?"
- Image: an image is the blueprint for a container. Images are portable, and do not interact with processing. The image is just the manual, not the actual labor to build something.
- Container: the container is the virtualized environment for an application. Commonly illustrated as shipping containers, they are the segment of your systems processing and memory that will be allocated to the program that is packaged up inside them. Containers are ephemeral, or temporary. They are meant to be created, used, and destroyed. RARELY do we need to keep a runing container around. instead, we stop the running processes inside the container, destroy the container (to free up the allocated memory and processor) and just create a new container based on the plan (the image for the container) when we need a new one.

We will be leveraging an existing image that we will retreive from Docker Hub (Dockers official container registry), so we do not need to write our own Dockerfile. With an existing image, we'll be able to start a container with one command.

We will need a few basic commands to manage our environment, and the containers that we'll be using.
- docker run ...
    - this will be the command we use to start a new container. we'll add additional information to the command to specify what image to use, what to name the container that it will create, and any environmental variables that we need to let the container know about.
- docker ps
    - this is a shorthand command that will list any actively running containers - NOT all containers. We can stop a container without deleting it.
- docker container ls -a
    - this will list all containers, running or stopped.
- docker container stop <name>
    - tell docker to make coffee. No, but really it's pretty straight forwards. stop the named container.
- docker container rm <name>
    - remove a stopped container
- docker container start <name>
    - remember that we can start and stop a container without deleting it if we want, but generally we can delete it!



# PostgreSQL
## A quickstart to running a postresql database.

- In terminal run:  
`docker run --name <container-name> -e POSTGRES_PASSWORD=<DB-Password> -p 5432:5432 -d postgres`

- Connect using the connection manager of your choice (I like the PostgreSQL Explorer VS Code extension)

- Profit