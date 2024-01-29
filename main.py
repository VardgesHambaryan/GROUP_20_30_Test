import requests
from bs4 import BeautifulSoup
import json


headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0",
}

# url = "https://smartcode.am/hy/"
# response = requests.get(url=url , headers = headers)

# with open('index.html' , 'w') as file:
#     file.write(response.text)



def get_courses():

    UNKNOWN_DICT = {
        'name': None,
        'duration': None,
        'price': None,
    }

    with open('index.html' , 'r') as file:
        response = file.read()

    courses = []
    soup = BeautifulSoup(response , 'lxml')

    course_list = soup.find_all(class_ = 'course-item')
    for i in range(len(course_list)):
        duration , price = course_list[i].find_all('span')[0].text , course_list[i].find_all('span')[1].text

        UNKNOWN_DICT = {
        'name': course_list[i].find('h2').text,
        'duration': duration,
        'price': price,
        }

        courses.append(UNKNOWN_DICT)

    with open('courses.json' , 'w', encoding='UTF-8') as file:
        json.dump(courses , file , indent=4 , ensure_ascii=False)
        

if __name__ == '__main__':
    get_courses()



























