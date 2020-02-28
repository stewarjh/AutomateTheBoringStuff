# Modules imported to complete def below no third party modules use pip installer.
import os, shutil


# This def gathers input for file location you want to collect.
def getFromFolder():
	print('Where do you want to get the file from? EX: C:\\\\Users\\\\SNEAKY\\\\Desktop\\\\AutomateTheBoringStuff2')
	return input()


# This def gathers a user input for a location it wants to send.
def getTwoFolder():
	print('Where do you want to put your file? EX: C:\\\\Users\\\\SNEAKY\\\\Desktop\\\\AutomateTheBoringStuff2')
	return input()


# This def chooses a file type.
def chooseFileType():
	print('What file type do you want to move? EX: .txt, .py, .png, etc...')
	return input()


def chooseFileName():
	print('What file do you want to move? EX: C:\\\\Users\\\\SNEAKY\\\\Desktop\\\\AutomateTheBoringStuff2\\\\bacon.text' )
	return input()

# This def moves file types from one folder to another
def moveFileTypes(moveFiles, whereTwo, fileType):
	for folderName, subfolders, filenames in os.walk(moveFiles):
		for file in filenames:
			if file.endswith(fileType):  # Can detect file types by [if file.endswith('.py'):]
				shutil.copy(file, whereTwo)  # Used to move the file to new location.
				os.remove(moveFiles + '\\' + file)  # Used to delete file from moved from  location .

fileType = chooseFileType()
moveFiles = getFromFolder()
whereTwo = getTwoFolder()

# This def moves file types from one folder to another
def moveFileName(moveFiles, whereTwo, fileName):
	for folderName, subfolders, filenames in os.walk(moveFiles):
		for file in filenames:
			if file(fileName):  # Can detect file by path and name.
				shutil.copy(file, whereTwo)  # Used to move the file to new location.
				os.remove(moveFiles + '\\' + file)  # Used to delete file from moved from  location .


fileName = chooseFileType()
moveFiles = getFromFolder()
whereTwo = getTwoFolder()

# DEF CAll LIST remove # to call a def.
#moveFileTypes(moveFiles, whereTwo, fileType)
moveFileName(moveFile, whereTwo, fileName)
