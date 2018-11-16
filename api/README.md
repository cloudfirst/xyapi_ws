
# 1 Request
- curl request 
curl -X POST "http://192.168.56.101/api/1.0/get/data" -H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d "datafile=003.pdf"

- http request
http://HOST/api/1.0/get/data

- raw rquest
```
POST /api/1.0/get/data HTTP/1.1
Host: 192.168.56.101:80
Content-Type: application/x-www-form-urlencoded
Cache-Control: no-cache

datafile=200.pdf
```

# 2 Responses
---------------------------------
Code    Description
---------------------------------
200     successfully get the data   
{
    "results": [
        {
            "confident": 0.8,
            "filename": "200.pdf",
            "heji": "123.45",
            "ztgz": "钢筋混泥土"
        }
    ]
}

---------------------------------
Code    Description
---------------------------------
400   bad input parameter 
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>400 Bad Request</title>
<h1>Bad Request</h1>
<p>invalid file name: 003.pdf.</p>