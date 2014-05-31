CKAN-PARLIAMENT-UK
==================

sdk for http://docs.ckan.org/en/ckan-2.1/api.html

A basic sdk for working with the UK parliamentary api: http://www.data.parliament.uk/dataset/01

Uses the amazing [Requests Library](http://docs.python-requests.org/en/latest/)


Install
-------

1. pip install -r requirements.txt


Demos
-----

1. have a look at examples.py

```
service = Packages()
service.get()  # perform the GET (returns the full json response)
service.help  # View the requests HELP (if present)
service.results  # shortcut to just the results iteratable (list)

service.resp  # the full response as per Requests Library: http://docs.python-requests.org/en/latest/
service.resp_status  # response status (200, 401...)
service.resp_headers  # the responses headers
service.resp_json  # the responses full json object
```

Authentication
==============

```
service = Packages(api_key='XXX')
```


ToDo
----

1. tests
2. more examples
3. better documentation of the resources
4. contact me for more