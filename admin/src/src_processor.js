function test(object, request){
fetch(request).then(function(response) {
  console.log(response.status); // returns 200
  response.blob().then(function(myBlob) {
    var objectURL = URL.createObjectURL(myBlob);
    myImage.src = objectURL;
  });
});
}
