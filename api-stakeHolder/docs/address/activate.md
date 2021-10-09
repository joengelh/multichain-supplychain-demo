# Activate

Activates Iot Device as a multichain stream and writes data to it.

**URL** : `/api/v1/activate/`

**Method** : `POST`

**Auth required** : NO

**Permissions required** : None

**Data constraints**

Provide Name

```json
{
    "name": "[string]"
}
```

**Data example** All fields must be sent.

```json
{
    "name": "package001"
}
```

## Success Response

**Condition** : If everything is OK.

**Code** : `200 OK`

**Content example**

```json
{
    "data": "package001"
}
```
