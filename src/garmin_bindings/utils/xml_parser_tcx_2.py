from xml_parser_interface import XmlParserInterface

class XmlParserTcxV2(XmlParserInterface):

    @property
    def namespace(self) -> str:
        return 'http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2'

    @property
    def tag_activities(self) -> str:
        return '{' + str(self._namespaces[self.key_root_namespace]) + '}Activities'

    @property
    def tag_activity(self) -> str:
        return '{' + str(self._namespaces[self.key_root_namespace]) + '}Activity'
