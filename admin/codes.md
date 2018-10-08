# SRC 3.1 Error Codes
| Error Code | Dscription |
| --- | --- |
| A1 | Object Not Found: Same as HTTP Error 404 |
| A2 | Object is Restricted: The object is available, but has privaliged access. Login to access the object|
| A3 | Object Does Not Match Type Requested: The object requested is requested is a different type(e.g. request for `int()` but receive `str()`)|
| Aa | Unknown Object Error: the error is unknown |
| Ab | Multiple Object Error: There are multiple errors in the object |
| B1 | JS Document Not Found: The JS document requested was not found |
| B2 | JS Document is Restricted: The JS document is availabe, but has privaliged access. Login to acces the object |
| B3 | JS Not Rendering: The JS running is taking too long to respond due to a long-running script |
| B4 | JS is Malformed: There is a syntax error in the JS |
| Ba | Unknown JS Error: There is an unknown problem with the JS |
| Bb | Multiple JS Error: Ther are multiple errors in the JS document |
| C1 | HTML Document Not Found: Same as HTTP Error 404 |
| C2 | HTML Link Corrupted: There is something wrong with an object linked in the HTML document |
| C3/C7 | HTML Form Error: nginx |
| C4 | Form Served OVer Insecure Network: The HTML for was sending or recieving data from an insecure site |
