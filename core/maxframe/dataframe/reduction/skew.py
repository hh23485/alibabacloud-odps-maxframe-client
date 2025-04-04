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

import numpy as np

from ... import opcodes
from ...core import ENTITY_TYPE, OutputType
from ...serialization.serializables import BoolField
from .core import DataFrameReductionMixin, DataFrameReductionOperator


class DataFrameSkew(DataFrameReductionOperator, DataFrameReductionMixin):
    _op_type_ = opcodes.SKEW
    _func_name = "skew"

    bias = BoolField("bias", default=None)

    @classmethod
    def get_reduction_callable(cls, op: "DataFrameSkew"):
        from .aggregation import where_function

        skipna, bias = op.skipna, op.bias

        def skew(x):
            cnt = x.count()
            mean = x.mean(skipna=skipna)
            divided = (
                (x**3).mean(skipna=skipna)
                - 3 * (x**2).mean(skipna=skipna) * mean
                + 2 * mean**3
            )
            var = x.var(skipna=skipna, ddof=0)
            if isinstance(var, ENTITY_TYPE) or var > 0:
                val = where_function(var > 0, divided / var**1.5, np.nan)
            else:
                val = np.nan
            if not bias:
                val = where_function(
                    (var > 0) & (cnt > 2),
                    val * ((cnt * (cnt - 1)) ** 0.5 / (cnt - 2)),
                    np.nan,
                )
            return val

        return skew


def skew_series(df, axis=None, skipna=True, level=None, bias=False, method=None):
    op = DataFrameSkew(
        axis=axis,
        skipna=skipna,
        level=level,
        bias=bias,
        output_types=[OutputType.scalar],
        method=method,
    )
    return op(df)


def skew_dataframe(
    df,
    axis=None,
    skipna=True,
    level=None,
    numeric_only=None,
    bias=False,
    method=None,
):
    op = DataFrameSkew(
        axis=axis,
        skipna=skipna,
        level=level,
        numeric_only=numeric_only,
        bias=bias,
        output_types=[OutputType.series],
        method=method,
    )
    return op(df)
