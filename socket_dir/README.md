Starting out server 

```
python -m http.server 9001
```

outout 
```
python -m http.server 9001
Serving HTTP on 0.0.0.0 port 9001 (http://0.0.0.0:9001/) ...

127.0.0.1 - - [14/Dec/2019 12:25:51] "GET / HTTP/1.1" 200 -
^C
Keyboard interrupt received, exiting.
```
CURL to check if server is running

```
 curl http://0.0.0.0:9001
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<title>Directory listing for /</title>
</head>
<body>
<h1>Directory listing for /</h1>
<hr>
<ul>
<li><a href=".git/">.git/</a></li>
<li><a href=".idea/">.idea/</a></li>
<li><a href="misc/">misc/</a></li>
<li><a href="process_synchronization/">process_synchronization/</a></li>
<li><a href="README.md">README.md</a></li>
<li><a href="reconnaissance/">reconnaissance/</a></li>
<li><a href="socket_dir/">socket_dir/</a></li>
<li><a href="socket_wrapper.py">socket_wrapper.py</a></li>
<li><a href="sorts/">sorts/</a></li>
</ul>
<hr>
</body>
</html>
```

Run client 
```
s = SocketWrapper("127.0.0.1",9001)
s.get_details( "abcd")
```

outout 
```
s.get_details("1234")                                                                                                                                                                               
Out[2]: '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"\n        "http://www.w3.org/TR/html4/strict.dtd">\n<html>\n    <head>\n        <meta http-equiv="Content-Type" content="text/html;charset=utf-8">\n        <title>Error response</title>\n    </head>\n    <body>\n        <h1>Error response</h1>\n        <p>Error code: 400</p>\n        <p>Message: Bad request syntax (\'1234\').</p>\n        <p>Error code explanation: HTTPStatus.BAD_REQUEST - Bad request syntax or unsupported method.</p>\n    </body>\n</html>\n'
```

Send with HTTP protocol 
```
 s.get_details("GET / HTTP/1.1\r\nHost: altanai\r\n\r\n")                                                                                                                                            
```
then the output is 
```
Out[3]: 'HTTP/1.0 200 OK\r\nServer: SimpleHTTP/0.6 Python/3.7.4\r\nDate: Sat, 14 Dec 2019 07:37:27 GMT\r\nContent-type: text/html; charset=utf-8\r\nContent-Length: 694\r\n\r\n<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">\n<html>\n<head>\n<meta http-equiv="Content-Type" content="text/html; charset=utf-8">\n<title>Directory listing for /</title>\n</head>\n<body>\n<h1>Directory listing for /</h1>\n<hr>\n<ul>\n<li><a href=".git/">.git/</a></li>\n<li><a href=".idea/">.idea/</a></li>\n<li><a href="misc/">misc/</a></li>\n<li><a href="process_synchronization/">process_synchronization/</a></li>\n<li><a href="README.md">README.md</a></li>\n<li><a href="reconnaissance/">reconnaissance/</a></li>\n<li><a href="socket_dir/">socket_dir/</a></li>\n<li><a href="sorts/">sorts/</a></li>\n<li><a href="venv/">venv/</a></li>\n</ul>\n<hr>\n</body>\n</html>\n'
```
