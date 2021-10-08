# Balance

Quantitiy of specified asset belonging to wallet 0 of node.

**URL** : `/api/v1/balance/`

**Method** : `GET`

**Auth required** : NO

**Permissions required** : None

**Data constraints**

Provide asset to query for

**Data example** All fields must be sent.

```json
}
    "asset": "[String]"
}
```

## Success Response

**Condition** : If everything is OK.

**Code** : `200 OK`

**Content example**

```json
{
    "data": 0
}
```
