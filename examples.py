# -*- coding: utf-8 -*-
from ckan_sdk import (Packages,
                      Groups,
                      Tags,
                      Resource)

import pprint


s = Packages()
pprint.pprint(s.get())
pprint.pprint(s.help)
pprint.pprint(s.resp)

# search
pprint.pprint(s.search(q='spending'))
pprint.pprint(s.help)

s = Groups()
pprint.pprint(s.get())


s = Tags()
pprint.pprint(s.get())


s = Resource()
pprint.pprint(s.get(q='District Names'))

"""
Authorized requests
-------------------

Will look like, for requests that need them, eventually
"""

s = Packages(api_key='XXX')
pprint.pprint(s.get())