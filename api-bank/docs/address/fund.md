# Fund

Funds users account with USD

**URL** : `/api/v1/fund/`

**Method** : `POST`

**Auth required** : NO

**Permissions required** : None

**Data constraints**

Provide multichain address and 
amount to be funded.

```json
{
    "account": "[multichain address]",
    "amount": "[integer
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
        "name": "EUR",
        "assetref": "40-265-39368",
        "qty": 100101
    }
}
```
