from __future__ import annotations
import os
import typing
import lxml.etree as ElemTree

class XmlParser:

    def __init__(self):
        self._parser = None
        self._xml_file_path = None

    def parse(
        self,
        xml_file_path: os.path,
        parser: XmlParser = None,
        parsers: typing.List[XmlParser] = None
    ):       
        self.__validate_xml_file_path(xml_file_path)
        self.__parse_namespaces()
        self.__select_appropriate_parser(parser, parsers)
        self.__parse_tree()

    def __validate_xml_file_path(self, xml_file_path: os.path):
        if os.path.exists(xml_file_path) and os.path.isfile(xml_file_path):
            self._xml_file_path = xml_file_path
        else:
            raise ValueError

    def __parse_namespaces(self) -> typing.Dict[str, str]:
        return dict([
            node for _, node in ElemTree.iterparse(
                self._xml_file_path, events=['start-ns']
            )
        ])

    def __select_appropriate_parser(self, parser: XmlParser, parsers: typing.List[XmlParser]):
        if not parser and not parsers:
            raise TypeError

        if parser and parsers:
            parsers.append(parser)
        elif parser and not parsers:
            parsers = [parser]

        self._parser = None
        for parser_type in parsers:
            namespaces = self.__parse_namespaces()
            try:
                self._parser = parser_type(namespaces)
                break
            except ValueError:
                self._parser = None

        if self._parser is None:
            raise TypeError

    def __parse_tree(self):
        #xml_root = ElemTree.parse(self._xml_file_path)
        #root = self._parser.iterate_root(xml_root)
        root = ElemTree.parse(self._xml_file_path).getroot()
        activities = self.__iter_elements(root, self._parser.tag_activities)
        for e in activities:
            print(e.tag)

    def __iter_elements(self, element: ElemTree.Element, tag: str) -> typing.List[ElemTree.Element]:
        elements = []
        for e in element.iter(tag):
            elements.append(e)
        return elements
