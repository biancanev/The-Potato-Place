# The-Potato-Place

## Contributing to The Potato Place

### Section 1
#### How To Contribute
Contributions are mandatory for all Potato Place Curators. In order to track each curators commits, we will use the commit function in our repository
Contributions must be in one of these forms:
* HTML(Hypertext Markup Language){.html}
```html
<html>
    <body>
    <p>My First HTML script!</p>
    </body>
</html>
```
* CSS(Cascading Style Sheets){.css}
```css
div{
    background-color: blue;
    position: absolute;
    width: 100%;
}
```
* JavaScript{.js}
```javascript
function getCookie(cname) {
    var name = cname + "=";
    var decodedCookie = decodeURIComponent(document.cookie);
    var ca = decodedCookie.split(';');
    for(var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}
```
* Python{.py}
```python
def happyBirthday(): #program does nothing as written
    print("Happy Birthday to you!")
    print("Happy Birthday to you!")
    print("Happy Birthday, dear person.")
    print("Happy Birthday to you!")
```

* PHP(Personal Homepage){.php}
```php
<?php
$x = 5;
$y = 10;

function myTest() {
    $GLOBALS['y'] = $GLOBALS['x'] + $GLOBALS['y'];
} 

myTest();
echo $y;
?>
```

* MD(Markup Documents){.md}
```
# MD equivilent of <h1>
## MD equivilent of <h2>
### MD equivilent of <h3>
#### MD equivilent of <h4>
##### MD equivilent of <h5>
###### MD equivilent of <h6>
MD equivilent of <p>
[value](href) MD equivilent of <a href="https://www.example.com/directory"></a>
```
See full documentation [here.](https://github.com/biancanev/The-Potato-Place/blob/master/markups/CONTRIBUTING.md)
## Contributor Covenant Code of Conduct

## Our Pledge

In the interest of fostering an open and welcoming environment, we as contributors and maintainers pledge to making participation in our project and our community a harassment-free experience for everyone, regardless of age, body size, disability, ethnicity, gender identity and expression, level of experience, nationality, personal appearance, race, religion, or sexual identity and orientation.

## Our Standards

Examples of behavior that contributes to creating a positive environment include:

* Using welcoming and inclusive language
* Being respectful of differing viewpoints and experiences
* Gracefully accepting constructive criticism
* Focusing on what is best for the community
* Showing empathy towards other community members

Examples of unacceptable behavior by participants include:

* The use of sexualized language or imagery and unwelcome sexual attention or advances
* Trolling, insulting/derogatory comments, and personal or political attacks
* Public or private harassment
* Publishing others' private information, such as a physical or electronic address, without explicit permission
* Other conduct which could reasonably be considered inappropriate in a professional setting

## Our Responsibilities

Project maintainers are responsible for clarifying the standards of acceptable behavior and are expected to take appropriate and fair corrective action in response to any instances of unacceptable behavior.

Project maintainers have the right and responsibility to remove, edit, or reject comments, commits, code, wiki edits, issues, and other contributions that are not aligned to this Code of Conduct, or to ban temporarily or permanently any contributor for other behaviors that they deem inappropriate, threatening, offensive, or harmful.

See full documentation [here.](https://github.com/biancanev/The-Potato-Place/blob/master/markups/CODE_OF_CONDUCT.md)

## Copying Other Work

Copying of other websites is strictly prohibited. There are 2 instances where you may copy code from another person/website:

* If the website/program is open source.
* If the creator gave explicit permission to you to copy the code

Any violation of these rules will result in an immediate ban.

### The Potato Place APIs

#### HTML APIs
##### Creating a New Tab On the Navbar
###### Content
```html
<div id="tabname">
    <!--Content goes here-->
</div>
```
###### Button Link
```html
<!--Button for navbar-->
<button class="tablinks" onclick="openTab(event, 'tabname')"> Tab Name </button>
```

##### Add Javascript
```javascript
//To make a Navbar
function openTab(evt, cityName) {//You can change the cityName parameter to anything
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(cityName).style.display = "block";
    evt.currentTarget.className += " active";
}
```
 ### The Potato Place's Discord
 
 We use Discord for recreational purposes. There is no formal use of it other than to play around with the bots and have fun with other users online.
