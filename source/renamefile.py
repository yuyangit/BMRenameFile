#-*- coding:utf-8 -*-

import os
import re
import sys, getopt

class RenameMode:

	onlyFile=0
	onlyDir=1
	both=2

def renamefiles(origText, targetText, currentPath="", renameType=0):

	if os.path.exists(currentPath) == False:
		currentPath = os.getcwd()
	print("处理中...")
	for dirMap in os.walk(currentPath):
		if renameType == RenameMode.onlyFile:
			for fileName in dirMap[2]:
				filePath = os.path.realpath(dirMap[0])+"/"+fileName
				if origText in fileName:
					resultName = fileName.replace(origText, targetText)
					resultPath = os.path.realpath(dirMap[0])+"/"+resultName
					os.rename(filePath, resultPath)

		elif renameType == RenameMode.onlyDir:
			for dirName in dirMap[1]:
				dirPath = os.path.realpath(dirMap[0])+"/"+dirName
				if origText in dirName:
					resultName = dirName.replace(origText, targetText)
					resultPath = os.path.realpath(dirMap[0])+"/"+resultName
					print(dirPath, resultPath)
					os.rename(dirPath, resultPath)
					
		elif renameType == RenameMode.both:

			for dirName in dirMap[1]:
				dirPath = os.path.realpath(dirMap[0])+"/"+dirName
				if origText in dirName:
					resultName = dirName.replace(origText, targetText)
					resultPath = os.path.realpath(dirMap[0])+"/"+resultName
					os.rename(dirPath, resultPath)
					
			for fileName in dirMap[2]:
				filePath = os.path.realpath(dirMap[0])+"/"+fileName
				if origText in fileName:
					resultName = fileName.replace(origText, targetText)
					resultPath = os.path.realpath(dirMap[0])+"/"+resultName
					os.rename(filePath, resultPath)
	print("处理成功!!!")


if __name__ == "__main__":
	import sys
	# :org:tgt:path:mode
	import argparse
	parser = argparse.ArgumentParser(description='这是一个批量修改文件名和文件的脚本.')
	parser.add_argument("org_string",
					help="将要被替换的字符串")
	parser.add_argument("tgt_string",
				help="将要被替换的字符串")
	parser.add_argument("-o", "--org",
						help="将要被替换的字符串")
	parser.add_argument("-t", "--tgt",
						help="需要的字符串")
	parser.add_argument("-p", "--path",
						help="指定目录")
	parser.add_argument("-m", "--mode", type=int,
						help="替换模式")

	args = parser.parse_args()
	org_string = ""
	if args.org != None:
		org_string = args.org
	else:
		org_string = args.org_string

	tgt_string = ""
	if args.tgt != None:
		tgt_string = args.tgt
	else:
		tgt_string = args.tgt_string

	current_path = ""
	if args.path != None:
		current_path = args.path

	mode = args.mode
	if mode == None:
		mode = 0

	if org_string == "" and tgt_string == "":
		if len(sys.argv) == 2:
			if sys.argv[1] == "-h" or sys.argv[1] == "help":
				print('''
1) 第一个参数为将要被替换的字符串
2) 第二个参数为将要替换的字符串
3) 第三个参数为指定目录
4) 第四个参数为替换模式:
	0. 仅替换文件名
	1. 仅替换目录名
	2. 替换文件名与目录名
					''')
			else:
				print("请输入 \"BMRenameFile help\" 参数帮助.")
		
		if len(sys.argv[1]) > 0 and len(sys.argv[2]) > 0:
			renamefiles(sys.argv[1], sys.argv[2], current_path, mode)
		else:
			print("请输入 \"BMRenameFile help\" 参数帮助.")
	else:
		renamefiles(org_string, tgt_string, current_path, mode)

