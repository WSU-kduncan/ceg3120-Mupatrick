                        Part 1:
Part 1 - CloudFormation Template TODOs

1 Modify security Group

Proxy
![Instance i-0d6669992462f43ea (proxy)](https://user-images.githubusercontent.com/77375881/141342400-a810d05d-3338-4f83-97a9-be8a0909d9bd.jpeg)

WebServ1
![Instance i-0a452d8c154bfaed0 (webserv1)](https://user-images.githubusercontent.com/77375881/141342432-12af7d61-d47d-4b91-8d13-47544b42c024.jpeg)

WebServ2
![Instance i-05f8ffd21e105ce92 (webserv2)](https://user-images.githubusercontent.com/77375881/141342467-d8cd91ca-b57d-448f-9bfa-f5e1883cce4d.jpeg)

2 create 3 instance

![j-0d6669992462f43eal](https://user-images.githubusercontent.com/77375881/141342787-88b8a3d2-526b-46af-951b-67585590e6d5.jpeg)

3 and 4 
elastic ip address
unique private IP
haproxy is installed / apache
the hostname is changed


Proxy
![Pr![Instance ID](https://user-images.githubusercontent.com/77375881/141345431-371aef08-6984-4224-8a13-f8bddae0d765.jpeg)
ivate IPv4 addresses](https://user-images.githubusercontent.com/77375881/141343541-5bf184bc-9114-45d2-af1c-56985dd63921.jpeg)
![lubuntu@proxy $ whereis haproxy](https://user-images.githubusercontent.com/77375881/141344992-e8fb4567-c24e-4e30-b2f6-9cee3b225ede.jpeg)

WebServ1
![ID Instance](https://user-images.githubusercontent.com/77375881/141343499-b4c0e2b1-a580-4140-883a-c9ad8df74ea6.jpeg)
![wherels](https://user-images.githubusercontent.com/77375881/141345011-34df5927-f529-4ef2-9962-868a0f625226.jpeg)

WebServ2
![Instance summary Info](https://user-images.githubusercontent.com/77375881/141343474-36eb6cca-ff0b-4b1f-a646-faad3907b284.jpeg)

![ubuntu@WebServ2 ~$ whereis apache2](https://user-images.githubusercontent.com/77375881/141345032-1cbb5b93-0cd3-4808-9976-3d6d4d47f1dc.jpeg)


Part 2 - Setup Load Balancing TODOs

![cat etc nosts](https://user-images.githubusercontent.com/77375881/141354933-21b24ce7-7a0d-4d17-b7bf-5413bca3556a.jpeg)



2 Document how to SSH in between the systems utilizing their private IPs.

![homeubuntuceg3120-f21 pem ubuntue10](https://user-images.githubusercontent.com/77375881/141346110-899ff4d2-e7d6-4f6b-86a0-9e5f5f43d34f.jpeg)


3 HAProxy restart and status

![lubuntu@proxy ~$ sudo systemctl restart haproxy service](https://user-images.githubusercontent.com/77375881/141348121-6afb646b-03c3-4c3a-a644-38b686c793e1.jpeg)

4 Webserver 1 & 2 restart
![ubuntu@WebServ1varwwwhtml$ sudo vim index html](https://user-images.githubusercontent.com/77375881/141348411-ed2cd9fb-055d-41bb-a697-e807de81114d.jpeg)


5 From the browser, when connecting to the proxy server, take two screenshots

Using Proxy IP

![A Not Secure](https://user-images.githubusercontent.com/77375881/141349312-55d4549f-f3dd-4ad7-a1f7-f3a636d44e86.jpeg)

![A Not Secure 52 1 136 68](https://user-images.githubusercontent.com/77375881/141348935-518a2e47-ce5d-458a-a3db-3d920e734e15.jpeg)


Using WebServ1 Public IP
![A Not Secure 34 197 151 222](https://user-images.githubusercontent.com/77375881/141349029-138ef97a-b584-4159-92f0-2e4f6b84ecf3.jpeg)


Using WebServ2 Public IP
![A Not Secure 50 17 252 186](https://user-images.githubusercontent.com/77375881/141349047-1a230c7c-1e2b-4e37-aa51-767dabd366c9.jpeg)

