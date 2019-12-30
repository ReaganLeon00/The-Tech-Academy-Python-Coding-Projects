import os
import time
filePath = "C:\\Users\\maggi\\OneDrive\\Desktop\\TECH ACADEMY\\python_projects\\PG 100"
directoryFiles = os.listdir(filePath)

for file in directoryFiles:
    if file.endswith(".txt"):
        absolutePath = os.path.join(filePath, file)
        modificationTime = os.path.getmtime(absolutePath)
        legibleTime = time.ctime(modificationTime)
        print(legibleTime)
        print(file)
    




