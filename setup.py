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

import uuid

from setuptools import setup
from pip.req import parse_requirements

try:
    install_reqs = parse_requirements("requirements.txt", session=uuid.uuid1())
except TypeError:
    install_reqs = parse_requirements("requirements.txt")


reqs = [str(ir.req) for ir in install_reqs]

extra = {}

setup(
    name='deployer',
    version='0.1',
    description='Deploys metadata-enhanced docker containers to Kubernetes, Mesos/Marathon, and more.',
    packages=[
        'deployer',
        'deployer.meta',
        'deployer.kubernetes'
    ],
    package_data={
        'deployer.kubernetes': ['*.jinja2']
    },
    entry_points={
        'console_scripts': ['deploy2kube = deployer.meta2kube:main']
    },
    include_package_data=True,
    install_requires=reqs,
    zip_safe=False,
    **extra
)
