# -*- coding: utf-8 -*-
import requests


class Parla(object):
    r = requests
    api_key = None
    version = 3
    base_url = 'http://demo.ckan.org/api/{version}/action/'
    resp = None  # response from server
    resp_status = None # shortcut to response.status_code
    resp_headers = None # shortcut to response.status_code

    def __init__(self, api_key=None, *args, **kwargs):
        self.api_key = api_key
        self.resp = None
        self.resp_status = None
        self.resp_headers = None
        self.version = kwargs.get('version', self.version)

    @property
    def headers(self):
        """
        Allow custom authorisation header to be passed in
        """
        return {'authorization': self.api_key} if self.api_key is not None else None

    @property
    def endpoint(self):
        base_url = self.base_url.format(version=self.version)  # allow user to override the version
        return '%s%s' % (base_url, self.action)

    def response(self, resp):
        self.resp = resp
        self.resp_status = resp.status_code
        self.resp_headers = resp.headers
        return resp

    def get(self, **kwargs):
        self.response(self.r.get(self.endpoint, params=kwargs, headers=self.headers))
        return self.resp.json()


class Packages(Parla):
    action = 'package_list'

    def __init__(self, *args, **kwargs):
        self.action = 'package_list'  # reset

    def search(self, q, **kwargs):
        self.action = 'package_search'
        return super(Packages, self).get(q=q, **kwargs)


class Groups(Parla):
    action = 'group_list'


class Tags(Parla):
    action = 'group_list'


class Resource(Parla):
    action = 'resource_search'
    def get(self, q, n='name' , **kwargs):
        q = '%s:%s' % (n, q)  # build search query
        return super(Resource, self).get(query=q, **kwargs)
