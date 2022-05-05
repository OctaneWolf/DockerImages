from os import listdir,getcwd
from os.path import isfile, join
import docker
cpath = str(getcwd())
client = docker.from_env()
dirs = [f for f in listdir(cpath) if not isfile(join(cpath, f))]
dirs.remove(".git")
print(dirs)
for x in dirs:

    client.images.build(path=str(cpath+"/"+x), buildargs={'tags':'test'} , tag=str("octanewolf/"+x))

with open('images.list', 'w') as f:
    f.write(str(dirs))