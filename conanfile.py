#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.69.0@bincrafters/stable")

class BoostQvmConan(base.BoostBaseConan):
    name = "boost_qvm"
    version = "1.69.0"
    url = "https://github.com/bincrafters/conan-boost_qvm"
    lib_short_names = ["qvm"]
    header_only_libs = ["qvm"]
    b2_requires = [
        "boost_assert",
        "boost_core",
        "boost_exception",
        "boost_static_assert",
        "boost_throw_exception"
    ]
