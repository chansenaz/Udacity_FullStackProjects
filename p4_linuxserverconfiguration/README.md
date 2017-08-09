# Linux Server Configuration
Christopher Hansen - [github](https://github.com/chansenaz)

### About
This is my fourth project for Udacity's [Full Stack Web Developer Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004)

### Assignment
You will take a baseline installation of a Linux distribution on a virtual machine and prepare it to host your web applications, to include installing updates, securing it from a number of attack vectors and installing/configuring web and database servers.

## Server Details
Public IP Address: 34.213.58.157 (since removed)

SSH Port: 2200

Application URL: http://34.213.58.157 (since removed)


---
## Configurations Made

### User Management
1. Created new user 'grader'
2. Gave grader permission to sudo
3. Gave grader secure key pair
4. Disabled remote login for root user

### Security
1. Configured ufw to only allow application ports
2. Enforced Key-based ssh authentication
3. Hosted ssh on non-default port 2200

### Application Functionality
1. Updated all installed packages
2. Configured the local timezone to UTC
3. Installed and configured Apache to serve a Python mod_wsgi application
4. Installed and configured PostgreSQL

---
## Software Installed
* apache2
* libapache2-mod-wsgi
* postgresql
* python-dev

---
## Third Party Sites Used
https://www.digitalocean.com/community/tutorials/how-to-deploy-a-flask-application-on-an-ubuntu-vps
https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-16-04