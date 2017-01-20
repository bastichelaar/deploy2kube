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

from ..meta import *

class KubernetesMetadata(Metadata):
    """

    """
    def __init__(self, image):
        Metadata.__init__(self, image)


    # Kubernetes-specific helper methods

    def annotations(self):
        return dict(
            self.__flatten__(
                config = self.__meta__,
                key_filter = lambda k: not(k.startswith('attributes'))
            )
        )


    # Support for getting out a flattened set of filtered properties

    @staticmethod
    def __flatten__(config, prefix = None, key_filter = lambda x: True):
        def concat(prefix, suffix):
            return prefix + '.' + suffix if prefix else suffix

        list_of_results = [
            KubernetesMetadata.__flatten__(value, concat(prefix, key), key_filter)
                if isinstance(value, ConfigTree)
                else [ (concat(prefix, key), value) ]

            for key, value in config.items()
            if key_filter(key)
        ]

        return [item for result in list_of_results
                     for item in result]
