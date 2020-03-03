# Move File Types From One Folder to Another
import os, shutil


# Folder that file or files are located.
def getFromFolder():
	return str(input('Where do you want to get the file from?\n'))


# Folder where file or files will be moved.
def getToFolder():
	return str(input('Where do you want to put your file?\n'))


# Uses file type EX .py .txt. png to select multiple files.
def chooseFileType():
	return str(input('What file type do you want to move? EX: .txt, .py, etc...\n'))


# Uses the filename to select file .
def fileName():
	return str(input('What file do you want to move? EX: HelloWorld.txt\n'))


# Selects folder you want to move.
def subFolderName():
		return str(input('Enter Selected folder name:\n'))


# Moved folders location.
def moveFolderTo():
	return str(input('Enter folder destination:\n'))


# Moves a folder to another location
def moveFolder(selectFolder, moveFolder):
	shutil.move(selectFolder, moveFolder,)


# Moves file or files of the same type to another folder.
def moveFileTypes(fromFolder, toFolder, fileType):
	for folderName, subfolders, filenames in os.walk(fromFolder):
		for file in filenames:
			if file.endswith(fileType): # can move file types by [if file.endswith('.py'):]
				fullyQualifiedFile = fromFolder + '\\' + file
				shutil.copy(fullyQualifiedFile, toFolder)
				os.remove(fullyQualifiedFile)


# Moves a file from one location to another.
def moveFileName(fromFolder, toFolder, thisFile):
	for folderName, subfolders, filenames in os.walk(fromFolder):
		for file in filenames:
			if file == thisFile: # can move file types by [if file.endswith('.py'):]
				fullyQualifiedFile = fromFolder + '\\' + file
				shutil.copy(fullyQualifiedFile, toFolder)
				os.remove(fullyQualifiedFile)


# Commands to move folder
def appfolderMove():
	selectFolder = subFolderName()
	folderMoveTo = moveFolderTo()
	moveFolder(selectFolder, folderMoveTo)


# Used to call moveFileType
def appMoveFileType():
	fileType = chooseFileType()
	fromFolder = getFromFolder()
	toFolder = getToFolder()
	moveFileTypes(fromFolder, toFolder, fileType)


# Used to call moveFileName
def appMoveFileName():
	fromFolder = getFromFolder()
	toFolder = getToFolder()
	thisFile = fileName()
	moveFileName(fromFolder, toFolder, thisFile)
