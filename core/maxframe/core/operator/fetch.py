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

import enum

from ... import opcodes
from ...serialization.serializables import (
    FieldTypes,
    Int32Field,
    ListField,
    ReferenceField,
    StringField,
)
from .base import Operator
from .core import TileableOperatorMixin


class Fetch(Operator):
    _op_type_ = opcodes.FETCH

    source_key = StringField("source_key", default=None)


class FetchMixin(TileableOperatorMixin):
    def check_inputs(self, inputs):
        # no inputs
        if inputs and len(inputs) > 0:
            raise ValueError(f"{type(self).__name__} has no inputs")


class FetchShuffle(Operator):
    _op_type_ = opcodes.FETCH_SHUFFLE

    source_keys = ListField("source_keys", FieldTypes.string)
    n_mappers = Int32Field("n_mappers")
    n_reducers = Int32Field("n_reducers")
    shuffle_fetch_type = ReferenceField("shuffle_fetch_type")


class ShuffleFetchType(enum.Enum):
    FETCH_BY_KEY = 0
    FETCH_BY_INDEX = 1
