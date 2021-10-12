                     Part 1
                     
1 VPC created & configured & role described

       - In the navigation pane, under VPC Dashboard
       - Click on your VPCs 
       - On right side, click on create VPC 
       - Enter VPC Name 
       - Enter IPV4 CIDR block
       - Click create CIDR on bottom 
 role described: VPC  is a private cloud computing environment contained within a public cloud 
       
        
2 Subnet created & configured & role described

       - Under VPC Dashboard
       - Click on subnets
       - On right side click on create subnet
       - Choose VPC you wanna configurete with 
       - Enter the subnet name 
       - Specify a private IP address range
       - Click create
  role described: A subnet is a range of IP addresses in your VPC

        
3 Internet gateway created & configured & role described

       - In the navigation pane, under VPC Dashboard
       - Click on internet gateways 
       - click on create gateway 
       - Enter the gateway name
       - Click on create gateway
       - select VPC you want to attach 
       - Click yes create
       
  role described: gateway is a network node used in telecommunications that connects  
  two networks with different transmission protocols together, it serves as an entry 
  and exit point for a network
        
4 Route table created and configured & role described

       = Under  VPC Dashboard
       = Click route tables
       = Click on create route table
       = Enter the route table name
       = Select VPC you want to configure with
       = Click yes create
       = Next  add the route (destination and target) and save 
       = Then associate with a subnet by click on subnet association, edit select subnet and click on save  
   role described:Route table is a set of rules that are used to determine 
   where network traffic from your subnet or gateway is directed.

        
5 Security group created and configured & role described

      - In the navigation pane, under VPC Dashboard
      - Click on security groups
      - Click on create security group
      - Enter name for security groupe
      - Select VPC you want to configure with
      - Add rule 
      - Click on create
 role described: Security group control incoming and outgoing traffic is like firewall for c2 instance

                       Part 2
  
1 Instance details
  AMI selected
  default username of the instance type selected
    Instance type selected
    
  For AMI select instance
  
      Under action click on image and temple
      Enter the name and click create
      
2 How to attach instance to VPC

         - Open the Amazon EC2 console
         - In the navigation pane, choose Instances.
         - Select one or more running EC2-Classic instances.
         - Choose Actions, ClassicLink, Link to VPC.
         - Choose a VPC.
         - Select one or more security groups to associate with your instances 
            The console displays security groups only for VPCs enabled for ClassicLink.
         - Choose Link.
 
3 Public IP address auto-assign - yay or nay and why?

      - Yes for me because I don’t own the internet, I move a lot and I don’t need VPN. 
      
4 How to create and attach storage volume to instance

        - Open the Amazon EC2 
        - In the navigation pane, choose Elastic Block Store, Volumes.
        - Select an available volume and choose Actions, Attach Volume.
        - For Instance, start typing the name or ID of the instance. Select the instance from the list of options 
        - For Device, you can keep the suggested device name, or type a different supported device name. 
        - Choose Attach.
        - Connect to your instance and mount the volume. 
 
5 How to tag instance with "Name" of "YOURLASTNAME-instance"

          - Click on edit icon
          - Enter the name then click save
          
6 How to associate VPC security group (your security group) with your instance

          - In the navigation pane, choose Security Groups.
          - Select the security group.
          - Choose Actions, Edit inbound rules or Actions, Edit outbound rules.
          - For each rule, choose Add rule and fill the ports
          - Choose Save rules.
 
7 How to create / reserve and associate and Elastic IP address with your instance

          - In the navigation pane, choose Network & Security, Elastic IPs.
          - Choose Allocate Elastic IP address.
          - For the Public IPv4 address pool, choose key name and values name.
          - Choose Allocate

8 Screenshot with instance details

    ![Services](https://user-images.githubusercontent.com/77375881/137005882-4083ddde-a68d-4fcf-a336-a0cd9bd50a8b.jpeg)
    

9 How to change hostname via commands on instance

          - hostname NEW_HOSTNAME
          
10 Screenshot of successful SSH connection to instance (with your new hostname instead of ip-##-##-##-##)

  ![httpsaws amazon comamazon-linux-2](https://user-images.githubusercontent.com/77375881/137005422-2ff53972-b760-4475-919a-bc5942f00958.jpeg)

