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

from eps_rapid.models.brand import Brand  # noqa: F401,E501


class Chain(object):
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
        'id': 'float',
        'name': 'str',
        'brands': 'dict(str, Brand)'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'brands': 'brands'
    }

    def __init__(self, id=None, name=None, brands=None):  # noqa: E501
        """Chain - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._brands = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if brands is not None:
            self.brands = brands

    @property
    def id(self):
        """Gets the id of this Chain.  # noqa: E501

        Chain id.  # noqa: E501

        :return: The id of this Chain.  # noqa: E501
        :rtype: float
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Chain.

        Chain id.  # noqa: E501

        :param id: The id of this Chain.  # noqa: E501
        :type: float
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Chain.  # noqa: E501

        Chain name.  # noqa: E501

        :return: The name of this Chain.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Chain.

        Chain name.  # noqa: E501

        :param name: The name of this Chain.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def brands(self):
        """Gets the brands of this Chain.  # noqa: E501

        Map of the chain's brands.  # noqa: E501

        :return: The brands of this Chain.  # noqa: E501
        :rtype: dict(str, Brand)
        """
        return self._brands

    @brands.setter
    def brands(self, brands):
        """Sets the brands of this Chain.

        Map of the chain's brands.  # noqa: E501

        :param brands: The brands of this Chain.  # noqa: E501
        :type: dict(str, Brand)
        """

        self._brands = brands

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
        if issubclass(Chain, dict):
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
        if not isinstance(other, Chain):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
