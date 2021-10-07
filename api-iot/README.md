# IoT API Documentation

## Concept

In order to make the OEMs products origin retracable for customers an thereby fight product manipulation and counterfeit products, the OEM uses IoT Devices in this demo.
Upon shipment, the IoTs Sensors are activated using the API and for as long as the IoT Device exists data is being written to the blockchain for customers to retrace.
The IoT Device can only be deactivated by persons having access to the IoT Node and are being deactivated upon final delivery to the customer by the OEM in this demo.

## Functionality

This API Serves to the **frontend-oem** all the functionalities expected of a iot service.
* activate new device
* deactivate existing device
* list all active devices

For this demo, the IoT Devices and theire sensors are being simulated by the Python Random module.

## Directions

In a real world scenario this API would be served by the node labeled **iot**.
For simplicities sake in the demo all APIs are being served by one central host using port 5005.

## Open Endpoints

* [root](docs/root.md) : `GET /`
* [activate](docs/address/activate.md) : `GET /api/v1/activate`
* [deactivate](docs/address/deactivate.md) : `POST /api/v1/deactivate`
* [listAll](docs/address/listAll.md) : `GET /api/v1/listAll`
