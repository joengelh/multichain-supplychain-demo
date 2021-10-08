# Stakeholder API Documentation

## Concept

This API is being used by all standard participants on the network.

### Manufacturer

A manufacturer of goods faces the challenge of quality and safety assurance. In a traditional business model, the manufacturer looses control over the product once it is shipped to a reseller. In a blockchain based business model, the manufacturer can give the device a unique ID and have IoT Sensors write data about the product to the blockchain for customers to retrace the products history. Counterfeit and manipulated products can thus be identified more easily.

### Customer

A Customer of goods faces the challenge of quality and safety assurance. In a traditional business model, a customer has to trust the manufacturer, aswell as service providers to treat goods according to law and quality standards. With the advent of blockchain technology though, customers can retrace the history of products and thus gain insight into quality and origin.

### Service Provider

Service Providers face the challenge of trust. Not only does it take a long time to build it, aswell good safety standards and a quality assuring supplychain are hard to prove. With blockchain technology though, service providers can prove theire processes and the adequate treatment of the products they are trying to resell.

## Functionality

This API Serves to the **frontend-oem**, **frontend-customer**, **frontend-serviceProvider** the following functionalities:
* retrieving the own address
* querying the blockchain for the current inventory aswell as USD balance
* issue new assets (when permissioned)
* sending assets to the business partners
* proposing a business deal as an atomic exchange
* reviewing proposed business deals
* accepting business deals as atomic exchanges
* withdrawing a business deal proposal
* list all business proposals

## Directions

In a real world scenario this API would be served by the node labeled **oem**, **customer** or **serviceProvider**.
For simplicities sake in the demo all APIs are being served by one central host using port 5003 for the OEM, 5007 for the customer, 5009 for the serviceProvider.

## Open Endpoints

* [root](docs/root.md) : `GET /`
* [ownAddress](docs/address/ownAddress.md) : `GET /api/v1/ownAddress`
* [balance](docs/address/balance.md) : `GET /api/v1/balance`
* [inventory](docs/address/inventory.md) : `GET /api/v1/inventory`
* [issueMore](docs/address/issueMore.md) : `POST /api/v1/issueMore`
* [send](docs/address/send.md) : `POST /api/v1/send`
* [atomicExchange](docs/address/atomicExchange.md) : `POST /api/v1/atomicExchange`
* [reviewExchange](docs/address/reviewExchange.md) : `POST /api/v1/reviewExchange`
* [acceptExchange](docs/address/acceptExchange.md) : `POST /api/v1/acceptExchange`
* [withdrawExchange](docs/address/withdrawExchange.md) : `POST /api/v1/withdrawExchange`
* [listTransactions](docs/address/listTransactions.md) : `GET /api/v1/listTransactions
