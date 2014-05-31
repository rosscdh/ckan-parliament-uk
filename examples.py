# -*- coding: utf-8 -*-
from ckan_sdk import (Packages,
                      Groups,
                      Tags,
                      Resource)

import pprint


s = Packages()
pprint.pprint(s.get())


s = Groups()
pprint.pprint(s.get())


s = Tags()
pprint.pprint(s.get())


s = Resource()
pprint.pprint(s.get(q='District Names'))