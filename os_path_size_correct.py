import os

totalSize = 0
for filename in os.listdir('C:\\Users\\SNEAKY\\Desktop\\AutomateTheBoringStuff'):
    if not os.path.isfile(os.path.join('C:\\Users\\SNEAKY\\Desktop\\AutomateTheBoringStuff', filename)):
        continue
    totalSize = totalSize + os.path.getsize(os.path.join('C:\\Users\\SNEAKY\\Desktop\\AutomateTheBoringStuff', filename))

print(totalSize)
