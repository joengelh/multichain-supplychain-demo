# Bank API Documentation

## Directions

In a real world scenario this API would be served by the node labeled **bank**.
For simplicities sake in the demo all APIs are being served by one central host using port 5001.

## Open Endpoints

* [root](docs/root.md) : `GET /`
* [ownAddress](docs/address/ownAddress.md) : `GET /api/v1/ownAddress`
* [burnAddress](docs/address/burnAddress.md) : `GET /api/v1/burnAddress`
* [balance](docs/address/balance.md) : `POST /api/v1/balance`
* [fund](docs/address/fund.md) : `POST /api/v1/fund`
* [refund](docs/address/refund.md) : `POST /api/v1/refund`
