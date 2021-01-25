# cheaf-backend-test

## Endpoint

Todas las peticiones de la API tienen como base la siguiente URL

`http://cheaf-backend-test.herokuapp.com/`

## Ejercicio 1 - CRUD de usuarios

### Crear un usuario nuevo

**Definición**

`POST /api/v1/user-crud/`

**Argumentos**
- `"username":string`, nombre de usuario.
- `"email":string`, correo con el que estará asociado el usuario registrado.
- `"password":string`, contraseña de autenticación del usuario.

**Response**
- `201 Created` on success
```json
{
    "url": "http://cheaf-backend-test.herokuapp.com/api/v1/user-crud/2/",
    "username": "testuser2",
    "email": "testuser2@email.com",
    "date_joined": "2021-01-25T06:37:09.113698Z"
}
```

### Leer a un usuario existente
**Definición**

`GET /api/v1/user-crud/<id>`

**Response**
- `200 OK` on success
```json
{
    "url": "http://cheaf-backend-test.herokuapp.com/api/v1/user-crud/2/",
    "username": "testuser2",
    "email": "testuser2@email.com",
    "date_joined": "2021-01-25T06:37:09.113698Z"
}
```

### Actualizar a un usuario existente

**Definición**

`PUT /api/v1/user-crud/<id>`

**Argumentos**
- `"username":string`, nombre de usuario.
- `"email":string`, correo con el que estará asociado el usuario registrado.
- `"password":string`, contraseña de autenticación del usuario.

**Response**
- `200 OK` on success
```json
{
    "url": "http://cheaf-backend-test.herokuapp.com/api/v1/user-crud/2/",
    "username": "testuser3",
    "email": "testuser3@email.com",
    "date_joined": "2021-01-25T06:37:09.113698Z"
}
```

### Eliminar a un usuario existente

**Definición**

`DELETE /api/v1/user-crud/<id>`

**Response**
- `204 No Content` on success
```json
{
}
```

### Ejercicio 2 - Lista de palabras al azar

**Definición**

`POST /api/v1/random-words/`

**Argumentos**
- `"words":list`, lista de strings con 10 palabras cualesquiera.

```json
{
    "words": [
        "prescription",
        "capture",
        "impress",
        "cheat",
        "capture",
        "impress",
        "plaintiff",
        "partner",
        "impress",
        "partner"
    ]
}
```

**Response**
- `200 OK` on success
```json
[
    {
        "prescription": 1
    },
    {
        "capture": 2
    },
    {
        "impress": 3
    },
    {
        "cheat": 1
    },
    {
        "plaintiff": 1
    },
    {
        "partner": 2
    }
]
```

### Ejercicio 3 - Distancia entre dos coordenadas

**Definición**

`POST /api/v1/dist-between-coords/`

**Argumentos**
- `"coords":list`, lista de dos diccionarios. Cada diccionario representa a una coordenada.
- `"lat": float/int`, numero que indica la latitud de la coordenada.
- `"long": float/int`, numero que indica la longitud de la coordenada.
  
```json
{
    "coords": [
        {
            "lat": 52.12212,
            "long": 12.12312
        },
        {
            "lat": 23.2313,
            "long": 23.23123
        }
    ]
}
```

**Response**
- `200 OK` on success
- `"dist_km":string`, distancia en kilómetros entre ambas coordenadas.
- `"dist_miles":string`, distancia en millas entre ambas coordenadas.

```json
{
    "dist_km": 3344.3756516279086,
    "dist_miles": 2078.0986859415443
}
```