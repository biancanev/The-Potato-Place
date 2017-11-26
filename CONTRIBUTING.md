# Contributing to The Potato Place

### Introduction
The Potato Place is a place where eveyone needs to contribute. In order to ensure this, we have set up a few guidelines.
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
def happyBirthdayEmily(): #program does nothing as written
    print("Happy Birthday to you!")
    print("Happy Birthday to you!")
    print("Happy Birthday, dear Emily.")
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

For example:
```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta content="stuff, to, help, search, engines, not" name="keywords">
<meta content="What this page is about." name="description">
<meta content="Display Webcam Stream" name="title">
<title>The Potato Place | Webchat</title>
<style>
button:hover{
    opacity: 0.65;
    }
video:hover{
    opacity: 0.65;
    }
#container {
    margin: 0px auto;
    width: 100%;
    height: 80%;
    border: 10px #333 solid;
}
#videoElement {
    width: 100%;
    height: 80%;
    min-width: 1000px;
    mindheight: 800px;
    background-color: #666;
    border: 10px #333 solid;
}
#launchBtn {
    background-color: LightGreen;
    }
</style>
</head>
<body><center>
<div id="container">
    <video autoplay="true" id="videoElement" onclick="VideoLaunchFunction()" onload="checkCookie"></video>
</div>
  </center>
    <button onclick="loading.innerHRML='Connection failed. please try again'" id="launchBtn">Launch Chat</button>
  <button onclick="javascript:screenshare();" disabled id="shareBtn">Share your screen</button>
  <div id="camera-publisher"></div>
  <div id="camera-subscriber"></div>
  <div id="screen-subscriber"></div>

<script>
function setCookie(cname,cvalue,exdays) {
    var d = new Date();
    d.setTime(d.getTime() + (exdays*24*60*60*1000));
    var expires = "expires=" + d.toGMTString();
    document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}
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
function checkCookie() {
    var user=getCookie("username");
    if (user != "") {
        alert("Welcome again " + user);
    } else {
       user = prompt("Please enter your name:","");
       if (user != "" && user != null) {
           setCookie("username", user, 30);
       }
    }
}
    
 var video = document.querySelector("#videoElement");
navigator.getUserMedia = navigator.getUserMedia || navigator.webkitGetUserMedia || navigator.mozGetUserMedia || navigator.msGetUserMedia || navigator.oGetUserMedia;
if (navigator.getUserMedia) {       

    navigator.getUserMedia({video: true}, handleVideo, videoError);
}
function handleVideo(stream) {
    video.src = window.URL.createObjectURL(stream);
}
function videoError(e) {
    alert("Video Feed Error. Sorry, we don't know what happened. Are you on v.0.92.5?");
}
  </script>
        <script>
        function VideoLauchFunction(){
            alert("Error 408. Request Timeout.");
        }
    </script>
  <script src="//static.opentok.com/v2/js/opentok.js"></script>
    <script type="text/javascript">
    // Go to https://dashboard.tokbox.com/ to get your OpenTok API Key and to generate
    // a test session ID and token:
    var apiKey    = '',
      sessionId = '',
      token     = '';
    // Replace this with the ID for your Chrome screen-sharing extension, which you can
    // get at chrome://extensions/:
    var extensionId = '<YOUR_CHROME_EXTENSION_ID>';
    // If you register your domain with the the Firefox screen-sharing whitelist, instead of using
    // a Firefox screen-sharing extension, set this to the Firefox version number, such as 36, in which
    // your domain was added to the whitelist:
    var ffWhitelistVersion; // = '36';
    var session = OT.initSession(apiKey, sessionId);
    session.connect(token, function(error) {
      if (error) { 
        alert('Error connecting to session: ' + 'Your server address is undefined. Please try again. -- Google says: ' + error.message);
        return;
      }
      // publish a stream using the camera and microphone
      var publisher = OT.initPublisher('camera-publisher');
      session.publish(publisher);
      document.getElementById('shareBtn').disabled = false;
    });
    session.on('streamCreated', function(event) {
      if (event.stream.videoType === 'screen') {
        // This is a screen-sharing stream published by another client
        var subOptions = {
          width: event.stream.videoDimensions.width / 2,
          height: event.stream.videoDimensions.height / 2
        };
        session.subscribe(event.stream, 'screen-subscriber', subOptions);
      } else {
        // This is a stream published by another client using the camera and microphone
        session.subscribe(event.stream, 'camera-subscriber');
      }
    });
    // For Google Chrome only, register your extension by ID,
    // You can find it at chrome://extensions once the extension is installed
    OT.registerScreenSharingExtension('chrome', extensionId, 2);
    function screenshare() {
      OT.checkScreenSharingCapability(function(response) {
        console.info(response);
        if (!response.supported || response.extensionRegistered === false) {
          alert('This browser does not support screen sharing.');
        } else if (response.extensionInstalled === false
            && (response.extensionRequired || !ffWhitelistVersion)) {
            alert('Please install the screen-sharing extension and load this page over HTTPS.');
        } else if (ffWhitelistVersion && navigator.userAgent.match(/Firefox/)
          && navigator.userAgent.match(/Firefox\/(\d+)/)[1] < ffWhitelistVersion) {
            alert('For screen sharing, please update your version of Firefox to '
              + ffWhitelistVersion + '.');
        } else {
          // Screen sharing is available. Publish the screen.
          // Create an element, but do not display it in the HTML DOM:
          var screenContainerElement = document.createElement('div');
          var screenSharingPublisher = OT.initPublisher(
            screenContainerElement,
            { videoSource : 'screen' },
            function(error) {
              if (error) {
                alert('Something went wrong: ' + error.message);
              } else {
                session.publish(
                  screenSharingPublisher,
                  function(error) {
                    if (error) {
                      alert('Something went wrong: ' + error.message);
                    }
                  });
              }
            });
          }
        });
    }
  </script>
      <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
    <script>
        $("document").ready(function(){
            $(".videoElement").click(function(){
                alert('ERROR 408. Request Timeout.');
            });
        });
    </script>
  <p id="loading">Looking for other users . . .</p>
  <p id="loading">Locating a server . . .</p>
  <p id="loading">Connection Status <---> OFFLINE</p>
</body>
</html>

``` 
is an acceptable contribution.
Failure to contribute may result in being kicked out of the repository

