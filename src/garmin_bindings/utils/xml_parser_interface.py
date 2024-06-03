from abc import ABC, abstractmethod
import typing
from lxml.etree import Element
from activity import Activity, Lap

class XmlParserInterface(ABC):

    def __init__(self, namespaces: typing.Dict[str, str]):
        super().__init__()
        self._namespaces = namespaces
        self.__validate_namespaces()

    def __validate_namespaces(self):
        if self.key_root_namespace in self._namespaces:
            if str(self.namespace).lower() == str(self._namespaces[self.key_root_namespace]).lower():
                return

        raise ValueError

    @property
    def key_root_namespace(self) -> str:
        return None

    @property
    @abstractmethod
    def namespace(self) -> str:
        return None

    @property
    @abstractmethod
    def tag_activities(self) -> str:
        return None

    @property
    @abstractmethod
    def tag_activity(self) -> str:
        return None
    
    @abstractmethod
    def parse_activity(self, element: Element) -> Activity:
        return Activity()
    
    @abstractmethod
    def parse_lap(self, element: Element) -> Lap:
        return Lap()
