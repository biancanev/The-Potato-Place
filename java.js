
myObj = {
    "name":"John",
    "age":30,
    "cars": {
        "car1":"Ford",
        "car2":"BMW",
        "car3":"Fiat"
    }
 } // Wait for DOM to load
document.addEventListener("DOMContentLoaded", function(event) {

  // Put the drop down into a variable
  var e = document.getElementById("jumpmenu");
  
  // Wait for user to select an option
  e.addEventListener("change", function() {
  
      // Put the selected value into a variable
      selectedURL = this.options[this.options.selectedIndex].value;
      
      // Check that the value is not null
      if (this.value != "null") {
      
        // Display the confirm box and put the response into a variable
        var confirmLeave = confirm("Are you sure?");
        
        // If user clicked "OK"
        if (confirmLeave==true) { 
        
          // Load the selected URL
          document.location.href = selectedURL; 
        }
        // If user clicked "Cancel"
        else { 
          return false;
        }
      }     
      
  });
  
});// Wait for DOM to load
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
document.addEventListener("DOMContentLoaded", function(event) {

  var e = document.getElementById("go");
  
  e.addEventListener( "click", function() {

    var name=prompt("What is your name?","Homer");
    if ( name!=null && name!="" ) {
      output = "Well " + name + ". You seem very daring!";
      }
    else {
      output = "Hey, I asked you your name!";
      }
    
    document.getElementById( "msg" ).innerText = output;

  }, false);
  
});
document.cookie = "username=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;"; 
document.cookie = "password=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;"; 






