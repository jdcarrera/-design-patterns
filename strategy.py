from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

class Context_example():

    def __init__(self, strategy: strategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: strategy) -> None:
        self._strategy = strategy

    def do_some_business_logic(self) -> None:
        print("Context: Sorting data using the strategy (not sure how it'll do it)")
        result = self._strategy.do_algorithm(["a", "b", "c", "d", "e"])
        print(",".join(result))