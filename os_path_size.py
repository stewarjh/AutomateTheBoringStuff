import os

totalSize = 0

filesATBS = os.listdir('C:\\Users\\SNEAKY\\Desktop\\AutomateTheBoringStuff')

for f in filesATBS:
    if not os.path.isfile(os.path.join('C:\\Users\\SNEAKY\\Desktop\\AutomateTheBoringStuff', f)):
        continue
    totalSize = totalSize + os.path.getsize(os.path.join('C:\\Users\\SNEAKY\\Desktop\\AutomateTheBoringStuff', f))
print(totalSize)
