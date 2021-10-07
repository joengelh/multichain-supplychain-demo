# Review Exchange

Returns information about a proposed exchange like offer and price.

**URL** : `/api/v1/reviewExchange/`

**Method** : `GET`

**Auth required** : NO

**Permissions required** : None

**Data constraints**

Provide exchange address.

```json
{
    "proposal":"[string]"
}
```

**Data example** All fields must be sent.

```json
{
"proposal": "010000000182b243e1458ec656d5f89fce52f66858cb4b7d91e05caf4b586e6624a3b0c36c000000006a47304402201c7468b3e72692a69b12b449dc770fd7c16897c57fc6ac28e5d07e676628a206022037f8acd2b2cca90f7332cadaa3c0d118a115f7b7c3301c88969576f2793d1aaa8321034ebeec63cd0ab6131d62d203dc178bcd33dba8df75f7c1a38eea394e577a8dfdffffffff0100000000000000003776a914eaaaa8cd21793342a6bb9ca8c0023f44720938fb88ac1c73706b7116ad7694442a5b94176ba35f723c8e5b40420f00000000007500000000"
}
```

## Success Response

**Condition** : If everything is OK and the proposal exists.

**Code** : `200 OK`

**Content example**

```json
{
    "data": {
        "offer": {
            "amount": 0,
            "assets": [
                {
                    "name": "lenovoServer",
                    "assetref": "954-267-38169",
                    "qty": 2
                }
            ]
        },
        "ask": {
            "amount": 0,
            "assets": [
                {
                    "name": "USD",
                    "assetref": "884-266-36443",
                    "qty": 10000
                }
            ]
        },
        "requiredfee": 0,
        "candisable": true,
        "cancomplete": true,
        "complete": false
    }
}
```
