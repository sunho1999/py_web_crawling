import requests
from bs4 import BeautifulSoup as bs

MEMBER_DATA = {
    'memberID':'wmfrlek1108','memberPassword':'vudtjsgh@789'
}

#하나의 세션(Session)객체를 생성해 일시적으로 유지합니다.
with requests.Session() as s:
    #로그인 페이지로의 Post 요청(Request)객체를 생성합니다.
    request = s.post('http://dowellcomputer.com/member/memberLoginAction.jsp',data=MEMBER_DATA)

print(request.text)

request = s.get('http://dowellcomputer.com/member/memberUpdateForm.jsp?ID=wmfrlek1108')
soup = bs(request.text,'html.parser')

result = soup.findAll('input',{"name": "memberEmail"})
print(result[0].get('value'))