// Wait for DOM to load
document.addEventListener("DOMContentLoaded", function(event) {

  // Put the button into a variable
  var e = document.getElementById("go");
  
  // Wait for user to click the button
  e.addEventListener( "click", function() {

    // Do the prompt and save user input to a variable
    var name = prompt("What is your name?","Homer");
    
    // Write out the user's input
    document.getElementById( "msg" ).innerText = name;

  }, false);
  
});
