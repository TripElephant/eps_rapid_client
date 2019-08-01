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


class BedGroupConfiguration(object):
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
        'type': 'str',
        'size': 'str',
        'quantity': 'float'
    }

    attribute_map = {
        'type': 'type',
        'size': 'size',
        'quantity': 'quantity'
    }

    def __init__(self, type=None, size=None, quantity=None):  # noqa: E501
        """BedGroupConfiguration - a model defined in Swagger"""  # noqa: E501

        self._type = None
        self._size = None
        self._quantity = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if size is not None:
            self.size = size
        if quantity is not None:
            self.quantity = quantity

    @property
    def type(self):
        """Gets the type of this BedGroupConfiguration.  # noqa: E501

        The type of this bed configuration in the room.  # noqa: E501

        :return: The type of this BedGroupConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BedGroupConfiguration.

        The type of this bed configuration in the room.  # noqa: E501

        :param type: The type of this BedGroupConfiguration.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def size(self):
        """Gets the size of this BedGroupConfiguration.  # noqa: E501

        The size of this bed configuration in the room.  # noqa: E501

        :return: The size of this BedGroupConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this BedGroupConfiguration.

        The size of this bed configuration in the room.  # noqa: E501

        :param size: The size of this BedGroupConfiguration.  # noqa: E501
        :type: str
        """

        self._size = size

    @property
    def quantity(self):
        """Gets the quantity of this BedGroupConfiguration.  # noqa: E501

        The number of this bed configuration in the room.  # noqa: E501

        :return: The quantity of this BedGroupConfiguration.  # noqa: E501
        :rtype: float
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this BedGroupConfiguration.

        The number of this bed configuration in the room.  # noqa: E501

        :param quantity: The quantity of this BedGroupConfiguration.  # noqa: E501
        :type: float
        """

        self._quantity = quantity

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
        if issubclass(BedGroupConfiguration, dict):
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
        if not isinstance(other, BedGroupConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other