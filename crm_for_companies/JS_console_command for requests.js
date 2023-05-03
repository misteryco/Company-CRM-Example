/*
POST METHOD
*/

fetch('http://localhost:8000/api_employees/create/', {
  method: 'POST',
  body: JSON.stringify({
        "first_name": "77Person77",
        "last_name": "77Last77`",
        "date_of_birth": "2001-02-20",
        "position": "New Employee",
        "photo": "/home/yd/Pictures/py/3789820.png",
        "salary": 177,
        "company": 1
    }),
  headers: {
    'Content-type': 'application/json; charset=UTF-8',
    "x-csrftoken": "aol7LXWOcHEwCNGAVqhKoHbuWur2Rvaonxwbc32vAouTmkbHZC2qSXKBs4AwheV0",
  }
})
.then(res => res.json())
.then(console.log)


/*
This code is using the Fetch API to make a POST request to the URL http://localhost:8000/api_employees/create/ with the following JSON data in the request body:

{
    "first_name": "77Person77",
    "last_name": "77Last77`",
    "date_of_birth": "2001-02-20",
    "position": "New Employee",
    "photo": "/home/yd/Pictures/py/3789820.png",
    "salary": 177,
    "company": 1
}
The headers of the request include:

{
    'Content-type': 'application/json; charset=UTF-8',
    "x-csrftoken": "aol7LXWOcHEwCNGAVqhKoHbuWur2Rvaonxwbc32vAouTmkbHZC2qSXKBs4AwheV0",
}
The response of the request is then logged to the console using console.log().

The Fetch API provides an interface for fetching resources (including across the network) and provides a more powerful and flexible feature set than XMLHttpRequest1. It provides a JavaScript interface for accessing and manipulating parts of the protocol, such as requests and responses2. It also provides a global fetch() method that provides an easy, logical way to fetch resources asynchronously across the network3.

Is there anything else you would like me to help you with?
*/


/*
GET METHOD

GET
The GET method requests that the target resource transfer a representation of its state. GET requests should only
retrieve data and should have no other effect. (This is also true of some other HTTP methods.)[1] For retrieving
resources without making changes, GET is preferred over POST, as they can be addressed through a URL. This enables
bookmarking and sharing and makes GET responses eligible for caching, which can save bandwidth. The W3C has published
guidance principles on this distinction, saying, "Web application design should be informed by the above principles,
ut also by the relevant limitations."[53] See safe methods below.

*/
fetch("http://localhost:8000/api_employees/", {
  "headers": {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
  },
  "method": "GET",
});


fetch(
"http://localhost:8000/api_employees/",
{
"method": "GET",
}
);

/*
PUT METHOD
PUT
The PUT method requests that the target resource create or update its state with the state defined by the
representation enclosed in the request. A distinction from POST is that the client specifies the target location on
the server.
*/
fetch("http://localhost:8000/api_employees/update/1", {
    method: 'PUT',
    body: JSON.stringify({
        "id": 1,
        "first_name": "Spas",
        "last_name": "FirstEmployee",
        "date_of_birth": "2005-05-19",
        "position": "New Employee",
        "photo": "image/upload/v1683098179/veekdiz9x1lvu43kfeyh.png",
        "salary": 100001,
        "company": 1
       }),
    headers: {
    'Content-type': 'application/json; charset=UTF-8',
    "x-csrftoken": "aol7LXWOcHEwCNGAVqhKoHbuWur2Rvaonxwbc32vAouTmkbHZC2qSXKBs4AwheV0",
    }
    })
.then(res => res.json())
.then(console.log)


/*
DELETE METHOD
DELETE
The DELETE method requests that the target resource delete its state.

*/

fetch("http://localhost:8000/api_employees/delete/13", {
  "headers": {
    "x-csrftoken": "WfgZKqM2HFBWSTNAqwrsK4ieww6vh6mc9or3bwSJ5mrjCqiHuIc8ekRl26fZHP7O",
  },
  "method": "DELETE",
});

// Important - we need csrftoken because server is configured to ask for such a token

/*
HEAD
The HEAD method requests that the target resource transfer a representation of its state, as for a GET request, but
without the representation data enclosed in the response body. This is useful for retrieving the representation metadata
 in the response header, without having to transfer the entire representation. Uses include checking whether a page is
 available through the status code and quickly finding the size of a file (Content-Length).
*/

fetch(
"http://localhost:8000/api_employees/",
{
"method": "HEAD",
}
);

/*
OPTIONS

The OPTIONS method requests that the target resource transfer the HTTP methods that it supports. This can be used to
check the functionality of a web server by requesting '*' instead of a specific resource.
*/


fetch(
"http://localhost:8000/api_employees/",
{
"method": "OPTIONS",
}
);

/*
TRACE
The TRACE method requests that the target resource transfer the received request in the response body. That way a
client can see what (if any) changes or additions have been made by intermediaries.

ACTUALLY UNSUPPORTED
*/

fetch(
"http://localhost:8000/api_employees/delete/2",
{
"method": "TRACE",
}
);



/*
PATCH METHOD

PATCH
The PATCH method requests that the target resource modify its state according to the partial update defined in the
representation enclosed in the request. This can save bandwidth by updating a part of a file or document without having
to transfer it entirely.[58]
*/
fetch("http://localhost:8000/api_employees/update/14", {
    method: 'PATCH',
    body: JSON.stringify({
        "id": 14,
        "first_name": "Spas",
        "last_name": "FirstEmployee",
        "date_of_birth": "2005-05-19",
        "position": "New Employee",
        "photo": "image/upload/v1683098179/veekdiz9x1lvu43kfeyh.png",
        "salary": 100001,
        "company": 1
       }),
    headers: {
    'Content-type': 'application/json; charset=UTF-8',
    "x-csrftoken": "aol7LXWOcHEwCNGAVqhKoHbuWur2Rvaonxwbc32vAouTmkbHZC2qSXKBs4AwheV0",
    }
    })
.then(res => res.json())
.then(console.log)

CONNECT
The CONNECT method requests that the intermediary establish a TCP/IP tunnel to the origin server identified by the
request target. It is often used to secure connections through one or more HTTP proxies with TLS.[56][57] See
HTTP CONNECT method.


