from __future__ import annotations
import os
import typing
import lxml.etree as ElemTree

class XmlParser:

    def __init__(self):
        self._parser = None
        self._xml_root = None
        self._activities = list()

    def parse(
        self,
        xml_file_path: os.path,
        parser: XmlParser = None,
        parsers: typing.List[XmlParser] = None
    ):       
        self.__validate_xml_file_path(xml_file_path)
        self.__select_appropriate_parser(parser, parsers)
        self.__parse_tree()

    def __validate_xml_file_path(self, xml_file_path: os.path):
        if not (os.path.exists(xml_file_path) and os.path.isfile(xml_file_path)):
            raise ValueError
        
        self._xml_root = ElemTree.parse(xml_file_path).getroot()

    def __select_appropriate_parser(self, parser: XmlParser, parsers: typing.List[XmlParser]):
        if not parser and not parsers:
            raise TypeError

        if parser and parsers:
            parsers.append(parser)
        elif parser and not parsers:
            parsers = [parser]

        self._parser = None
        for parser_type in parsers:
            try:
                self._parser = parser_type(self._xml_root.nsmap)
                break
            except ValueError:
                self._parser = None

        if self._parser is None:
            raise TypeError

    def __parse_tree(self):
        for e_activities in self.__iter_elements(self._xml_root, self._parser.tag_activities):
            for e_activity in self.__iter_elements(e_activities, self._parser.tag_activity):
                activity = self._parser.parse_activity(e_activity)
                
                for e_lap in self.__iter_elements(e_activity, self._parser.tag_lap):
                    lap = self._parser.parse_lap(e_lap)
                    activity.laps.append(lap)
                
                self._activities.append(activity)

    def __iter_elements(self, element: ElemTree.Element, tag: str) -> typing.List[ElemTree.Element]:
        elements = []
        for e in element.iter(tag):
            elements.append(e)
        return elements
