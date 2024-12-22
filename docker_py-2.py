import os
from dotenv import load_dotenv
import docker

# to call the docker daemon module
client = docker.from_env()

# it is used to call the dotenv module
load_dotenv()

# load the username from the .env file
docker_username = os.getenv("DOCKER_HUB_USERNAME")

# load the password from the .env file
docker_password = os.getenv("DOCKER_HUB_PASSWORD")
image_name = "nginx-file"
repository_name = f"{docker_username}/{image_name}"
tag = "v-1"
name=input("Enter the name of the container here:")

def pull_and_create():
    # to login into the docker hub using the username and password
    client.login(username=docker_username,password=docker_password)

    # pulling of image from the docker hub
    pulled_image = client.images.pull(repository_name,tag=tag)
    print(f"pulling image is {pulled_image.tags}")

    # creating the container using the image which was pulled above
    container = client.containers.run(f"{repository_name}:{tag}",name=name,detach=True)
    print(f"container {container.name} is creating ")

pull_and_create()