#!/usr/bin/env python
from existence import ExistenceOfSatisfaction as EOS

existing = EOS()
for i in range(11):
    print(existing.step())
