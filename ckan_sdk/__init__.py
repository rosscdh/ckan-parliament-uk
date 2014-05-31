# -*- coding: utf-8 -*-
import requests


class Parla(object):
    r = requests
    base_url = 'http://demo.ckan.org/api/3/action/'
    resp = None

    @property
    def endpoint(self):
        return '%s%s' % (self.base_url, self.action)

    def get(self, **kwargs):
        self.resp = self.r.get(self.endpoint, params=kwargs)
        return self.resp.json()


class Packages(Parla):
    action = 'package_list'


class Groups(Parla):
    action = 'group_list'


class Tags(Parla):
    action = 'group_list'


class Resource(Parla):
    action = 'resource_search'
    def get(self, q, n='name' , **kwargs):
        q = '%s:%s' % (n, q)  # build search query
        return super(Resource, self).get(query=q, **kwargs)