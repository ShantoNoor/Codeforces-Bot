import requests as req
import re
import os
import sys

def createFile(name, src):
	with open (name, 'w') as f:
		f.write(src)


def readFile(name, src):
	content = ''
	with open (name, 'r') as f:
		content = f.read()

	return content


main_path = os.getcwd()
cpp_template = readFile('cpp_template.txt', main_path)
py_template = readFile('py_template.txt', main_path)

def genIOS(problem_url, path):
	cf = req.get(problem_url).text

	title_pattern = r'<div class="title">(.*?\. .*?)</div>'
	title = re.search(title_pattern, cf)
	title = title.group(1)

	pattern = re.compile(r'<pre>\n((\n|.)*?)</pre>')
	matches = pattern.finditer(cf)

	res = []
	for match in matches:
		res.append(match.group(1))

	os.chdir(path)
	os.mkdir(title)
	print(f'\t{title}\\') #<-p
	path = os.path.join(path, title)
	os.chdir(path)

	createFile(f'{title}.py', py_template)
	print(f'\t\t{title}.py') #<-p
	createFile(f'{title}.cpp', cpp_template)
	print(f'\t\t{title}.cpp') #<-p

	j = 1
	for i in range(0, len(res), 2):
		if i == 0:
			createFile(f'input.txt', res[i])
			print(f'\t\tinput.txt') #<-p
			createFile(f'output.txt', res[i+1])
			print(f'\t\toutput.txt') #<-p
		else:
			createFile(f'input{j}.txt', res[i])
			print(f'\t\tinput{j}.txt') #<-p
			createFile(f'output{j}.txt', res[i+1])
			print(f'\t\toutput{j}.txt') #<-p
			j += 1


def getProblem(url, path):
	DOMAIN = "https://codeforces.com"
	cf = req.get(url).text

	pattern = re.compile(r'<td class="id">((\n|.)*?)</td>')
	matches = pattern.finditer(cf)

	title_pattern = r'<title>(.*?)</title>'
	title = re.search(title_pattern, cf)
	title = title.group(1).split('-')[1][1:-1]

	os.chdir(path)
	os.mkdir(title)
	print(f'{title}\\') #<-p
	path = os.path.join(path, title)
	os.chdir(path)

	cf = ""
	for match in matches:
		cf += match.group(1)

	pattern = re.compile(r'href="(.*?)"')
	matches = pattern.finditer(cf)

	for link in matches:
		genIOS(DOMAIN+link.group(1), path)
		os.chdir(path)


def main():
	path = r'' #<-- Default Path: if not set it will use main_path(where CF_Bot.py is located!)
	if path == '': path = main_path

	if len(sys.argv) == 3:
		url = sys.argv[1]
		path = sys.argv[2]

	elif len(sys.argv) == 2:
		url = sys.argv[1]

	else:
		info = input('Enter info(link, path): ').split(',')
		url = info[0]
		if len(info) > 1:
			i = 0
			while(info[1][i] == ' '): i += 1
			path = info[1][i:]

	print('\nCodeforces Bot by Shanto Noor !...')
	print('Starting process...\n')
	print(f'Link: {url}')
	print(f'Path: {path}\n')
	if 'problem' in url:
		genIOS(url, path)

	else:
		getProblem(url, path)

	print('\nProcess finished successfully!...')


if __name__ == '__main__':
	main()
