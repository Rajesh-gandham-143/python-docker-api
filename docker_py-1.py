import docker

client = docker.from_env()

image= input("Enter the image name :")
name = input("Enter the container name : ")
container = client.containers.run(image,name=name,detach=True)

list_container = client.containers.list(all=True)

for lst in list_container:
    print(f"name:{lst.name} status:{lst.status}")

rm_container = client.containers.get(f"{name}")
print(f"removing this container : {rm_container.name}")
rm_container.remove(force=True)
print(f"{rm_container.name}:it is successfully removed")