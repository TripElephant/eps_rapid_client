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

from eps_rapid.models.value_adds import ValueAdds  # noqa: F401,E501


class RetrieveRatePromotions(object):
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
        'value_adds': 'ValueAdds'
    }

    attribute_map = {
        'value_adds': 'value_adds'
    }

    def __init__(self, value_adds=None):  # noqa: E501
        """RetrieveRatePromotions - a model defined in Swagger"""  # noqa: E501

        self._value_adds = None
        self.discriminator = None

        if value_adds is not None:
            self.value_adds = value_adds

    @property
    def value_adds(self):
        """Gets the value_adds of this RetrieveRatePromotions.  # noqa: E501


        :return: The value_adds of this RetrieveRatePromotions.  # noqa: E501
        :rtype: ValueAdds
        """
        return self._value_adds

    @value_adds.setter
    def value_adds(self, value_adds):
        """Sets the value_adds of this RetrieveRatePromotions.


        :param value_adds: The value_adds of this RetrieveRatePromotions.  # noqa: E501
        :type: ValueAdds
        """

        self._value_adds = value_adds

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
        if issubclass(RetrieveRatePromotions, dict):
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
        if not isinstance(other, RetrieveRatePromotions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
