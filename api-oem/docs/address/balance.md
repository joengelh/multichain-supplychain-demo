# Balance

Returns USD balance of specified multichain address.

**URL** : `/api/v1/balance`

**Method** : `GET`

**Auth required** : NO

**Permissions required** : None

**Data constraints**

Provide multichain address.

```json
{
    "account": "[multichain address]"
}
```

**Data example** All fields must be sent.

```json
{
    "account": "1ExJS65CFCniLT7r8h1pXByr9L3q3YsgMhMA3D"
}
```

## Success Response

**Condition** : If everything is OK and the account exists.

**Code** : `200 OK`

**Content example**

```json
{
    "data": {
        "name": "USD",
        "assetref": "40-265-39368",
        "qty": 100101
    }
}
```
