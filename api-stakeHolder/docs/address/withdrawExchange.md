# Withdraw Atomic Exchange

Withdraws a proposed exchange to the proposed conditions.

**URL** : `/api/v1/withdrawExchange/`

**Method** : `POST`

**Auth required** : NO

**Permissions required** : None

**Data constraints**

Provide exchange address.

```json
{
    "proposal": "[string]"
}
```

**Data example** All fields must be sent.

```json
{
"proposal":"010000000188ab6069a2b792919aa44985e8635f8c70e6b1cd82e452ff028d65525724cbb1000000006b483045022100aa2af7a6578b1784a0c220b60ced686c031aef804699d3f6d3561d500e74fbdd02202a738be114829f9163290533eb2de716fd71275db6216f5d893d486a5de835fc8321034ebeec63cd0ab6131d62d203dc178bcd33dba8df75f7c1a38eea394e577a8dfdffffffff0100000000000000003776a914eaaaa8cd21793342a6bb9ca8c0023f44720938fb88ac1c73706b7116ad7694442a5b94176ba35f723c8e5b40420f00000000007500000000"
}
```

## Success Response

**Condition** : If everything is OK and the proposal still is unfilled

**Code** : `200 OK`

**Content example**

```json
{
    "data": "2ab7f090fe51b78c458ec9b1e329bff55b199c4d1220ea4c8ca39b28d8bf7b75"
}
```
