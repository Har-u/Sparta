import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(data.text, 'html.parser')
movies = soup.select("#old_content > table > tbody > tr")
i = 0
for movie in movies :
    
    # 위와 같이 랭킹을 정리하면 page가 바뀌면 순위가 반복됨,
    # 그러므로 이미지 td의 alt값(이미지가 엑박일때 대체 text인경우가 많음)를 땡겨올것
    #movie 안에는 몇십개의 tr들이 있음
    #그 중 td class가 title인 부분을 구분하여 div 안의 a를 찾아서 text만 출력해야함
    a_tag = movie.select_one('td.title > div > a')
    star = movie.select_one('td.point')
    # rank =movie.select_one('td:nth-child(1) > img')['alt']
    if a_tag != None : 
        print(str(i)+" " + a_tag.text +" " + star.text)
    i = i+1

#old_content > table > tbody > tr:nth-child(2)

#############################
# (입맛에 맞게 코딩)
#############################