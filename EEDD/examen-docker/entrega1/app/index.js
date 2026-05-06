const express = require("express");
const { MongoClient } = require("mongodb");

const app = express();
const port = 3000;

const url = "mongodb://root:DoD_CRM_DATABASE_25@mongo:27017";

const client = new MongoClient(url);

client.connect()
  .then(() => console.log("Conectado a MongoDB"))
  .catch(err => console.error(err));

app.get("/", (req, res) => {
  res.send("CRM funcionando 🚀");
});

app.listen(port, () => {
  console.log(`Servidor en puerto ${port}`);
});