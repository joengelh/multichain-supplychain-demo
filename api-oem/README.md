# OEM API Documentation

## Concept

A manufacturer of goods faces the challenge of quality and safety assurance. In a traditional business model, the manufacturer looses control over the product once it is shipped to a reseller. In a blockchain based business model, the manufacturer can give the device a unique ID and have IoT Sensors write data about the product to the blockchain for customers to retrace the products history. Counterfeit and manipulated products can thus be identified more easily.

## Functionality

This API Serves to the **frontend-OEM** the following functionalities:
* retrieving the own address
* querying the blockchain for the current issued inventory
* issue new assets
* sending assets to the business partners
* proposing a business deal as an atomic exchange

## Directions

In a real world scenario this API would be served by the node labeled **OEM**.
For simplicities sake in the demo all APIs are being served by one central host using port 5003.

## Open Endpoints

* [root](docs/root.md) : `GET /`
* [ownAddress](docs/address/ownAddress.md) : `GET /api/v1/ownAddress`
* [balance](docs/address/balance.md) : `GET /api/v1/balance`
* [inventory](docs/address/inventory.md) : `GET /api/v1/inventory`
* [issueMore](docs/address/issueMore.md) : `POST /api/v1/issueMore`
* [send](docs/address/send.md) : `POST /api/v1/send`
* [atomicExchange](docs/address/atomicExchange.md) : `POST /api/v1/atomicExchange`
