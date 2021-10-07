# Bank API Documentation

## Concept

A banking service on the blockchain is fundamentally diffrent from traditional banking services, since the bank does not require to have administrative access to the account/wallet of the customer. Hence, the relationship can be designed in a trustless manner.

## Functionality

This API Serves to the **frontend-bank** all the functionalities expected of a bank service.
Firstly, the customer can create an account using wallet address, name, email and password.
Thereafter he can convert USD to USD Token by funding USD to theire own wallet.
This transaction can be monitored and billed accordingly by the bank.
Aswell the customer can view the blockchains burn address and use it in his own interface to burn USD. This transaction can be monitored and billed accordingly aswell.

## Directions

In a real world scenario this API would be served by the node labeled **bank**.
For simplicities sake in the demo all APIs are being served by one central host using port 5001.

## Open Endpoints

* [root](docs/root.md) : `GET /`
* [ownAddress](docs/address/ownAddress.md) : `GET /api/v1/ownAddress`
* [balance](docs/address/balance.md) : `POST /api/v1/balance`
* [burnAddress](docs/address/burnAddress.md) : `GET /api/v1/burnAddress`
* [fund](docs/address/fund.md) : `POST /api/v1/fund`
* [refund](docs/address/refund.md) : `POST /api/v1/refund`
