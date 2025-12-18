import docker

# Connection to docker
client = docker.from_env()

# list images
images = client.images.list()
for img in images:
    print(img.id, img.tags)

# pull an image
client.images.pull("nginx", tag="latest")

# delete an image
client.images.remove("nginx:latest", force=True)

# Create and run a container
container = client.containers.run(
    image="nginx:latest",
    name="my_nginx",
    ports={"80/tcp": 8080},
    detach=True #background
)

# get container by id
container = client.containers.get("my_nginx")

# logs
logs = container.logs()
print(logs.decode())

# stop
container.stop()

# start
container.start()

# restart
container.restart()

# remove
container.remove(force=True)

# exec a command inside the container
exec_result = container.exec_run("nginx -v")
print(exec_result.output.decode())

#list of networks
networks = client.networks.list()

# create a network
network = client.networks.create("my_network", driver="bridge")

# connect a container to a network
network.connect(container)

# remove a network
network.remove()

# list of volumes
volumes = client.volumes.list()

# create a volume
volume = client.volumes.create(name="my_volume")

# delete a volume
volume.remove()


# indo Docker
info = client.info()
print(info)

# version Docker
version = client.version()
print(version)
