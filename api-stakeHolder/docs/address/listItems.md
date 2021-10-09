# List Items

Returns list of all items written by specific IoT Device.

**URL** : `/api/v1/listItems

**Method** : `GET`

**Auth required** : NO

**Permissions required** : None

**Data constraints**

Name of IoT Device

```json
{
    "name":"[string]"
}
```

**Data example** All fields must be sent.

```json
{
    "name":"device1"
}
```

## Success Response

**Condition** : If everything is OK and sensor is active.

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
