#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_dbrocker
----------------------------------

Tests for `dbrocker` module.
"""

import pytest

from dbrocker import dbrocker


def test_if_env_DBROCKER_CONNSTRING_is_not_set_it_should_error():
    with pytest.raises(RuntimeError):
        dbrocker.execute('SELECT * FROM wherever')
