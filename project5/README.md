			Part 1 - CloudFormation Template TODOs
			
The CloudFormation template provided in this project folder is updated to get you started on this project.
All said and done, your template should do the following:

1 Modify the Security Group to have the following additional rules:

			Access HTTP from any IP address
			IpProtocol: tcp
				  FromPort: "80"
				  ToPort: "80"
				  CidrIp: 0.0.0.0/0

			Access HTTP from within the VPC
			IpProtocol: tcp
				  FromPort: "80"
				  ToPort: "80"
				  CidrIp: 10.0.0.0/24
				  
2 Create 3 instances: 

	- Succeed (check image file)
[image file](https://github.com/WSU-kduncan/ceg3120-Mupatrick/blob/main/project5/image.md)
	
3 One instance configured such that:

	- it gets an elastic ip address - Succeed (check image file)
	- it gets a unique private IP - Succeed (check image file)
	- haproxy is installed - Succeed (check image file)
	- the hostname is changed and unique to the system - Succeed
	
4 Two additional instances configured such that:
	- Update 11/4 each instance gets a unique elastic IP address - Succeed
	- each gets a unique private IP - Succeed
	- webserver of choice is installed - Succeed
	- the hostname changed and unique for each system - Succeed
	
5 The deliverable for this part is the CloudFormation template included in your repo folder. 
	- for template check "patrick_template.yml" file [template file](https://github.com/WSU-kduncan/ceg3120-Mupatrick/blob/main/project5/patrick_template.yml)

		Part 2 - Setup Load Balancing TODOs
		
Setup the following and add documentation or screenshots to your README.md file as specified.

1 Create an /etc/hosts file on each system that correlates hostnames to private IPs.
  Description of how file is configured:

	Steps I take after ssh for each system 
		- sudo vim etc/hosts
		- Press i for insert
		- Then add a few line by typing : "private-Ip fileName name"
		- For example : 10.0.0.12 webserv1.domain.com webserv1
 
2 Document how to SSH in between the systems utilizing their private IPs.

	Have a private key and remember to change permission
	For me I have my private key in each system then I used a below command
	ssh -i /home/ubuntu/ceg3120-f21.pem ubuntu@private Ip
	“Check image file for prove” [image file](https://github.com/WSU-kduncan/ceg3120-Mupatrick/blob/main/project5/image.md)
 
3 HAProxy configuration & documentation requirements

	How to install package
	Yes, your template should preinstall the package. Write it again for your documentation
	
		Steps:
			In template command is 
				#!/bin/bash -xe
				apt-get update && \
				apt-get install -y git python3 python3-pip  haproxy && \
				hostnamectl set-hostname  WebserName && \
				reboot
				
			In terminal command is:
				Sudo apt-get update
				Sudo apt-get install -y git python3 python3-pip  haproxy
				Sudo hostname  WebserName or sudo hostnamectl set-hostname wbserName
				
	What file(s) where modified & their location
	
		- File modified is haproxy.cfg
		- Location is /etc/haproxy
		
	What configuration(s) were set (if any)
		global
			# global setting
		    maxconn 50000
		    log /dev/log local0
		    user haproxy
		    group haproxy
		    stats socket /run/haproxy/admin.sock user haproxy group haproxy mode 660 level admin
		    
		defaults
			# defaults here
		    timeout connect 10s
		    timeout client 30s
		    timeout server 30s
		    log global
		    mode http
		    option httplog
		    maxconn 3000
		    
		frontend front
			# a front that accepts request from clients
		    bind 52.1.136.68:80
		    bind 10.0.0.10:80
			# bind *:80
		    default_backend patrick_serv
		    
		backend patrick_serv
			# accept request
		    balance roundrobin
			#Display
		    server WebServ1 10.0.1.12:80
		    server WebServ2 10.0.1.11:80

	How to restart the service after a configuration change
		- Command is sudo systemctl restart haproxy.service
		
	Resources used (websites)
		- https://www.haproxy.com/blog/the-four-essential-sections-of-an-haproxy-configuration/

4 Webserver 1 & 2 configuration & documentation requirements

	How to install package
	Yes, your template should preinstall the package. Write it again for your documentation
	
		In template command is 
			- apt-get update && \
			- apt-get install -y git python3 python3-pip  apache2 && \
			- hostnamectl set-hostname  WebserName && \
			- reboot
			
		In terminal command is:
			- Sudo apt-get update
			- Sudo apt-get install -y git python3 python3-pip  apache2
			- Sudo hostname  WebserName or sudo hostnamectl set-hostname wbserName
			
	What file(s) where modified & their location
		- File is index.html
		- Location is /var/www/html
		
	What configuration(s) were set (if any)
	- none
	
	How to restart the service after a configuration change
		- sudo service apache2 reload
		
	Resources used (websites)
	- https://www.digitalocean.com/community/tutorials/how-to-install-the-apache-web-server-on-ubuntu-20-04

5 From the browser, when connecting to the proxy server, take two screenshots.
	one screenshot that shows content from "server 1"  Succeed (check image file)
	one screenshot that shows content from "server 2" Succeed (check image file)
	
6 (Optional) - link to your proxy so I can click it. 
 	- [proxy](http://52.1.136.68/)
