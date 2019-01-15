# SRC 3.1 Codes
| Code | Description | Severity |
| :---: | --- | :---: |
| A1 | Object Not Found: Same as HTTP Error 404 | 5 |
| A2 | Object is Restricted: The object is available, but has privaliged access. Log in to access the object| 2 |
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
| Fa1 | File Corrupted | 7-8|
| Fa2 | Unknown Corruption | 10 |
| Fa3 | Packages Sent to Unknown IP | 8-10 |
| G1 | Server Connected | 0 |
| G2 | Server Disconnected | 2-7 |
| G3 | Server Error | 5-9 |
| G4 | Server Virus | 10 |
### Code Breakdowns
+ A - Object Errors: A package sent to your website is malformed or doesn't exist
+ B - JS Errors : A JS document is malformed or doesn't exist.
+ C - HTML Errors: A HTML document is malformed or doesn't exist.
+ D - Version Info: A version of your website has been released, or not.
+ RSP - External Info: Someone viewed and made a pull request.
+ SRCS - Success Info: Success!!!
+ E - Unknowns: There is some error that SRC is unable to process.
+ F - Fatal Errors: These errors are involve file corruption or package missends.
+ G - Server Info: Your server status changed.
### Error Server Requests
| Request | Description | Server | Severity |
| --- | --- | --- | --- |
| error_user_null_request | The user used a function with a null parameter. Retry the function with the correct parameters | N/a | 1 |
| error_user_bad_request | The user linked or uploaded a corrupted file or package. The server rejected the package and your account has been put under a watch list. | TPP Security Portal | 3-7 |
| error_user_timed_out | The user took too long to respond in the response window. The server sut off the connection for security reasons. | TPP Security Portal/TPP Screen Watcher | 1 |
| error_user_host_insecure | The user is using an outdated browser/OS and needs to update it before granted access to the server | TPP Security Portal | 2 |
| error_user_bad_credentials | The user provide credentials that are outdated or lower clearance. Make sure our credentials are correct and reenter them | TPP Accounting Window | 1 |
| error_server_request_timed_out | The server took too long to respond so a different server cut your access to the server | TPP Security Portal | 4 |
| nginx | nginx | N/a | 1 |
#### Severity Scale
| 0 | 5 | 10 |
| --- | --- | --- |
| Not severe | Severe | Extremely Severe |
