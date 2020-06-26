# Copyright 2020 MONAI Consortium
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest
import numpy as np
from parameterized import parameterized

from monai.transforms import CropForegroundd

TEST_CASE_1 = [
    {
        "keys": ["img", "label"],
        "source_key": "label",
        "select_fn": lambda x: x > 0,
        "channel_indexes": None,
        "margin": 0,
    },
    {
        "img": np.array([[[1, 0, 2, 0, 1], [0, 1, 2, 1, 0], [2, 2, 3, 2, 2], [0, 1, 2, 1, 0], [1, 0, 2, 0, 1]]]),
        "label": np.array([[[0, 0, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 0, 0]]]),
    },
    np.array([[[1, 2, 1], [2, 3, 2], [1, 2, 1]]]),
]

TEST_CASE_2 = [
    {"keys": ["img"], "source_key": "img", "select_fn": lambda x: x > 1, "channel_indexes": None, "margin": 0},
    {"img": np.array([[[0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 1, 3, 1, 0], [0, 1, 1, 1, 0], [0, 0, 0, 0, 0]]])},
    np.array([[[3]]]),
]

TEST_CASE_3 = [
    {"keys": ["img"], "source_key": "img", "select_fn": lambda x: x > 0, "channel_indexes": 0, "margin": 0},
    {"img": np.array([[[0, 0, 0, 0, 0], [0, 1, 2, 1, 0], [0, 2, 3, 2, 0], [0, 1, 2, 1, 0], [0, 0, 0, 0, 0]]])},
    np.array([[[1, 2, 1], [2, 3, 2], [1, 2, 1]]]),
]

TEST_CASE_4 = [
    {"keys": ["img"], "source_key": "img", "select_fn": lambda x: x > 0, "channel_indexes": None, "margin": 1},
    {"img": np.array([[[0, 0, 0, 0, 0], [0, 1, 2, 1, 0], [0, 2, 3, 2, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]])},
    np.array([[[0, 0, 0, 0, 0], [0, 1, 2, 1, 0], [0, 2, 3, 2, 0], [0, 0, 0, 0, 0]]]),
]


class TestCropForegroundd(unittest.TestCase):
    @parameterized.expand([TEST_CASE_1, TEST_CASE_2, TEST_CASE_3, TEST_CASE_4])
    def test_value(self, argments, image, expected_data):
        result = CropForegroundd(**argments)(image)
        np.testing.assert_allclose(result["img"], expected_data)


if __name__ == "__main__":
    unittest.main()
