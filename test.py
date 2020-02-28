import os

for folderName, subfolders, filenames in os.walk('C:\\Users\\SNEAKY\\Desktop\\AutomateTheBoringStuff2'):
	print('The folder is ' + folderName)
	print('This subfolders in ' + folderName + ' are: ' + str(subfolders)
	print('This filesname in ' + folderName + ' are: ' + str(filenames))
    print()