
function connectToDatabase(){
  var mysql = require('mysql');

  var con = mysql.createConnection({
    host: "localhost",
    user: "root",
    password: "admin"
  });
  
  con.connect(function(err) {
    if (err) throw err;
    console.log("Connected!");
  });
}//connectToDatabase

function insertSQL(SQL){
  var mysql = require('mysql');

  var con = mysql.createConnection({
    host: "localhost",
    user: "root",
    password: "admin"
  });
  
  con.connect(function(err) {
    if (err) throw err;
    con.query(SQL, function (err, result) {
      if (err) throw err;
      console.log(result);
    });
  });
}//insertSQL


function pingCheck(){
  var ping = require ('net-ping');
  var session = ping.createSession ();

  session.pingHost (target, function (error, target) {
    if (error)
        console.log (target + ": " + error.toString ());
    else
        console.log (target + ": Alive");
});
}//pingCheck

var express = require("express");
var login = require("./routes/loginroutes");
var bodyParser = require('body-parser');
var app = express();
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());
app.use(function(req, res, next) {
    res.header("Access-Control-Allow-Origin", "*");
    res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
    next();
});
var router = express.Router();
// test route
router.get('/', function(req, res) {
    res.json({ message: 'welcome to our upload module apis' });
});
//route to handle user registration
router.post('/register',login.register);
router.post('/login',login.login)
app.use('/api', router);
app.listen(5000);

