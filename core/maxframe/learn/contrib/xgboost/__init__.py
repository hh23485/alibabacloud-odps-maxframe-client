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

from .core import Booster
from .dmatrix import DMatrix
from .predict import predict
from .train import train

# isort: off
from ..utils import config_mod_getattr as _config_mod_getattr

_config_mod_getattr(
    {
        "XGBClassifier": ".classifier.XGBClassifier",
        "XGBRegressor": ".regressor.XGBRegressor",
    },
    globals(),
)

del _config_mod_getattr

__all__ = ["Booster", "DMatrix", "XGBClassifier", "XGBRegressor", "predict", "train"]
