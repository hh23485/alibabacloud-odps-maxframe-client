# Copyright 1999-2025 Alibaba Group Holding Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


def _install():
    import pandas as pd

    from ....core import CachedAccessor
    from ....utils import adapt_docstring
    from ...core import DATAFRAME_TYPE, SERIES_TYPE
    from .core import DataFramePlotAccessor, PlotAccessor, SeriesPlotAccessor

    for t in DATAFRAME_TYPE:
        t.plot = CachedAccessor("plot", DataFramePlotAccessor)
    for method in dir(pd.DataFrame.plot):
        if not method.startswith("_"):
            DataFramePlotAccessor._register(method)

    for t in SERIES_TYPE:
        t.plot = CachedAccessor("plot", SeriesPlotAccessor)
    for method in dir(pd.Series.plot):
        if not method.startswith("_"):
            SeriesPlotAccessor._register(method)

    PlotAccessor.__doc__ = adapt_docstring(pd.DataFrame.plot.__doc__)


_install()
del _install
