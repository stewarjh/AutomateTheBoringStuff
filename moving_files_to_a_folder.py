# Move File Types From One Folder to Another
import os, shutil

def getFromFolder():
	print('Where do you want to get the file from? EX: C:\\\\Users\\\\SNEAKY\\\\Desktop\\\\AutomateTheBoringStuff2')
	return input()


def getTwoFolder():
	print('Where do you want to put your file? EX: C:\\\\Users\\\\SNEAKY\\\\Desktop\\\\AutomateTheBoringStuff2')
	return input()


def chooseFileType():
	print('What file type do you want to move? EX: .txt, .py, .png, etc...')
	return input()


def moveFileTypes(moveFiles, whereTwo, fileType):
	for folderName, subfolders, filenames in os.walk(moveFiles):
		for file in filenames:
			if file.endswith(fileType): # can move file types by [if file.endswith('.py'):]
				shutil.copy(file, whereTwo)
				os.remove(moveFiles + '\\' + file)


fileType = chooseFileType()
moveFiles = getFromFolder()
whereTwo = getTwoFolder()

moveFileTypes(moveFiles, whereTwo, fileType)

