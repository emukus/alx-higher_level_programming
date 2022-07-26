#!/usr/bin/python3
"""Defines lazy_matrix function."""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiplies 2 matrices using the module NumPy"""
    return np.matmul(m_a, m_b)
