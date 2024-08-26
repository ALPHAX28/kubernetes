import time
import requests

server_list = ['http://load-balancer-service:80']  

while True:
    try:
        for server in server_list:
            response = requests.post(server, data="hi")
            print(response.text)
            time.sleep(1) 
    except Exception as e:
        print(f"Failed to connect to {server}: {e}")
