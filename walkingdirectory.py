import os

for folderName, subfolders, filenames in os.walk('C:\\Users\\SNEAKY\\Desktop\\AutomateTheBoringStuff2'):
	print(folderName)
	print(subfolders)
	print(filenames)


