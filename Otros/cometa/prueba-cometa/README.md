# Prueba Técnica - Sistema de Reserva de Motos

Este es un proyecto Next.js con Drizzle ORM configurado para una prueba técnica de sistema de reserva de motos.

## 🚀 Setup

### 1. Instalar dependencias

```bash
pnpm install
```

### 2. Configurar variables de entorno

Crear archivo `.env` en la raíz del proyecto con:

```env
DATABASE_URL="postgresql://usuario:password@host:puerto/base_de_datos"
NEXT_PUBLIC_GOOGLE_MAPS_API_KEY="tu_api_key_de_google_maps"
```

**Notas**:
- Obtén tu `DATABASE_URL` desde el panel de Supabase en la sección de configuración de la base de datos.
- Para obtener una API key de Google Maps:
  1. Ve a [Google Cloud Console](https://console.cloud.google.com/)
  2. Crea un nuevo proyecto o selecciona uno existente
  3. Habilita la "Maps JavaScript API"
  4. Ve a "Credenciales" y crea una nueva API key
  5. Copia la API key y añádela a tu archivo `.env` como `NEXT_PUBLIC_GOOGLE_MAPS_API_KEY`

### 3. Ejecutar migraciones

Aplicar cambios directamente a la base de datos (recomendado para desarrollo):

```bash
pnpm db:push
```

O generar y aplicar migraciones:

```bash
pnpm db:generate
pnpm db:migrate
```

### 4. Seed de datos iniciales (opcional)

Para poblar la base de datos con motos de ejemplo en Palma de Mallorca:

```bash
pnpm db:seed
```

Esto insertará 5 motos de ejemplo en lugares emblemáticos de Palma de Mallorca:
- Catedral de Santa María de Palma (La Seu)
- Castillo de Bellver
- Baños Árabes
- Parque del Mar
- Plaza de España

### 5. Iniciar servidor de desarrollo

```bash
pnpm dev
```

Abrir [http://localhost:3001](http://localhost:3001) en el navegador.

**Nota**: Si no has configurado `NEXT_PUBLIC_GOOGLE_MAPS_API_KEY`, verás un mensaje de error en el mapa. Asegúrate de configurarla antes de iniciar el servidor.

## 📁 Estructura del Proyecto

```
├── app/
│   ├── api/
│   │   └── bikes/              # Endpoints de API para motos
│   │       ├── route.ts        # GET /api/bikes (listar todas)
│   │       └── [id]/
│   │           ├── route.ts    # GET /api/bikes/:id
│   │           ├── reserve/
│   │           │   └── route.ts    # POST /api/bikes/:id/reserve
│   │           ├── start-ride/
│   │           │   └── route.ts   # POST /api/bikes/:id/start-ride
│   │           └── end-ride/
│   │               └── route.ts   # POST /api/bikes/:id/end-ride
│   ├── components/
│   │   └── BikeMap.tsx         # Componente de mapa con Google Maps
│   ├── hooks/
│   │   └── useBikes.ts         # Hook de TanStack Query para obtener motos
│   ├── providers/
│   │   └── QueryProvider.tsx   # Provider de TanStack Query
│   └── page.tsx                # Página principal con mapa
├── src/
│   └── db/
│       ├── schema.ts           # Esquema Drizzle (tabla bikes)
│       └── index.ts            # Cliente de base de datos
├── scripts/
│   └── seed.ts                 # Script para poblar datos de ejemplo (Palma de Mallorca)
├── drizzle.config.ts           # Configuración de Drizzle Kit
└── PRUEBA_TECNICA.md           # Enunciado completo de la prueba
```

## 🔌 Endpoints de API Disponibles

### GET `/api/bikes`
Lista todas las motos. Aplica lazy expiration automáticamente.

**Response:**
```json
{
  "bikes": [
    {
      "id": 1,
      "status": "AVAILABLE",
      "latitude": "40.4168",
      "longitude": "-3.7038",
      ...
    }
  ]
}
```

### GET `/api/bikes/:id`
Obtiene una moto por ID.

### POST `/api/bikes/:id/reserve`
Reserva una moto por 15 minutos.

**Request Body:**
```json
{
  "userId": "user123"
}
```

### POST `/api/bikes/:id/start-ride`
Inicia un viaje en una moto reservada.

**Request Body:**
```json
{
  "userId": "user123"
}
```

### POST `/api/bikes/:id/end-ride`
Finaliza un viaje en curso.

**Request Body:**
```json
{
  "userId": "user123"
}
```

## 📊 Modelo de Datos

### Tabla `bikes`

- `id`: ID único (auto-incremental)
- `status`: Estado (`AVAILABLE`, `RESERVED`, `IN_USE`)
- `reservedUntil`: Timestamp de expiración de reserva
- `reservedBy`: ID del usuario que reservó
- `updatedAt`: Última actualización
- `rideStartedAt`: Timestamp de inicio del viaje
- `latitude`: Latitud de la moto
- `longitude`: Longitud de la moto

## 🛠️ Scripts Disponibles

- `pnpm dev` - Inicia servidor de desarrollo
- `pnpm build` - Construye para producción
- `pnpm start` - Inicia servidor de producción
- `pnpm lint` - Ejecuta ESLint
- `pnpm db:push` - Aplica cambios de schema directamente
- `pnpm db:generate` - Genera migraciones desde schema
- `pnpm db:migrate` - Aplica migraciones generadas
- `pnpm db:seed` - Pobla la base de datos con datos de ejemplo

## 📖 Documentación de la Prueba

Ver `PRUEBA_TECNICA.md` para el enunciado completo, requisitos, criterios de aceptación y guía de implementación.

## 🧪 Probar los Endpoints

Puedes probar los endpoints manualmente con curl o herramientas como Postman:

```bash
# Listar todas las motos
curl http://localhost:3000/api/bikes

# Obtener una moto específica
curl http://localhost:3000/api/bikes/1

# Reservar una moto
curl -X POST http://localhost:3000/api/bikes/1/reserve \
  -H "Content-Type: application/json" \
  -d '{"userId": "user123"}'

# Iniciar viaje
curl -X POST http://localhost:3000/api/bikes/1/start-ride \
  -H "Content-Type: application/json" \
  -d '{"userId": "user123"}'

# Finalizar viaje
curl -X POST http://localhost:3000/api/bikes/1/end-ride \
  -H "Content-Type: application/json" \
  -d '{"userId": "user123"}'
```
