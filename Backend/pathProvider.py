import os

def getPathToModels(name):
    package_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(package_dir + "/models/" + name)