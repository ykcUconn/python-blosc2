# -*- coding: utf-8 -*-
"""
Created on Thu Sep 25 10:52:42 2025

@author: yangk
"""

import numpy as np
import blosc2

shape = (10_000, 10_000)
array = blosc2.arange(np.prod(shape), shape=shape)