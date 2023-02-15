"""Правило: если post - тогда есть body, если get, то тогда появляетя queryStringParam"""

# 1) GET https://hbihj92uvc.execute-api.ca-central-1.amazonaws.com/getPerson?first_name=Tol&last_name=Varv&age=11&source=postman&method=get_passing_params_via_url
passed_params_via_postman_get_url = {
   "version":"2.0",
   "routeKey":"GET /getPerson",
   "rawPath":"/getPerson",
   "rawQueryString":"first_name=Tol&last_name=Varv&age=11&source=postman&method=get_passing_params_via_url",
   "headers":{
      "accept":"*/*",
      "accept-encoding":"gzip, deflate, br",
      "cache-control":"no-cache",
      "content-length":"0",
      "host":"hbihj92uvc.execute-api.ca-central-1.amazonaws.com",
      "postman-token":"eb9eb9a4-de60-4f39-a490-164bf847ba8b",
      "user-agent":"PostmanRuntime/7.30.0",
      "x-amzn-trace-id":"Root=1-63ecb814-6f00ba705906dae30115b523",
      "x-forwarded-for":"176.97.63.100",
      "x-forwarded-port":"443",
      "x-forwarded-proto":"https"
   },
   "queryStringParameters":{
      "age":"11",
      "first_name":"Tol",
      "last_name":"Varv",
      "method":"get_passing_params_via_url",
      "source":"postman"
   },
   "requestContext":{
      "accountId":"140294923654",
      "apiId":"hbihj92uvc",
      "domainName":"hbihj92uvc.execute-api.ca-central-1.amazonaws.com",
      "domainPrefix":"hbihj92uvc",
      "http":{
         "method":"GET",
         "path":"/getPerson",
         "protocol":"HTTP/1.1",
         "sourceIp":"176.97.63.100",
         "userAgent":"PostmanRuntime/7.30.0"
      },
      "requestId":"AYGzPgLq4osEJxQ=",
      "routeKey":"GET /getPerson",
      "stage":"$default",
      "time":"15/Feb/2023:10:46:44 +0000",
      "timeEpoch":1676458004458
   },
   "isBase64Encoded":false
}

# 2) POST https://hbihj92uvc.execute-api.ca-central-1.amazonaws.com/createPerson
# body txt {
#     "first_name": "Nickolay",
#     "last_name": "Varvonets",
#     "age": 27,
#     "source": "postman",
#     "method": "post with text body"
# }
passed_params_via_postman_post_txt_body = {
   "version":"2.0",
   "routeKey":"POST /createPerson",
   "rawPath":"/createPerson",
   "rawQueryString":"",
   "headers":{
      "accept":"*/*",
      "accept-encoding":"gzip, deflate, br",
      "cache-control":"no-cache",
      "content-length":"138",
      "content-type":"text/plain",
      "host":"hbihj92uvc.execute-api.ca-central-1.amazonaws.com",
      "postman-token":"578f3e20-9406-4677-9f96-54ba51e9ffa2",
      "user-agent":"PostmanRuntime/7.30.0",
      "x-amzn-trace-id":"Root=1-63ecb822-2c373243552c02e30df49011",
      "x-forwarded-for":"176.97.63.100",
      "x-forwarded-port":"443",
      "x-forwarded-proto":"https"
   },
   "requestContext":{
      "accountId":"140294923654",
      "apiId":"hbihj92uvc",
      "domainName":"hbihj92uvc.execute-api.ca-central-1.amazonaws.com",
      "domainPrefix":"hbihj92uvc",
      "http":{
         "method":"POST",
         "path":"/createPerson",
         "protocol":"HTTP/1.1",
         "sourceIp":"176.97.63.100",
         "userAgent":"PostmanRuntime/7.30.0"
      },
      "requestId":"AYG1XiRY4osEJrw=",
      "routeKey":"POST /createPerson",
      "stage":"$default",
      "time":"15/Feb/2023:10:46:58 +0000",
      "timeEpoch":1676458018033
   },
   "body":"{\n    \"first_name\": \"Nickolay\",\n    \"last_name\": \"Varvonets\",\n    \"age\": 27,\n    \"source\": \"postman\"\n    \"method\": \"post with text body\"\n}",
   "isBase64Encoded":false
}
