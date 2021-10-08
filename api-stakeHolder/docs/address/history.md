# List Transactions

Returns a list of the last 10 transactions from the wallet.

**URL** : `/api/v1/listTransactions/`

**Method** : `GET

**Auth required** : NO

**Permissions required** : None

**Data constraints**

NO

```json
{
}
```

**Data example** All fields must be sent.

```json
{
}
```

## Success Response

**Condition** : If everything is OK and the proposal exists.

**Code** : `200 OK`

**Content example**

```json
{
    "data": [
        {
            "balance": {
                "amount": 0,
                "assets": []
            },
            "myaddresses": [
                "1YiYg4zzyMq2oLjjDNLTT7oTHuq1QR1i8JuRRk"
            ],
            "addresses": [],
            "permissions": [],
            "items": [],
            "data": [],
            "confirmations": 130,
            "blockhash": "006ea5416509a1fd4de05e2913f3abbb4ea82c06b4515ceb76ac8dd995dc625a",
            "blockindex": 1,
            "blocktime": 1633637177,
            "txid": "19fac134faaa9da58fc5c5c144fece9d3044199b62256c22d169b1a14e5985f5",
            "valid": true,
            "time": 1633637158,
            "timereceived": 1633637158
        },
        {
            "balance": {
                "amount": 0,
                "assets": []
            },
            "myaddresses": [
                "1YiYg4zzyMq2oLjjDNLTT7oTHuq1QR1i8JuRRk"
            ],
            "addresses": [],
            "permissions": [],
            "items": [],
            "data": [],
            "confirmations": 94,
            "blockhash": "00a2babf84c21a8a249a3c4f778f2096a8c3ade311fbe6af8a228ea42b8213bb",
            "blockindex": 1,
            "blocktime": 1633637728,
            "txid": "36dfebd9aee5bb5da3a20444b36c278c7a70acefec90e94c79e4d84cac373246",
            "valid": true,
            "time": 1633637709,
            "timereceived": 1633637709
        },
        {
            "balance": {
                "amount": 0,
                "assets": []
            },
            "myaddresses": [
                "1YiYg4zzyMq2oLjjDNLTT7oTHuq1QR1i8JuRRk"
            ],
            "addresses": [],
            "permissions": [],
            "items": [],
            "data": [],
            "confirmations": 90,
            "blockhash": "0092e24df87453f332dcfbfec38951d9db67c7b2283f167fe38bc1644110ee01",
            "blockindex": 1,
            "blocktime": 1633637772,
            "txid": "a529adb21faf17a7aab7b130d073f625e6feac78dbbe851ca1f12ae5e5f78802",
            "valid": true,
            "time": 1633637756,
            "timereceived": 1633637756
        },
        {
            "balance": {
                "amount": 0,
                "assets": []
            },
            "myaddresses": [
                "1YiYg4zzyMq2oLjjDNLTT7oTHuq1QR1i8JuRRk"
            ],
            "addresses": [],
            "permissions": [],
            "items": [],
            "data": [],
            "confirmations": 89,
            "blockhash": "00c58a30323b72e7fc522527bf7f0accf4f621bbde0b714d98b9e944ed51f75a",
            "blockindex": 1,
            "blocktime": 1633637789,
            "txid": "6cc3b0a324666e584baf5ce0917d4bcb5868f652ce9ff8d556c68e45e143b282",
            "valid": true,
            "time": 1633637788,
            "timereceived": 1633637788
        },
        {
            "balance": {
                "amount": 0,
                "assets": []
            },
            "myaddresses": [
                "1YiYg4zzyMq2oLjjDNLTT7oTHuq1QR1i8JuRRk"
            ],
            "addresses": [],
            "permissions": [],
            "items": [],
            "data": [],
            "confirmations": 72,
            "blockhash": "0093729f84d18f4db4add4ec547cc220bc29a4ef9ba932aa64690f59366abdc8",
            "blockindex": 1,
            "blocktime": 1633638039,
            "txid": "bfba277a3bd39d98470dc435653db3b7b064df95a8a17a6596c9f7cac5e14b1a",
            "valid": true,
            "time": 1633638035,
            "timereceived": 1633638035
        },
        {
            "balance": {
                "amount": 0,
                "assets": []
            },
            "myaddresses": [
                "1YiYg4zzyMq2oLjjDNLTT7oTHuq1QR1i8JuRRk"
            ],
            "addresses": [],
            "permissions": [],
            "items": [],
            "data": [],
            "confirmations": 71,
            "blockhash": "002457054b59ce93e0567f4430a835f7ae4e985d509dbb887df93f9e66da4273",
            "blockindex": 1,
            "blocktime": 1633638060,
            "txid": "32518e74f3c7110bf7ff0ea852c7f6e0b90e463ceee3e17d4d3f51320736588b",
            "valid": true,
            "time": 1633638050,
            "timereceived": 1633638050
        },
        {
            "balance": {
                "amount": 0,
                "assets": []
            },
            "myaddresses": [
                "1YiYg4zzyMq2oLjjDNLTT7oTHuq1QR1i8JuRRk"
            ],
            "addresses": [],
            "permissions": [],
            "items": [],
            "data": [],
            "confirmations": 49,
            "blockhash": "00e4ec0514954d91d0dc616ee0741da7aeb2a092cb9c5fa0e4164c92a63b57a7",
            "blockindex": 1,
            "blocktime": 1633638453,
            "txid": "b1cb245752658d02ff52e482cdb1e6708c5f63e88549a49a9192b7a26960ab88",
            "valid": true,
            "time": 1633638439,
            "timereceived": 1633638439
        },
        {
            "balance": {
                "amount": 0,
                "assets": []
            },
            "myaddresses": [
                "1YiYg4zzyMq2oLjjDNLTT7oTHuq1QR1i8JuRRk"
            ],
            "addresses": [],
            "permissions": [],
            "items": [],
            "data": [],
            "confirmations": 30,
            "blockhash": "000503cd57ef344ac2c23113a7a3146e6a05b63a66ec070ffd14d28494e95cef",
            "blockindex": 1,
            "blocktime": 1633638698,
            "txid": "88f5c307069ecbab174076104fcba499ec5d978c43a2ad7b1895e4a6e53b6ea8",
            "valid": true,
            "time": 1633638696,
            "timereceived": 1633638696
        },
        {
            "balance": {
                "amount": 0,
                "assets": []
            },
            "myaddresses": [
                "1YiYg4zzyMq2oLjjDNLTT7oTHuq1QR1i8JuRRk"
            ],
            "addresses": [],
            "permissions": [],
            "items": [],
            "data": [],
            "confirmations": 23,
            "blockhash": "00b22e4a992a1b6c6414f623589df20bc8ad77bf0ba5291b1984815a12e9be51",
            "blockindex": 1,
            "blocktime": 1633638812,
            "txid": "5cdcbb998e4bce89464c82cffff191a93a657fa5d1bdfc0877fd96fff61ed17a",
            "valid": true,
            "time": 1633638797,
            "timereceived": 1633638797
        },
        {
            "balance": {
                "amount": 0,
                "assets": []
            },
            "myaddresses": [
                "1YiYg4zzyMq2oLjjDNLTT7oTHuq1QR1i8JuRRk"
            ],
            "addresses": [],
            "permissions": [],
            "items": [],
            "data": [],
            "confirmations": 21,
            "blockhash": "00952b1d4def2d1541ce6cc458cb1e212b6275d7443e3c0fa13510ad6ade08a2",
            "blockindex": 1,
            "blocktime": 1633638833,
            "txid": "2ab7f090fe51b78c458ec9b1e329bff55b199c4d1220ea4c8ca39b28d8bf7b75",
            "valid": true,
            "time": 1633638819,
            "timereceived": 1633638819
        }
    ]
}
```
