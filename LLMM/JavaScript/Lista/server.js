const express = require("express");
const fs = require("fs");
const path = require("path");

const app = express();

// Middleware
app.use(express.static("public"));
app.use(express.urlencoded({ extended: true }));
app.use(express.json());

// Ruta para guardar datos
app.post("/guardar", (req, res) => {
  const nuevoUsuario = req.body;

  const filePath = path.join(__dirname, "data", "data.json");

  let datos = [];

  if (fs.existsSync(filePath)) {
    datos = JSON.parse(fs.readFileSync(filePath));
  }

  datos.push(nuevoUsuario);

  fs.writeFileSync(filePath, JSON.stringify(datos, null, 2));

  res.send("Guardado correctamente");
});

// Servidor
app.listen(3000, () => {
  console.log("Servidor en http://localhost:3000");
});