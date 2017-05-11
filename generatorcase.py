#! /usr/bin/env python3
# -*- coding: utf-8 -*-
generatorcase = (x*x for x in range(99))
for n in generatorcase:
    print(n)