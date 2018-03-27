require('http');
http.createServer(function (req, res) {
  res.write('Test Node JS')
  res.end();
}.listen(8080);
