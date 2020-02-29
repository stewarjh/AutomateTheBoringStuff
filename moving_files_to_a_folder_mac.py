# Move File Types From One Folder to Another
import os, shutil


def getFromFolder():
	print('Where do you want to get the file from?')
	return input()


def getToFolder():
	print('Where do you want to put your file?')
	return input()


def chooseFileType():
	print('What file type do you want to move? EX: .txt, .py, .png, etc...')
	return input()


def moveFileTypes(fromFolder, toFolder, fileType):
	for folderName, subfolders, filenames in os.walk(fromFolder):
		for file in filenames:
			if file.endswith(fileType): # can move file types by [if file.endswith('.py'):]
				fullyQualifiedFile = fromFolder + os.sep + file
				shutil.copy(fullyQualifiedFile, toFolder)
				os.remove(fullyQualifiedFile)


def app():
	fileType = chooseFileType()
	fromFolder = getFromFolder()
	toFolder = getToFolder()
	moveFileTypes(fromFolder, toFolder, fileType)


app()