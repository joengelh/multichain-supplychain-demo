# Send

Sends a specified amount of a specified asset to a specified address.

**URL** : `/api/v1/send/`

**Method** : `POST`

**Auth required** : NO

**Permissions required** : None

**Data constraints**

Provide address, amount and asset.

```json
{
    "name": "[string]"
    "amount": [posititve float]
    "address": "[blockchain address]"
}
```

**Data example** All fields must be sent.

```json
{
    "name":"dellServer",
    "amount":2
    "address":"1ExJS65CFCniLT7r8h1pXByr9L3q3YsgMhMA3D"
}
```

## Success Response

**Condition** : If everything is OK enough of the asset is owned the amount is divisible by one and the address exists.

**Code** : `200 OK`

**Content example**

```json
{
    "data": 1
}
```
