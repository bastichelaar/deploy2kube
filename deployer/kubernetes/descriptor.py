# -*- coding: utf-8 -*-
#
# Copyright 2016 FashionTrade
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from jinja2 import *

def generate_kubernetes_descriptor(template, number, prefix):
    """
        TODO:
          - the template doesn't add anything at the moment, so get rid of it
          - build up a k8s-specific object that matches the jinja template 1-to-1
            so it doesn't need to perform any specific logic (and we can easily
            slide in the annotations).
    """
    env = Environment(
        loader = PackageLoader('metatron.kubernetes', ''),
        trim_blocks = True,
        keep_trailing_newline = True
    )

    template = env.get_template('%s.jinja2' % template)

    return template.render(customer="%s-%s" % (prefix, number))
