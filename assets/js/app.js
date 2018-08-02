function modify_div(x,y,width,height,id,round){
  var element = document.getElementById(id);
  element.style.left = x;
  element.style.bottom = y;
  element.style.width = width;
  element.style.height = height;
  //round parameter is optional
  if(round === undefined){
    return false;
  }else{
    element.style.borderRadius = round;
  }
}
//For Chats[Not in use]
function create_Session(){
  var name, id;
  name = prompt("Chat Session Creation Step 1 of 2:\nEnter the name you want to use this session");
  sessionStorage.setItem("name", name);
  id = prompt("Chat Session Creation Step 2 0f 2\nEnter a TPP Chat ID(this step is optional)");
  if(id === undefined){
   id = Math.floor(Math.random()*100000000) 
  }
  return name + id;
}
