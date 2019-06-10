#!/usr/bin/env python

# Copyright 2018 D-Wave Systems Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import print_function

import sys

import dimod
from hybrid.reference.kerberos import KerberosSampler

problem = sys.argv[1]
with open(problem) as fp:
    bqm = dimod.BinaryQuadraticModel.from_coo(fp)

energy_threshold = None
if len(sys.argv) > 2:
    energy_threshold = float(sys.argv[2])

solution = KerberosSampler().sample(bqm, max_iter=10, convergence=3,
                                    energy_threshold=energy_threshold)

print("Solution: {!r}".format(solution.record))
