import requests
from bs4 import BeautifulSoup
from termcolor import colored

proxies = {
  "http": "http://172.16.76.99:8123",
  "https": "http://172.16.76.99:8123"
}
# Danh sách các thư viện cần kiểm tra

def get_vuln(library, version):
    
    # Tạo URL để truy vấn
    url = f'https://www.nuget.org/packages/{library}/{version}'
    
    # Thực hiện yêu cầu GET
    response = requests.get(url,proxies=proxies)
    
    # Phân tích cú pháp HTML
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Tìm phần tử chứa thông tin lỗi
    error_element = soup.find('div', class_='validation-summary-errors')
    
    if error_element is not None:
        # Hiển thị thông tin lỗi
        print(f'{library} {version} - {error_element.text.strip()}')
    else:
        print(f'{library} {version} - No errors found')

f = open('lib.txt', 'r')
for line in f:
    line = line.strip()
    line = line.encode('utf-8').decode('utf-8')
    data = line.split(':')
    if len(data) == 2:
        name = data[0].encode('utf-8').decode('utf-8')
        ver = data[1].encode('utf-8').decode('utf-8')
        if name != "" and ver != "":
            get_vuln(name, ver)
    else:
        continue