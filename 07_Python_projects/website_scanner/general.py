import os

def create_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def write_file(path, data):
    with open(path, 'w') as f:
        f.write(data)
        f.close()