### Section 2
#### Adding a new Contributor
To add a new contributor, you first need to ask biancanev or ConnorPark to add a contributor. A message should look something like this:
```
@biancanev, Can we add examplename to our repository? I think he/she will be a big help with the PHP. 
-- thanks, Your name
```

You should get a response like this:
```
@Your name, Thank you for contacting me to add examplename to our repository, yes, please do add examplename to our repository!
-- biancanev
```
or
```
@Your name, Thank uou for contacting me to add examplename to our repository, however, I do not believe that this person is fit to edit the repository
--Thanks for understanding
biancanev
```

### Section 3
#### Removing a Current Contributor
Sometimes there is going to be a contributor that is just not helping, or is becoming a negative impact. If this is so, then please contact biancanev to ask for removal. Your message should look like this:
```
@biancanev, I feel that examplename is becoming a negative impact for me, and the rest of the contributors. I feel that we should remove him/her from the repository. 
--Thanks for your time
Your name
```

### Section 4
#### Consequences
If your contributions intentionally try to target a person, you will be severely punished. This includes:

* Consistantly poking fun at a person
* Using inappropriate language
* Talking about political/economical topics
For example:

```
@exampleperson1, what are you thinking? b---ch you better delete that dumb script.
```


Consequences will vary by the severity of the action.

Also, adding or removing a contributor _(see sections 2 & 3)_ is strictly prohibited. If found adding or removing a contributor, you will be kicked out automatically.
### Section 5
#### Getting Help
Getting help is not hard at all. Whether it be your code is not working, or you just don't know what to add, you can always add an issue in our issue tab, and we will get to it as soon as possible. Your post should look something like this:
```
@everyone, ASK YOUR QUESTION HERE. DESCRIBE WHAT YOU NEED HELP WITH. BE CONSISE.
-- YourName
```
As always you need to be consise and specific with your post.

