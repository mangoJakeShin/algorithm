import requests
import time

url = "https://leisure-web-api.yanolja.com/product/v1/products/10201016/option-groups/10257731/schedules?startDate=2025-04-04&endDate=2025-05-11"  # 요청을 보낼 주소
cookies = {
     "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
    , "Access-Token":"442A472D4B6150645367566B59703373367639792442264528482B4D62516554"
}

while True:
    try:
        response = requests.get(url)
        print("상태 코드:", response.status_code)
        print("응답 헤더:", response.headers)
        print("응답 본문:", response.text)
    except Exception as e:
        print("오류 발생:", str(e))

    time.sleep(10)  # 10초 대기
