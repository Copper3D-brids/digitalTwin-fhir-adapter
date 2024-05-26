from abc import ABC, abstractmethod
from typing import Optional, List
from .Element import Identifier, Meta


class AbstractResource(ABC):
    def __init__(self, meta: Optional[Meta] = None, identifier: Optional[List[Identifier]] = None):
        self.meta = meta
        self.identifier = identifier

    @abstractmethod
    def get(self):
        pass

    @abstractmethod
    def transfer(self):
        pass
