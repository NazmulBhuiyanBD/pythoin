"""#allows you to perform a wide variety of tasks, such as reading and writing files, interacting with the file system, and running system commands.
import os
#os.mkdir("data")
for i in range(30):
    #os.mkdir(f"data/days{i+1}")   this will create new file
    os.rename(f"data/days{i+1}",f"tutorial {i*10}")

"""

import os
folder=os.listdir(f"data")
print(folder)

for i in folder:
    print(os.listdir(f"data/{folder}"))