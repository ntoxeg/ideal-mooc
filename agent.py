#!/usr/bin/env python
from existence import ExistenceOfSatisfaction as EOS
from existence import ExistenceVS

print("Part 1: Self-satisfaction")
existing = EOS()
for i in range(11):
    print(existing.step())

print("\nPart 2: Valence")
existVS = ExistenceVS()
for i in range(11):
    print(existVS.step())
