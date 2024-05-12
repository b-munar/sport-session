# Instalacion

1. Clonar repositorio

```bash
git clone https://github.com/b-munar/event

2. 

```bash
docker compose build
docker compose up
```


El servicio de Servicios de terceros.

## 1. Get Sessions 

Retorna sesiones deportivas del usuario.

<table>
<tr>
<td> Método </td>
<td> GET </td>
</tr>
<tr>
<td> Ruta </td>
<td> <strong>localhost:6950/sport-session</strong> </td>
</tr>
<tr>
<td> Parámetros </td>
<td> N/A </td>
</tr>
<tr>
<td> Encabezados </td>
<td>N/A</td>
</tr>
<tr>
<td> Cuerpo </td>
<td>N/A</td>
</tr>
</table>

### Respuestas

<table>
<tr>
<th> Código </th>
<th> Descripción </th>
<th> Cuerpo </th>
</tr>
<tbody>
<td> 200 </td>
<td>En caso de exito</td>
<td>

```json
{
    "sessions": [
        {
            "id": "b17b69c9-739b-4056-bd0a-ddab1573eb8d",
            "trainingDayId": "86559da0-6100-45e1-84e7-85a304a6be21",
            "FTP": 78.0,
            "VO": 12.0,
            "RPM": 89.0,
            "KCAL": 110.0,
            "endDate": "2022-06-14 13:00:00",
            "startDate": "2022-06-14 13:00:00"
        },
        {
            "id": "70bd0832-a7d2-4453-8887-af5c980cd666",
            "trainingDayId": "86559da0-6100-45e1-84e7-85a304a6be21",
            "FTP": 70.0,
            "VO": 10.0,
            "RPM": 98.0,
            "KCAL": 300.0,
            "endDate": "2022-06-14 17:30:00",
            "startDate": "2022-06-14 17:00:00"
        }
    ]
}
```
</td>
</tr>
</tbody>
</table>

## 2. Post session 

Permite realizar el almacenamiento de información de una sesion deportiva.

<table>
<tr>
<td> Método </td>
<td> POST </td>
</tr>
<tr>
<td> Ruta </td>
<td> <strong>localhost:6950/sport-session</strong> </td>
</tr>
<tr>
<td> Parámetros </td>
<td> N/A </td>
</tr>
<tr>
<td> Encabezados </td>
<td>N/A</td>
</tr>
<tr>
<td> Cuerpo </td>
<td>

```json
 {
 "trainingDayId": "86559da0-6100-45e1-84e7-85a304a6be21",
 "FTP": 70,
 "VO": 10, 
 "RPM": 98,
 "KCAL": 300,
 "startDate": "2022-06-14T17:00:00-07:00",
 "endDate": "2022-06-14T17:30:00-07:00"
}
  ```
</td>
</tr>
</table>

### Respuestas

<table>
<tr>
<th> Código </th>
<th> Descripción </th>
<th> Cuerpo </th>
</tr>
<tbody>
<td> 200 </td>
<td>En caso de exito</td>
<td>

```json
{
    "id": "70bd0832-a7d2-4453-8887-af5c980cd666",
    "trainingDayId": "86559da0-6100-45e1-84e7-85a304a6be21",
    "FTP": 70.0,
    "VO": 10.0,
    "RPM": 98.0,
    "KCAL": 300.0,
    "endDate": "2022-06-14 17:30:00",
    "startDate": "2022-06-14 17:00:00"
}
```
</td>
</tr>
</tbody>
</table>

## 3. Get Sports Indices 

Retorna indices deportivos del usuario.

<table>
<tr>
<td> Método </td>
<td> GET </td>
</tr>
<tr>
<td> Ruta </td>
<td> <strong>localhost:6950/sport-session/avg</strong> </td>
</tr>
<tr>
<td> Parámetros </td>
<td> N/A </td>
</tr>
<tr>
<td> Encabezados </td>
<td>N/A</td>
</tr>
<tr>
<td> Cuerpo </td>
<td>N/A</td>
</tr>
</table>

### Respuestas

<table>
<tr>
<th> Código </th>
<th> Descripción </th>
<th> Cuerpo </th>
</tr>
<tbody>
<td> 200 </td>
<td>En caso de exito</td>
<td>

```json
{
    "average_results": [
        {
            "RPM": 93.5,
            "VO": 11.0,
            "FTP": 74.0,
            "KCAL": 205.0
        }
    ]
}
```
</td>
</tr>
</tbody>
</table>