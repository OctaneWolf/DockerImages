const express = require('express');
const app = new express();
let ip = "0.0.0.0";
//holder
app.post('/publicip', function(req, res, ){
   ip=req.originalUrl.slice(10)
    res.json(ip)
});

app.use(function(req, res){
    res.status(404);
    res.send({ error: "Sorry, can't find that" })
});
app.listen(3000)