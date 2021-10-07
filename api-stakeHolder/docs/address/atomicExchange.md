# Atomic Exchange

Proposes to exchange a specified asset of a specified quantity for a specified price of a specified barter,
returns address of the exchange.

:warning: **Only two classes of assets at once**: in this demo, only one asset can be exchanged for another at once :warning:

**URL** : `/api/v1/atomicExchange/`

**Method** : `POST`

**Auth required** : NO

**Permissions required** : None

**Data constraints**

Provide address, amount and asset.

```json
{
    "name": "[string]",
    "amount": [integer],
    "barter":[string],
    "price": [positive float]
}
```

**Data example** All fields must be sent.

```json
{
    "name":"dellServer",
    "amount":2,
    "barter":"USD",
    "price": 400000
}
```

## Success Response

**Condition** : If everything is OK enough of the asset is owned and the amount is divisible by one.

**Code** : `200 OK`

**Content example**

```json
{
"data": "010000000121f30439afdb35e262f881d1889848211d18197715815cbed8167129d7eaf508000000006b483045022100dfd8062b8db11eba8cc09e7da9aac70b05ac71cbc7130fe8db947e5636eb6aa50220328c4669824c724d341f153d2cc64f972fb988db06e7ebe434bf7adc7f7ffe6a8321034ebeec63cd0ab6131d62d203dc178bcd33dba8df75f7c1a38eea394e577a8dfdffffffff0100000000000000003776a914eaaaa8cd21793342a6bb9ca8c0023f44720938fb88ac1c73706b7116ad7694442a5b94176ba35f723c8e5b005a6202000000007500000000"
}
```
