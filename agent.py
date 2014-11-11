#!/usr/bin/env python
from existence import ExistenceOfSatisfaction, ExistenceVS

print("Part 1: Self-satisfaction")
existing = ExistenceOfSatisfaction()
for i in range(11):
    print(existing.step())

print("\nPart 2: Valence")
existVS = ExistenceVS()
for j in range(11):
    print(existVS.step())
