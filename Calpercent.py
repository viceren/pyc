#! /usr/bin/env python3
# -*- coding: utf-8 -*-

UsageLastYear = float(input('Please input last year usage:'))
UsageThisYear = float(input('Please input this year usage:'))
ImprovePercent = ((UsageThisYear - UsageLastYear) / UsageLastYear) * 100
print ('The improvement percent is: %.5f%%' % ImprovePercent)