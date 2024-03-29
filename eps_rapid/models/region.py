# coding: utf-8

"""
    Rapid

    EPS Rapid V2.3  # noqa: E501

    OpenAPI spec version: 2.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from eps_rapid.models.region_ancestors import RegionAncestors  # noqa: F401,E501
from eps_rapid.models.region_coordinates import RegionCoordinates  # noqa: F401,E501


class Region(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'type': 'str',
        'name': 'str',
        'name_full': 'str',
        'descriptor': 'str',
        'country_code': 'str',
        'coordinates': 'RegionCoordinates',
        'ancestors': 'list[RegionAncestors]',
        'descendants': 'dict(str, list[str])',
        'property_ids': 'list[str]',
        'property_ids_expanded': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'name': 'name',
        'name_full': 'name_full',
        'descriptor': 'descriptor',
        'country_code': 'country_code',
        'coordinates': 'coordinates',
        'ancestors': 'ancestors',
        'descendants': 'descendants',
        'property_ids': 'property_ids',
        'property_ids_expanded': 'property_ids_expanded'
    }

    def __init__(self, id=None, type=None, name=None, name_full=None, descriptor=None, country_code=None, coordinates=None, ancestors=None, descendants=None, property_ids=None, property_ids_expanded=None):  # noqa: E501
        """Region - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._type = None
        self._name = None
        self._name_full = None
        self._descriptor = None
        self._country_code = None
        self._coordinates = None
        self._ancestors = None
        self._descendants = None
        self._property_ids = None
        self._property_ids_expanded = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if name is not None:
            self.name = name
        if name_full is not None:
            self.name_full = name_full
        if descriptor is not None:
            self.descriptor = descriptor
        if country_code is not None:
            self.country_code = country_code
        if coordinates is not None:
            self.coordinates = coordinates
        if ancestors is not None:
            self.ancestors = ancestors
        if descendants is not None:
            self.descendants = descendants
        if property_ids is not None:
            self.property_ids = property_ids
        if property_ids_expanded is not None:
            self.property_ids_expanded = property_ids_expanded

    @property
    def id(self):
        """Gets the id of this Region.  # noqa: E501

        Region Id.  # noqa: E501

        :return: The id of this Region.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Region.

        Region Id.  # noqa: E501

        :param id: The id of this Region.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this Region.  # noqa: E501

        Region type.  # noqa: E501

        :return: The type of this Region.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Region.

        Region type.  # noqa: E501

        :param type: The type of this Region.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def name(self):
        """Gets the name of this Region.  # noqa: E501

        Region name.  # noqa: E501

        :return: The name of this Region.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Region.

        Region name.  # noqa: E501

        :param name: The name of this Region.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def name_full(self):
        """Gets the name_full of this Region.  # noqa: E501

        Full region name.  # noqa: E501

        :return: The name_full of this Region.  # noqa: E501
        :rtype: str
        """
        return self._name_full

    @name_full.setter
    def name_full(self, name_full):
        """Sets the name_full of this Region.

        Full region name.  # noqa: E501

        :param name_full: The name_full of this Region.  # noqa: E501
        :type: str
        """

        self._name_full = name_full

    @property
    def descriptor(self):
        """Gets the descriptor of this Region.  # noqa: E501

        Specific information about the region e.g. whether it covers surrounding areas for a city. Only present when relevant for a region. See our [region descriptors reference](https://developer.expediapartnersolutions.com/reference/geography-reference-lists-2-2/) for current known descriptor values.  # noqa: E501

        :return: The descriptor of this Region.  # noqa: E501
        :rtype: str
        """
        return self._descriptor

    @descriptor.setter
    def descriptor(self, descriptor):
        """Sets the descriptor of this Region.

        Specific information about the region e.g. whether it covers surrounding areas for a city. Only present when relevant for a region. See our [region descriptors reference](https://developer.expediapartnersolutions.com/reference/geography-reference-lists-2-2/) for current known descriptor values.  # noqa: E501

        :param descriptor: The descriptor of this Region.  # noqa: E501
        :type: str
        """

        self._descriptor = descriptor

    @property
    def country_code(self):
        """Gets the country_code of this Region.  # noqa: E501

        Region country code (ISO-3166 ALPHA-2).  # noqa: E501

        :return: The country_code of this Region.  # noqa: E501
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this Region.

        Region country code (ISO-3166 ALPHA-2).  # noqa: E501

        :param country_code: The country_code of this Region.  # noqa: E501
        :type: str
        """

        self._country_code = country_code

    @property
    def coordinates(self):
        """Gets the coordinates of this Region.  # noqa: E501


        :return: The coordinates of this Region.  # noqa: E501
        :rtype: RegionCoordinates
        """
        return self._coordinates

    @coordinates.setter
    def coordinates(self, coordinates):
        """Sets the coordinates of this Region.


        :param coordinates: The coordinates of this Region.  # noqa: E501
        :type: RegionCoordinates
        """

        self._coordinates = coordinates

    @property
    def ancestors(self):
        """Gets the ancestors of this Region.  # noqa: E501

        An array of the region's ancestors.  # noqa: E501

        :return: The ancestors of this Region.  # noqa: E501
        :rtype: list[RegionAncestors]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """Sets the ancestors of this Region.

        An array of the region's ancestors.  # noqa: E501

        :param ancestors: The ancestors of this Region.  # noqa: E501
        :type: list[RegionAncestors]
        """

        self._ancestors = ancestors

    @property
    def descendants(self):
        """Gets the descendants of this Region.  # noqa: E501

        A map of the region types that contain direct descendants of the region.  # noqa: E501

        :return: The descendants of this Region.  # noqa: E501
        :rtype: dict(str, list[str])
        """
        return self._descendants

    @descendants.setter
    def descendants(self, descendants):
        """Sets the descendants of this Region.

        A map of the region types that contain direct descendants of the region.  # noqa: E501

        :param descendants: The descendants of this Region.  # noqa: E501
        :type: dict(str, list[str])
        """

        self._descendants = descendants

    @property
    def property_ids(self):
        """Gets the property_ids of this Region.  # noqa: E501

        An array of associated property ids for the region.  # noqa: E501

        :return: The property_ids of this Region.  # noqa: E501
        :rtype: list[str]
        """
        return self._property_ids

    @property_ids.setter
    def property_ids(self, property_ids):
        """Sets the property_ids of this Region.

        An array of associated property ids for the region.  # noqa: E501

        :param property_ids: The property_ids of this Region.  # noqa: E501
        :type: list[str]
        """

        self._property_ids = property_ids

    @property
    def property_ids_expanded(self):
        """Gets the property_ids_expanded of this Region.  # noqa: E501

        An array of associated property ids within an expanded radius for the region.  # noqa: E501

        :return: The property_ids_expanded of this Region.  # noqa: E501
        :rtype: list[str]
        """
        return self._property_ids_expanded

    @property_ids_expanded.setter
    def property_ids_expanded(self, property_ids_expanded):
        """Sets the property_ids_expanded of this Region.

        An array of associated property ids within an expanded radius for the region.  # noqa: E501

        :param property_ids_expanded: The property_ids_expanded of this Region.  # noqa: E501
        :type: list[str]
        """

        self._property_ids_expanded = property_ids_expanded

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Region, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Region):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
