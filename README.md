# multichain-supplychain-demo
This project aims to offer a drastically simple blockchain demo of a trustless supply chain, in which a customer buys an electronic device from an OEM after a service provider added value to it. Throughout the entire supply chain an IoT Device is monitoring environment parameters and a tail of the syslogs.

## Installation
The underlying blockchain can be installed, configured and all participants permissioned using the following Ansible project on [Github](https://github.com/joengelh/multichain-ansible-automation)

Thereafter copy the .env.sample file to .env and fill in your nodes addresses and private keys.

:warning: **Dont share private keys in production**: seperate the .env files to each node according to ownership instead :warning:

In order to install the required python packages simply run:

```bash
pip3 install -r <endpoint directory>/requirements.txt
```

## Participants
A multitude of web-based apps give every one of the following stakeholders direct access to the blockchain.
Since this project is still in the making, a ```-``` stands for an endpoint still to be developed.

name | description | port webinterface | port api | status
-----|-------------|-------------------|----------|-------
serviceProvider | participant adding value to product | - | - | :heart:
customer | product purchasing party | - | - | :heart:
iot | device attached to product, monitoring | no frontend required | 5005 | :green_heart:
oem | initial producer of product | - | 5003 | :yellow_heart:
bank | issuer of stablecoin USD | 5002 | 5001 | :green_heart:

## Use Case

In this usecase, an OEM is selling goods (electronic devices) to a customer, using a stablecoin USD.
The stablecoin is issued by a bank and can be refunded by sending the tokens to the networks burn address.

In order to represent the goods on the supplychain, the OEM mints products by issuing a new asset class and selling the asset to the service provider in exchange for USD.

Afterwards the service provider re-sells the product to the customer for the original price plus a markup using multichains atomic exchanges.
Fron the minting of the asset until the customers reception of the product, the IoT member writes data contiuously to the blockchain regarding location, temperature, humidity, shock (G-force) and the tail of the syslogs.

A multichain smart filter ensures the customer will only buy the product if its has been monitored continously by the IoT device and the data does not present damaging circumstances for the product or malware deployment in the syslogs.

## Transactions

1. bank swaps money if requested in gui after login :thumbsup:
2. customer communicates serviceProvider the business needs :thumbsup:
3. serviceProvider communicates oem the besiness needs :thumbsup:
4. oem issues asset & stream :thumbsup:
5. iot writes to stream :thumbsup:
6. oem offers atomic transaction server against EUR :thumbsup:
7. service provider reviews data, accepts
8. service provider writes to steam
9. iot writes to stream
10. service provider offers atomic transaction, server against EUR
11. customer reviews data, accepts

## Run it!
After the multichain has been deployed using for example this [Github Project](https://github.com/joengelh/multichain-ansible-automation) and the .env file has been filled with the nodes addresses and private keys, the webservers can be started.
For that, from the projects root directory, simple call them using:

```bash
python3 api-bank/main.py
```

in case of an API endpoint or:

```bash
python3 frontend-bank/main.py
```

in case of a web ui.

## Powerpoint

![Title](images/slide1.PNG)

### Starting Point

![Starting Point](images/slide2.PNG)

### Black Box

![Black Box](images/slide3.PNG)

### The Problem

![The Problem](images/slide4.PNG)

### The Solution

![The Solution](images/slide5.PNG)

![Needs Met](images/slide6.PNG)

