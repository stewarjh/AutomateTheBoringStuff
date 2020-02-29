# Move File Types From One Folder to Another
import os, shutil


def getFromFolder():
	print('Where do you want to get the file from? EX: C:\\\\Users\\\\')
	return input()


def getToFolder():
	print('Where do you want to put your file? EX: C:\\\\Users\\\\')
	return input()


def chooseFileType():
	print('What file type do you want to move? EX: .txt, .py, etc...')
	return input()

def fileName():
	print('What file do you want to move? EX: HelloWorld.txt')
	return input()


def moveFileTypes(fromFolder, toFolder, fileType):
	for folderName, subfolders, filenames in os.walk(fromFolder):
		for file in filenames:
			if file.endswith(fileType): # can move file types by [if file.endswith('.py'):]
				fullyQualifiedFile = fromFolder + '\\' + file
				shutil.copy(fullyQualifiedFile, toFolder)
				os.remove(fullyQualifiedFile)


def moveFileName(fromFolder, toFolder, thisFile):
	for folderName, subfolders, filenames in os.walk(fromFolder):
		for file in filenames:
			if file == thisFile: # can move file types by [if file.endswith('.py'):]
				fullyQualifiedFile = fromFolder + '\\' + file
				shutil.copy(fullyQualifiedFile, toFolder)
				os.remove(fullyQualifiedFile)


def app():
	fileType = chooseFileType()
	fromFolder = getFromFolder()
	toFolder = getToFolder()
	moveFileTypes(fromFolder, toFolder, fileType)


def app2():
	fromFolder = getFromFolder()
	toFolder = getToFolder()
	thisFile = fileName()
	moveFileName(fromFolder, toFolder, thisFile)


#app()


app2()