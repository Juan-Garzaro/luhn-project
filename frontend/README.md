# Levantamiento y Pruebas del Proyecto

## Levantar PROYECTO

###  PRODUCCIÓN

```bash
docker-compose up -d --build
```

Probar en:
http://localhost:3000

---

### PREPRODUCCIÓN

```bash
docker-compose -f docker-compose.yml -f docker-compose.pre.yml up -d --build
```

 Probar en:
http://localhost:3001

---

## PRUEBA 

1. Abrir el frontend
2. Ingresar número válido:

```
4532015112830366
```

3. Resultado esperado:

```
✅ Número válido
```
4. Ingresar número Inválido:

```
3150
```

5. Resultado esperado:

```
❌ Número Inválido
```
6. Luego acceder a:

* Producción: http://localhost:8080
* Preproducción: http://localhost:8081

Verificar que el número válido se guardó en la base de datos

---

## Acceso a Adminer (Base de Datos)

URL: http://localhost:8080

**Nota:** Adminer no tiene autenticación propia. Se conecta directamente a la base de datos.

### Configuración:

* **System:** PostgreSQL
* **Server:** db
* **Username:** admin
* **Password:** admin
* **Database:**

  * `luhn_prod` → Producción
  * `luhn_pre` → Preproducción

