# Fund

Funds users account with USD by issuing the asset
directly to the specified account.

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
    "amount": "[posititve float]"
}
```

**Data example** All fields must be sent.

```json
{
    "account":"1ExJS65CFCniLT7r8h1pXByr9L3q3YsgMhMA3D",
    "amount":1.2
}
```

## Success Response

**Condition** : If everything is OK and the account exists.

**Code** : `200 OK`

**Content example**

```json
{
    "data": 1.2
}
```
