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

