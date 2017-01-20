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

import re

from pyhocon import *
from .docker import dockerInspect

class Metadata(object):
    """
    Class the wraps a pyhocon ConfigTree instance with some extra behavior
    for creating instances for a specific docker image and adding a small
    number of extra metadata attributes, like:

    - meta.attributes.image
    - meta.attributes.project
    - meta.attributes.version
    - meta.attributes.registry (optional)
    """
    def __init__(self, image):
        def __image_attributes__(image):
            pattern = re.compile('(?:(.+)/)?(.+):(.+)')
            matched = pattern.match(image)

            # TODO: raise an error if matched is None

            return matched.groups()

        def __parse__(image):
            # Inspect the metadata embedded in the specified image
            inspected = dockerInspect(image)
            data = ConfigFactory.parse_string(inspected)

            # Add some extra metadata based on the specified image name and version
            registry, project, version = __image_attributes__(image)
            data.put('meta.project.name', project)
            data.put('meta.project.version', version)
            data.put('meta.container.image', image)

            return data

        self.__meta__ = __parse__(image)


    # Add some ConfigTree/dict-like passthrough methods

    def items(self):
        return self.__meta__.items()

    def iterkeys(self):
        return self.__meta__.iterkeys()

    def __getitem__(self, key):
        return self.__meta__[key]
