import sys, os

rootpath = os.path.dirname(__file__)
path_folder1 = os.path.join(rootpath, "folder1")
path_folder2 = os.path.join(rootpath, "folder2")


os.system("cls||clear")
print("="*100)

print (rootpath)
print(path_folder1)

print("="*100)

sys.path.append(path_folder1)
sys.path.append(path_folder2)

import module1, module2