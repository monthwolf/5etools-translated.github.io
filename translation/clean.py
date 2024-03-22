#!/usr/bin/env python3
import re
import argparse

parser = argparse.ArgumentParser(description='Delete all broken translations')
parser.add_argument('files', type=str, nargs='*')
parser.add_argument('--maxfiles', type=int, default=150)
args = parser.parse_args()

start=0
#print(args.files)
def clean_files(log:str,logs:list):
	num=args.maxfiles
	for file in args.files[start:]:
		with open(file,"r+") as data:
			#清理包含未替换变量、输出不完整、未翻译、输出丢失变量的错误翻译映射
			text=re.sub(r'.*?(%?\d+%|%num%).*\n|.*?\{\d\}.*\n|.*?:([^a-zA-Z\n]+).*?(\[\.*\].*|[a-zA-Z]+",?)\n|".*?:[^\u4e00-\u9fa5]+",?\n|.*?\{.*?\}.*?:[^\{\}\n]+",?\n', '', data.read())
			text=re.sub(r',\n\s*\}','\n}',text)
			data.seek(0)
			data.truncate()
			data.write(text)
			logs[1]=file
			log.seek(0)
			log.truncate()
			log.write('\n'.join(logs))
			data.close()
			num-=1
			print(data.name+"清理完毕")
		if(num==0):
			break
	log.close()
if __name__ == "__main__":
	try:
		with open('log.txt','r+') as log:
			logs=str.split(log.read(),'\n')
			if len(logs)==2 and logs[0]==str(args.files):
				# print(logs[1])
				# print(args.files.index(logs[1]))
				start=args.files.index(logs[1])
				if args.files[-1]==logs[1]:
					start=0
			else:
				logs[0]=str(args.files)
			clean_files(log,logs)
	except FileNotFoundError:
		log=open('log.txt','w+')
		logs=['','']
		logs[0]=str(args.files)
		clean_files(log,logs)
