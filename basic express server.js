var express = require("express");
var request = require("request");
var bodyParser = require("body-parser");


var app = express();

app.listen(process.env.PORT || 8000, function() {
  console.log("listening on: 8000");
});

app.use(bodyParser.json());
app.use(
  bodyParser.urlencoded({
    extended: false
  })
);

app.get("/", (req, res) => {

  res.send('ping');
};
