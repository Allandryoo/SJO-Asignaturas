const express = require('express')
const cors = require('cors')
const productosController = require('./productos/productos.controller')

const app = express()

// Middlewares
app.use(express.json()) // reemplaza body-parser
app.use(cors())

// Rutas de productos
app.route('/productos')

  // Obtener productos
  .get(async (req, res) => {
    try {
      const listaProductos = await productosController.obtenerListaProductos()
      res.json(listaProductos)
    } catch (error) {
      console.error(error.message)
      res.status(500).json({
        error: 'Error al obtener la lista de productos'
      })
    }
  })

  // Crear producto
  .post(async (req, res) => {
    try {
      const nuevoProducto = req.body

      const productoCreado =
        await productosController.crearProducto(nuevoProducto)

      res.status(201).json(productoCreado)

    } catch (error) {
      console.error(error.message)
      res.status(500).json({
        error: 'Error al crear el producto'
      })
    }
  })

// Ruta principal
app.get('/', (req, res) => {
  res.send('Backend productos funcionando')
})

// Iniciar servidor
const PORT = 3000

app.listen(PORT, () => {
  console.log(`Servidor activado en http://localhost:${PORT}`)
})