import express from 'express';
import { v4 as uuidv4 } from 'uuid';
const app = express();
app.use(express.json());
import { productos } from './database.js';
// Nota: `productos` se importa desde la base de datos en memoria. Las modificaciones
const ejecutaValidacion = (data, validacion, mensajedeError) =>
     validacion(data) ? data : { error: mensajedeError }
app.route('/productos')
     .get((req, res) => {
         res.json(productos)
     })
     .post((req, res) => {
         // destructuracion    (pedir a chatgPT otra forma)
         const { titulo, precio } = req.body
         const nuevoProducto = {
            id: uuidv4(),
            titulo: titulo
         }
         const valida_titulo = ejecutaValidacion(
            titulo,
            data => data && data.length > 3,
            'Mínimo de 4 carácteres'
         )
         if (valida_titulo.error) {
            res.status(400).send(valida_titulo.error)
            return
        }
        productos.push(nuevoProducto)
        res.status(201).json(nuevoProducto) // respuesta creado producto
    })
app.get('/', (req, res) => {
     res.send('Backend productos')
})
app.listen(3000, () => {
     console.log('Activado localhost:3000.')
})