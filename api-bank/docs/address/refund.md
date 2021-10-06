# Refund

Refunds USD by sending specified amount of USD
from the banks wallet to the blockchains burn address.

**URL** : `/api/v1/refund/`

**Method** : `POST`

**Auth required** : NO

**Permissions required** : None

**Data constraints**

Provide amount to be burned from the banks wallet

```json
{
    "amount": "[posititve float]"
}
```

**Data example** All fields must be sent.

```json
{
    "amount":1.2
}
```

## Success Response

**Condition** : If everything is OK and the bank has the required amount of USD.

**Code** : `200 OK`

**Content example**

```json
{
    "data": 1.2
}
```
