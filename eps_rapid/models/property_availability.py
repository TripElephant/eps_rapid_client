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

from eps_rapid.models.link import Link  # noqa: F401,E501
from eps_rapid.models.property_availability_without_score import PropertyAvailabilityWithoutScore  # noqa: F401,E501
from eps_rapid.models.property_availability_without_score_rooms import PropertyAvailabilityWithoutScoreRooms  # noqa: F401,E501


class PropertyAvailability(object):
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
        'property_id': 'str',
        'rooms': 'list[PropertyAvailabilityWithoutScoreRooms]',
        'links': 'dict(str, Link)',
        'score': 'float'
    }

    attribute_map = {
        'property_id': 'property_id',
        'rooms': 'rooms',
        'links': 'links',
        'score': 'score'
    }

    def __init__(self, property_id=None, rooms=None, links=None, score=None):  # noqa: E501
        """PropertyAvailability - a model defined in Swagger"""  # noqa: E501

        self._property_id = None
        self._rooms = None
        self._links = None
        self._score = None
        self.discriminator = None

        self.property_id = property_id
        self.rooms = rooms
        if links is not None:
            self.links = links
        if score is not None:
            self.score = score

    @property
    def property_id(self):
        """Gets the property_id of this PropertyAvailability.  # noqa: E501

        Expedia property ID.  # noqa: E501

        :return: The property_id of this PropertyAvailability.  # noqa: E501
        :rtype: str
        """
        return self._property_id

    @property_id.setter
    def property_id(self, property_id):
        """Sets the property_id of this PropertyAvailability.

        Expedia property ID.  # noqa: E501

        :param property_id: The property_id of this PropertyAvailability.  # noqa: E501
        :type: str
        """
        if property_id is None:
            raise ValueError("Invalid value for `property_id`, must not be `None`")  # noqa: E501

        self._property_id = property_id

    @property
    def rooms(self):
        """Gets the rooms of this PropertyAvailability.  # noqa: E501

        Array of objects containing room information.  # noqa: E501

        :return: The rooms of this PropertyAvailability.  # noqa: E501
        :rtype: list[PropertyAvailabilityWithoutScoreRooms]
        """
        return self._rooms

    @rooms.setter
    def rooms(self, rooms):
        """Sets the rooms of this PropertyAvailability.

        Array of objects containing room information.  # noqa: E501

        :param rooms: The rooms of this PropertyAvailability.  # noqa: E501
        :type: list[PropertyAvailabilityWithoutScoreRooms]
        """
        if rooms is None:
            raise ValueError("Invalid value for `rooms`, must not be `None`")  # noqa: E501

        self._rooms = rooms

    @property
    def links(self):
        """Gets the links of this PropertyAvailability.  # noqa: E501

        A map of links, including links to request additional rates and recommendations.  # noqa: E501

        :return: The links of this PropertyAvailability.  # noqa: E501
        :rtype: dict(str, Link)
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this PropertyAvailability.

        A map of links, including links to request additional rates and recommendations.  # noqa: E501

        :param links: The links of this PropertyAvailability.  # noqa: E501
        :type: dict(str, Link)
        """

        self._links = links

    @property
    def score(self):
        """Gets the score of this PropertyAvailability.  # noqa: E501

        A score to sort properties where the higher the value the better. It can be used to:<br> * Sort the properties on the response<br> * Sort properties across multiple responses in parallel searches for large regions<br>  # noqa: E501

        :return: The score of this PropertyAvailability.  # noqa: E501
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this PropertyAvailability.

        A score to sort properties where the higher the value the better. It can be used to:<br> * Sort the properties on the response<br> * Sort properties across multiple responses in parallel searches for large regions<br>  # noqa: E501

        :param score: The score of this PropertyAvailability.  # noqa: E501
        :type: float
        """

        self._score = score

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
        if issubclass(PropertyAvailability, dict):
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
        if not isinstance(other, PropertyAvailability):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
