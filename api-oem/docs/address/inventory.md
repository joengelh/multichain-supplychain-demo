# Inventory

Displays list of assets belonging to the OEM.

**URL** : `/api/v1/inventory/`

**Method** : `GET`

**Auth required** : NO

**Permissions required** : None

**Data constraints**

NO

**Data example** All fields must be sent.

```json
}
}
```

## Success Response

**Condition** : If everything is OK.

**Code** : `200 OK`

**Content example**

```json
{
    "data": [
        {
            "name": "lenovoServer",
            "assetref": "954-267-38169",
            "qty": 2
        },
        {
            "name": "ibmServer",
            "assetref": "953-267-10558",
            "qty": 1
        }
    ]
}
```
