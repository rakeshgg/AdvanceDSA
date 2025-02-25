### Today's Discussion Points - lec1

#### EC2 = Server

- Server: Essentially a supercomputer with extensive hardware configurations.

#### AWS

- Server as an EC2 Instance:
  - Software Configuration (AMI): Amazon Machine Image (e.g., Ubuntu, RHEL)
  - Hardware Configuration: Instance type specifies CPU, memory, and I/O performance.

#### Factors to Consider When Choosing Instance Types:

1. Workload Requirements: CPU, memory, I/O needs.
2. Cost Efficiency: Budget-friendly options.
3. Elasticity: Auto-scaling capabilities.
4. Architecture: x86 or ARM-based processors.

#### Use Cases for Instance Types:

- T-Series: Development environments.
- C-Series: Compute-intensive workloads.
- R-Series: Databases.
- G-Series: Graphics and machine learning.

#### File Formats:

- .PEM (Privacy Enhanced Mail): Used for secure file transfer.
- .PPK: Format compatible with PuTTY.

---

Steps:

1. Run sudo yum update -y.
2. Install Apache: sudo yum install httpd.
3. Verify installation: httpd -v.
4. Check the service status: sudo service httpd status.
5. Start the service: sudo service httpd start.
6. Confirm status again: sudo service httpd status.
7. Navigate to the web root directory: cd /var/www/html.
8. List files: ls.
9. Create an HTML file: sudo nano index.html.
10. Save and verify the file.

---

### Task 04.12: Hosting a Static Webpage on a Windows EC2 Instance

### LEC2

- EBS Volumes
- AMI
- SS (Snapshot)

—--------------------------------------------
_Today's Discussion Points:_

1. _Root Volume:_

   - The default storage volume associated with an instance.

2. _EBS Volume (Elastic Block Store):_

   - A durable storage service for any type of data an application requires.

3. _EBS Scenarios Hands-On:_

   - Created a volume in one Availability Zone (AZ) and demonstrated its usage in another AZ.
   - Explored cross-location functionality.

4. _Snapshots:_
   - A point-in-time backup of an EBS volume.

_Usage of Snapshots:_

- Backup
- Disaster Recovery (DR)
- Data Cloning
- Migration

### LEC3

_Next Class:_

- _AMIs (Amazon Machine Images)_

_Task:_

- Practice creating and managing EBS volumes.
- Complete the assigned task for _04.12_.

=================================

1. _User Data_:

   - Automates tasks such as software installation, configuration, and updates.

2. _Cloning of EBS Volume_:

   - Cloning EBS volumes to another Availability Zone (AZ) or across regions.

3. _Example Bash Script for Automating Web Server Setup_:
   bash
   #!/bin/bash

   # Update the system

   apt update -y

   # Install Apache

   apt install -y apache2

   # Start Apache

   systemctl start apache2
   systemctl enable apache2

   # Create a sample webpage

   echo "<html><h1>Welcome to Apache on Ubuntu</h1></html>" > /var/www/html/index.html

   # Restart Apache to load new content

   systemctl restart apache2

4. _Usage of AMI (Amazon Machine Image)_:
   - Used to create identical EC2 instances with pre-configured software, settings, and configurations.
   - Webserver setup example: Apache + MySQL.
   - AMI creation and replication for scaling and fault tolerance.
   - _Disaster Recovery (DR) and Backup_:
     - By using AMIs, EC2 instances can be quickly launched in case of failure, preserving the previous configurations.
     - Quick deployment to different regions.
     - Automation with Auto Scaling.

---

### Usage of Snapshots (SS):

- _Common Use Cases for Snapshots_:
  - Backup of EBS volumes.
  - Disaster Recovery.
  - Data migration.
  - Volume replication.
  - Application migration.
  - Creating new AMIs.

---

### Task Instructions:

1. _Launch a Webserver with Multiple Configurations_:
   - Configure the webserver with various settings.
   - Take an AMI of the webserver.
   - Launch a replica of the original webserver from the AMI.
   - Deploy the replica in a different location.

### Introduction to Elastic Load Balancing (ELB)

_Discussion Points for Today:_

- AWS EC2
- Load Balancer - ELB

_Listener Rules:_

- HTTP, HTTPS
- Rules define how incoming traffic is routed to specific target groups based on conditions.

_Types of Load Balancers:_

- Classic LB
- Application LB (ALB)
- Network LB (NLB)
- Gateway LB (GLB)

_Key Features:_

- Equal distribution of incoming traffic to registered instances
- Health monitoring
- Simplifies SSL/TLS certificate management with ACM integration (SSL/TLS offloading)
- Flexible routing: host-based, path-based, header-based routing
- Traffic management
- Logging & monitoring with AWS X-Ray (to trace requests through the application)
- Cost efficiency: Pay-as-you-go pricing model based on hours, data amount, and number of LCUs.

### Auto Scaling Groups (ASG)

#### Features of Auto Scaling Group (ASG):

- _Automatic Scaling_
- _High Availability_
- _Cost Optimization_
- _ELB Integration_

#### Components of ASG:

- _Launch Template_
- _Scaling Policy_
- _Capacity_

#### ASG Lab:

- _Task_: Complete the hands-on exercise for ASG and ALB.
