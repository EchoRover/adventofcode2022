


def getInput():

    file = open("q7data.txt")

    data = file.read().split("\n")

    return data 




class Directory:

    def __init__(self,name,size = None,parent = None):
        self.type = "dir"
        self.name = name
        self.size = size
        self.parent = parent
        self.sub_directories = []

    def add_something(self,thing):
        self.sub_directories.append(thing)

    def get_something(self,directory):
        for thing in self.sub_directories:
            if thing.name == directory:
                return thing
        return None

    def calculateSize(self):
        size = 0
        for thing in self.sub_directories:
            if not thing.size:
                thing.calculateSize()
            size += thing.size
        self.size = size





class File:
    def __init__(self,name,size):
        self.type = "file"
        self.name = name
        self.size = size


def get_sizes_max(data):

    data.pop(0)
    root = Directory("/")

    current_directory = root

    for command in data:

        command_parts = command.split()

        if command_parts[0] == "$":
            if command_parts[1] == "cd":
                
                if command_parts[-1] == "..":
                    current_directory = current_directory.parent
                else:
                    current_directory = current_directory.get_something(command_parts[-1])
                    if not current_directory:
                        current_directory = root
        else:
            if command.startswith("dir"):
                current_directory.add_something(Directory(command_parts[-1],parent = current_directory))
            else:
                current_directory.add_something(File(command_parts[-1],int(command_parts[0])))

    root.calculateSize()


    #print([(i.name,i.size) for i in root.sub_directories])
    
    size = atmost(root,100000)
    
    print("closest directories to remove are", sum(size))

    #part 2

    size_left = 70000000 - root.size

    needed = 30000000 - size_left

    #print(size_left,needed)

    new_size = atleast(root,needed)
    
    print("smallest to remove",min(new_size))



def show_directors(root,level = 0):

    print("  " * level + "-"+root.name + " (dir)"+f" ({root.size})")
    level += 1


    for thing in root.sub_directories:
        if thing.type == "dir":
            show_directors(thing,level)
        else:
            print("    " * level + thing.name + f" ({thing.size})")


def atmost(root,value):

    sizes = []

    for subdir in root.sub_directories:
        if subdir.type == "dir":
            if subdir.size <= value:
                sizes.append(subdir.size)

            sizes.extend(atmost(subdir,value))

    return sizes

def atleast(root,value):

    sizes = []

    for subdir in root.sub_directories:
        if subdir.type == "dir":
            if subdir.size >= value:
                sizes.append(subdir.size)

            sizes.extend(atleast(subdir,value))

    return sizes












data = getInput()
get_sizes_max(data)