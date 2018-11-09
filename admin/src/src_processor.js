function test(object, request){
fetch(request).then(function(response) {
  console.log(response.status); // returns 200
  response.blob().then(function(myBlob) {
    var objectURL = URL.createObjectURL(myBlob);
    object.src = objectURL;
  });
  return response.status;
});
}
function name(obj, req){
  var etype, enum;
  var x = test(obj, req);
  if(x[0] == 1){
    etype = "A";
    var a = 1;
    var bool = false;
    while(bool == false){
      if(x[2] == 1a){
        enum = "1";  
      }
    }
  }
}
