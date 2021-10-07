# List All

Returns list of all active IoT Devices.

**URL** : `/api/v1/listAll

**Method** : `GET`

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

**Condition** : If everything is OK.

**Code** : `200 OK`

**Content example**

```json
{
    "data": [
        "package002",
        "package001"
    ]
}
```
