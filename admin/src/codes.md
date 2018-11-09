# SRC 3.1 Codes
| Code | Description | Severity |
| --- | --- | --- |
| A1 | Object Not Found: Same as HTTP Error 404 | 5 |
| A2 | Object is Restricted: The object is available, but has privaliged access. Login to access the object| 2 |
| A3 | Object Does Not Match Type Requested: The object requested is requested is a different type(e.g. request for `int()` but receive `str()`)| 3 |
| Aa | Unknown Object Error: the error is unknown | 5 |
| Ab | Multiple Object Error: There are multiple errors in the object | 7 |
| B1 | JS Document Not Found: The JS document requested was not found | 5 |
| B2 | JS Document is Restricted: The JS document is availabe, but has privaliged access. Login to acces the object | 2 |
| B3 | JS Not Rendering: The JS running is taking too long to respond due to a long-running script | 5 |
| B4 | JS is Malformed: There is a syntax error in the JS | 3-6 |
| Ba | Unknown JS Error: There is an unknown problem with the JS | 5 |
| Bb | Multiple JS Error: Ther are multiple errors in the JS document | 7 |
| C1 | HTML Document Not Found: Same as HTTP Error 404 | 5 |
| C2 | HTML Link Corrupted: There is something wrong with an object linked in the HTML document | 9 |
| C3/C7 | HTML Form Error: nginx | 7 |
| C4 | Form Served Over Insecure Network: The HTML for was sending or recieving data from an insecure site | 6 |
| C5 | HTML is Malformed: HTML syntax error | 3-6 |
| Ca6 | Unknown HTML Form Error: soething went wrong in the form request | 7 |
| D1 | Version Update | 0 |
| D2 | Version Restore | 0 |
| D3 | Version Backup | 0 |
| D4 | Version Error | 8 |
| RSP1 | External Comment | 0 |
| RSP2 | External Edit | 0 |
| RSP3 | External Request | 0 |
| RSP4 | External Fork | 0 |
| SRCS1 | Form Success | 0 |
| SRCS2 | Update Success | 0 |
| Ea1 | Unknown Error | 1-10 |
| Ea2 | Unknown Malform | 1-5 |
#### Severity Scale
| 0 | 5 | 10 |
| --- | --- | --- |
| Not severe | Severe | Extremely Severe |
