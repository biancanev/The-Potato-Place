# The-Potato-Place
Your Online Gaming/Other Random Things Site

# Contributing to The Potato Place

### Section 1
#### How To Contribute
Contributions are mandatory for all Potato Place Curators. In order to track each curators commits, we will use the commit function in our repository
Contributions must be in one of these forms:
* HTML(Hypertext Markup Language)
```html
<html>
    <body>
    <p>My First HTML script!</p>
    </body>
</html>
```
* CSS(Cascading Style Sheets)
```css
div{
    background-color: blue;
    position: absolute;
    width: 100%;
}
```
* JavaScript
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
* Python
```python
def happyBirthday(): #program does nothing as written
    print("Happy Birthday to you!")
    print("Happy Birthday to you!")
    print("Happy Birthday, dear person.")
    print("Happy Birthday to you!")
```

* PHP(Personal Homepage)
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
See full [documentation here.](https://github.com/biancanev/The-Potato-Place/blob/master/markups/CONTRIBUTING.md)
# Contributor Covenant Code of Conduct

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

See full [documentation here.](https://github.com/biancanev/The-Potato-Place/blob/master/markups/CODE_OF_CONDUCT.md)

### The Potato Place API

#### HTML API

```html
<!--To Create a new tab-->
<div id="tabname">
</div>
<!--Button for navbar-->
<button class="tablinks" onclick="openTab(event, 'tabname')"> Tab Name </button>
```
