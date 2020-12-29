import sys
from commands import *

# Rules:
print('Please start writing the content:')
print('1. # for h1 tag')
print('2. ## for h2 tag')
print('3. ### for h3 tag')
print('4. <enter> to insert line break')
print('5. => visible_text link ')
print('6. simple text for paragraph')
print('7. ``` to print text without changes')
print('8. > to print blockquote')
print('9. * for list elements')
print('10. // for comments')
print('11. _ for ruler')

filename = sys.argv[1].strip()
convname = filename.split('.')[0]+'.html'
title = input('\nEnter title of Webpage: ')
start_html = '''<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>'''+title+'''</title>
	<link href="https://fonts.googleapis.com/css2?family=Fira+Code&family=Gelasio&family=Roboto&display=swap" rel="stylesheet">
	<link rel="stylesheet" href="./assets/style.css">
</head>
<body>
	<nav id="navbar">
		<a class="button" href="./index.html">Home</a>
		<a class="button" href="./blog.html">Blog</a>
		<a class="button" href="./doc.html">Doc</a>
		<a class="button" href="./about.html">About</a>
	</nav>
	<div id="data">'''
mid_html=''
end_html = '''
	</div>
	<footer>
		<p id="bottomtext">
		&#169; 2020 Arsh Jethi
		</p>
	</footer>
</body>
</html>
'''
try:
	file = open(filename,'r')
	data = file.readlines()
	file.close()
	length=len(data)
	i=0
	temp=''
	while i<length:
		text=data[i].lstrip(' ').split(' ',1)
		if text[0]=='>':
			temp+='\n\t\t<blockquote>\n'
			if (i<length and (text:=data[i].lstrip(' ').split(' ',1))[0]=='>'):
				temp+='\t\t\t'+text[1].strip()
				i+=1
			while(i<length and (text:=data[i].lstrip(' ').split(' ',1))[0]=='>'):
				temp=temp+' <br/>\n\t\t\t'+text[1].strip()
				i+=1
			temp+='\n\t\t</blockquote>'
			mid_html += temp
			temp=''
			continue
		elif text[0]=='```\n':
			temp+='\n<pre>\n'
			i+=1
			while(i<length and (data[i].lstrip(' ').split(' ',1))[0]!='```\n'):
				temp+=data[i]
				i+=1
			temp+='</pre>'
			mid_html += temp
			temp=''
			i+=1
			continue
		elif text[0]=='*':
			temp+='\n\t\t<ul>\n'
			while(i<length and (text:=data[i].lstrip(' ').split(' ',1))[0]=='*'):
				temp+='\t\t\t<li>'+text[1].strip()+'</li>\n'
				i+=1
			temp+='\t\t</ul>'
			mid_html += temp
			temp=''
			continue
		elif commands.get(text[0],0):
			mid_html += commands[text[0]](text[1]) if len(text)>1 else commands[text[0]]
		else:
			temp+='\n\t\t<p>\n'
			if i<length and ((strip_data:=data[i].strip())=='' or strip_data.split(' ',1)[0] not in ">```_*###=>//"):
				temp+='\t\t\t'+strip_data
				i+=1
			while i<length and ((strip_data:=data[i].strip())=='' or strip_data.split(' ',1)[0] not in ">```_*###=>//"):
				temp=temp+' <br/>\n\t\t\t'+strip_data
				i+=1
			temp += '\n\t\t</p>'
			mid_html+=temp
			temp = ''
			continue
		i+=1
	
	final_html = start_html + mid_html + end_html
	file = open(convname,'w')
	file.write(final_html)
	file.close()

except Exception as e:
    print("Some error occured :",e)