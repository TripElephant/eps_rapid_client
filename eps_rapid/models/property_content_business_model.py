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


class PropertyContentBusinessModel(object):
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
        'expedia_collect': 'bool',
        'property_collect': 'bool'
    }

    attribute_map = {
        'expedia_collect': 'expedia_collect',
        'property_collect': 'property_collect'
    }

    def __init__(self, expedia_collect=None, property_collect=None):  # noqa: E501
        """PropertyContentBusinessModel - a model defined in Swagger"""  # noqa: E501

        self._expedia_collect = None
        self._property_collect = None
        self.discriminator = None

        if expedia_collect is not None:
            self.expedia_collect = expedia_collect
        if property_collect is not None:
            self.property_collect = property_collect

    @property
    def expedia_collect(self):
        """Gets the expedia_collect of this PropertyContentBusinessModel.  # noqa: E501

        Whether or not a payment for this property can be taken by Expedia at the time of booking.  # noqa: E501

        :return: The expedia_collect of this PropertyContentBusinessModel.  # noqa: E501
        :rtype: bool
        """
        return self._expedia_collect

    @expedia_collect.setter
    def expedia_collect(self, expedia_collect):
        """Sets the expedia_collect of this PropertyContentBusinessModel.

        Whether or not a payment for this property can be taken by Expedia at the time of booking.  # noqa: E501

        :param expedia_collect: The expedia_collect of this PropertyContentBusinessModel.  # noqa: E501
        :type: bool
        """

        self._expedia_collect = expedia_collect

    @property
    def property_collect(self):
        """Gets the property_collect of this PropertyContentBusinessModel.  # noqa: E501

        Whether or not a payment for this property can be taken by the property upon arrival.  # noqa: E501

        :return: The property_collect of this PropertyContentBusinessModel.  # noqa: E501
        :rtype: bool
        """
        return self._property_collect

    @property_collect.setter
    def property_collect(self, property_collect):
        """Sets the property_collect of this PropertyContentBusinessModel.

        Whether or not a payment for this property can be taken by the property upon arrival.  # noqa: E501

        :param property_collect: The property_collect of this PropertyContentBusinessModel.  # noqa: E501
        :type: bool
        """

        self._property_collect = property_collect

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
        if issubclass(PropertyContentBusinessModel, dict):
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
        if not isinstance(other, PropertyContentBusinessModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
