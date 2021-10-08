# Issue

Issues a specified amount of an asset specifically named.
The asset is only divisible by one since it is supposed to represent 
real units the OEM produces.

**URL** : `/api/v1/issue/`

**Method** : `POST`

**Auth required** : NO

**Permissions required** : None

**Data constraints**

Provide amount to be burned from the banks wallet

```json
{
    "name": "[string]",
    "amount": [posititve float]
}
```

**Data example** All fields must be sent.

```json
{
    "name":"dellServer",
    "amount":2
}
```

## Success Response

**Condition** : If everything is OK and the asset name is not reserved by another member on the blockchain.

**Code** : `200 OK`

**Content example**

```json
{
    "data": 1
}
```
