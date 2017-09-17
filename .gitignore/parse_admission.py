
import urllib2
from bs4 import BeautifulSoup
import re
quote_page = 'https://www.ugrad.vcu.edu/why/faqs/admissions.html'
page = urllib2.urlopen(quote_page)

soup = BeautifulSoup(page,'html.parser')

questions = soup.find_all('h4')

first_link = soup.h4

tags = []

for tag in soup.find_all(True):
    tags.append(tag.name)

# print tags

tags_post_h4 = []


for num,i in enumerate(tags):
	if i == 'h4':
		tags_post_h4.append(tags[num+1])
		
# print tags_post_h4

def check_questions(questions):
	if 'table' in tags_post_h4:

		ind = tags_post_h4.index('table')
		# print ind
		questions.pop(ind)
		return questions
		
	else:
		pass

# questions = check_questions(questions)

if 'table' in tags_post_h4:

	questions = check_questions(questions)



# for i in questions:
	# print i.text.strip()

# print len(questions)



answers = first_link.find_all_next('p')

string_ans = []

for i in answers:
	string_ans.append(str(i))

grab_ans = []

def cleanhtml(raw_html):
 cleanr = re.compile('<a.*?>')
 cleantext = re.sub(cleanr, '', raw_html)
 cleantext = re.sub('</a>', '', cleantext)
 return cleantext

for i in string_ans:	
	if i.startswith('<p>') :
		ans = re.search('<p>(.*)<',i).group(1)
		ans = cleanhtml(ans)
		grab_ans.append(ans)
		# print ('\n'+ans)
		

ques_ans_dic = {}

for num,i in enumerate(questions):
	# i=i.text.strip
	# print type(i)
	i=str(i)
	j = i.replace('?','')
	j = re.search(r'(?<=\>)(?!\<)(.*)(?=\<)(?<!\>)',j).group(1)

	# print (i.split())
	# i = i.split()
	# print i 
# 	i = i.remove('?')
# 	i = ' '.join(i)
	ques_ans_dic[str(j)]= grab_ans[num]

print ques_ans_dic

# for i in ques_ans_dic:
# 	print i 
# 	print ques_ans_dic[i]

# for num,i in enumerate(questions):
# 	i=i.text.strip
# 	i=str(i)
# 	i = list(i).remove('?')
# 	i = ' '.join(i)
# 	ques_ans_dic[str(i)]= grab_ans[num]

# print ques_ans_dic
		


# def process(i):
# 	ans = re.search('<p>(.*)<',i).group(1)
# 	ans = cleanhtml(ans)
# 	return ans

# cat_full_string = []
# anss = []

# stringo = ''

# for num,i in enumerate(string_ans):	
# 	# if i.startswith('h4'):
# 	# print i 

# 	if i.startswith('<p>') and string_ans[num+1].startswith('<p>'): 
# 		# print process(i)



# 		stringo = stringo + process(i)+process(string_ans[num+1])

# 		# grab_ans.append(ans)
# 		# print ('\n'+ans)
# 		cat_full_string.append(stringo)
		

# 	elif i.startswith('<p>') and  string_ans[num+1].startswith('<p ')and string_ans[num-1].startswith('<p>'):
# 		pass

# 	elif i.startswith('<p>') :
# 		anss.append(process(i))
	 	

	# elif i.startswith('<h4>') and string_ans[num+1].startswith('<p>'):
	# 	anss.append(i)
	# 	print i

# t_ans=[cat_full_string[-1]]+anss

# print len(anss)

# print cat_full_string[-1]
# print (anss)

# for i in t_ans:
# 	print i

# print len(grab_ans)
	
	





