# multichain-supplychain-demo
This project aims to offer a drastically simple blockchain demo of a trustless supply chain.

The underlying blockchain can be installed, configured and all participants permissioned using the following Ansible project on [Github Repository](https://github.com/joengelh/multichain-ansible-automation)

A multitude of web-based apps give every one of the following stakeholders:

name | description | port webinterface | port api
-----|-------------|-------------------|---------
serviceProvider | multichain administrator | 


## use case

![Title](images/slide1.PNG)

### Starting Point

![Starting Point](images/slide2.PNG)

### Black Box

![Black Box](images/slide3.PNG)

### The Problem

![The Problem](images/slide4.PNG)

### The Solution

![The Solution](images/slide5.PNG)

### transactions
1. bank swaps money if requested in gui after login :thumbsup:
2. customer communicates serviceProvider the business needs :thumbsup:
3. serviceProvider communicates oem the besiness needs :thumbsup:
4. oem issues asset & stream
5. iot writes to stream
6. oem offers atomic transaction server against EUR
7. service provider reviews data, accepts
8. service provider writes to steam
9. iot writes to stream
10. service provider offers atomic transaction, server against EUR
11. customer reviews data, accepts

![Needs Met](images/slide6.PNG)

