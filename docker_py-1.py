import docker

# This is used to connect to docker deamon
client = docker.from_env()

# Enter the image name here
image= input("Enter the image name :")

# Enter the container name here
name = input("Enter the container name : ")

# it is used to create the container using run method
container = client.containers.run(image,name=name,detach=True)

# it is used to list all the containers using list method
list_container = client.containers.list(all=True)


for lst in list_container:
    # Here we have used the for loop to list all the container's name and their status
    print(f"name:{lst.name} status:{lst.status}")

# it is used to get the containers on the basis of container's name
rm_container = client.containers.get(f"{name}")
print(f"removing this container : {rm_container.name}")

# it is used to remove the container
rm_container.remove(force=True)
print(f"{rm_container.name}:it is successfully removed")