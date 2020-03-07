#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from __future__ import print_function

import numpy as np

from pyspark import SparkContext
# $example on$
from pyspark.mllib.stat import Statistics
# $example off$

if __name__ == "__main__":
    sc = SparkContext(appName="CorrelationsExample")  # SparkContext

    # $example on$
    seriesX = sc.parallelize([1.0, 2.0, 3.0, 3.0, 5.0])  # a series
    # seriesY must have the same number of partitions and cardinality as seriesX
    seriesY = sc.parallelize([11.0, 22.0, 33.0, 33.0, 555.0])

    # Compute the correlation using Pearson's method. Enter "spearman" for Spearman's method.
    # If a method is not specified, Pearson's method will be used by default.
    print("Correlation is: " + str(Statistics.corr(seriesX, seriesY, method="pearson")))

    sc.stop()
