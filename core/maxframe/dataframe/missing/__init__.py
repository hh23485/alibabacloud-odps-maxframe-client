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

from .checkna import isna, isnull, notna, notnull
from .dropna import df_dropna, index_dropna, series_dropna
from .fillna import bfill, ffill, fillna, index_fillna
from .replace import df_replace, series_replace


def _install():
    from ..core import DATAFRAME_TYPE, INDEX_TYPE, SERIES_TYPE

    for cls in DATAFRAME_TYPE + SERIES_TYPE:
        setattr(cls, "backfill", bfill)
        setattr(cls, "bfill", bfill)
        setattr(cls, "fillna", fillna)
        setattr(cls, "ffill", ffill)
        setattr(cls, "isna", isna)
        setattr(cls, "isnull", isnull)
        setattr(cls, "notna", notna)
        setattr(cls, "notnull", notnull)
        setattr(cls, "pad", ffill)

    for cls in DATAFRAME_TYPE:
        setattr(cls, "dropna", df_dropna)
        setattr(cls, "replace", df_replace)

    for cls in SERIES_TYPE:
        setattr(cls, "dropna", series_dropna)
        setattr(cls, "replace", series_replace)

    for cls in INDEX_TYPE:
        setattr(cls, "dropna", index_dropna)
        setattr(cls, "fillna", index_fillna)
        setattr(cls, "isna", isna)
        setattr(cls, "isnull", isnull)
        setattr(cls, "notna", notna)
        setattr(cls, "notnull", notnull)


_install()
del _install
