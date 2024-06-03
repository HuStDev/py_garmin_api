from xml_parser_interface import XmlParserInterface
from lxml.etree import Element
from activity import Activity, Lap
from datetime import datetime

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
    
    @property
    def tag_lap(self) -> str:
        return '{' + str(self._namespaces[self.key_root_namespace]) + '}Lap'
    
    def parse_activity(self, element: Element) -> Activity:
        activity = Activity()
        
        activity.sport = str(element.get('Sport'))
        
        return activity
    
    def parse_lap(self, element: Element) -> Lap:
        lap = Lap()
        
        lap.start_time = datetime.strptime(element.get('StartTime'), '%Y-%m-%dT%H:%M:%S.%fZ') # 2022-06-28T05:02:22.000Z
        lap.total_time_s = element.getiterator(tag='TotalTimeSeconds').text
        lap.total_distance_m = float(element.getiterator(tag='DistanceMeters'))
        
        return lap
