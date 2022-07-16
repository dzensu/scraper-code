from bs4 import BeautifulSoup


with open("../blank/index.html") as file:
    src = file.read()

suop = BeautifulSoup(src, 'lxml')

#title = suop.title
#print(title.text, title)

#div, div1 = suop.find_all('div'), suop.find('h1')

#info = suop.find('div', class_ ='user__birth__date')
#infro2 = suop.find('div', class_='user__birth__date').find_all('span')

#full_info = suop.find(class_='user__data').find_all('span')

#soc = suop.find(class_='social__networks').find_all('a')
#for i in soc:
#    soc_ = i.get('href')
 #   print(soc_)

#parent = suop.find(class_='post__text').find_parents()

