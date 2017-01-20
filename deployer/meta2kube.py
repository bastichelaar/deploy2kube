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
import os
import click
import shutil
import tempfile

from subprocess import call
from deployer.kubernetes import *

@click.command()
@click.option('--amount', '-a', default=1, help="Amount of customers to generate")
@click.option('--prefix', '-p', default="customer", help="Prefix used for naming")
def meta2kube(amount, prefix):
    """
    Generate and deploy Kubernetes deployment descriptors
    """
    dirpath = tempfile.mkdtemp()
    for x in range(amount):
        with click.open_file("%s/%s.yml" % (dirpath, x), 'w') as f:
            f.write(generate_kubernetes_descriptor('kubernetes', x, prefix))

    call(['kubectl', 'apply', '-f', dirpath])
    shutil.rmtree(dirpath)

def main():
    meta2kube()

if __name__ == '__main__':
    main()
