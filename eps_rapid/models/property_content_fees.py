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


class PropertyContentFees(object):
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
        'mandatory': 'str',
        'optional': 'str'
    }

    attribute_map = {
        'mandatory': 'mandatory',
        'optional': 'optional'
    }

    def __init__(self, mandatory=None, optional=None):  # noqa: E501
        """PropertyContentFees - a model defined in Swagger"""  # noqa: E501

        self._mandatory = None
        self._optional = None
        self.discriminator = None

        if mandatory is not None:
            self.mandatory = mandatory
        if optional is not None:
            self.optional = optional

    @property
    def mandatory(self):
        """Gets the mandatory of this PropertyContentFees.  # noqa: E501

        Describes resort fees and other mandatory taxes or charges. May describe which services are covered by any fees, such as fitness centers or internet access.  # noqa: E501

        :return: The mandatory of this PropertyContentFees.  # noqa: E501
        :rtype: str
        """
        return self._mandatory

    @mandatory.setter
    def mandatory(self, mandatory):
        """Sets the mandatory of this PropertyContentFees.

        Describes resort fees and other mandatory taxes or charges. May describe which services are covered by any fees, such as fitness centers or internet access.  # noqa: E501

        :param mandatory: The mandatory of this PropertyContentFees.  # noqa: E501
        :type: str
        """

        self._mandatory = mandatory

    @property
    def optional(self):
        """Gets the optional of this PropertyContentFees.  # noqa: E501

        Describes additional optional fees for items such as breakfast, wifi, parking, pets etc.  # noqa: E501

        :return: The optional of this PropertyContentFees.  # noqa: E501
        :rtype: str
        """
        return self._optional

    @optional.setter
    def optional(self, optional):
        """Sets the optional of this PropertyContentFees.

        Describes additional optional fees for items such as breakfast, wifi, parking, pets etc.  # noqa: E501

        :param optional: The optional of this PropertyContentFees.  # noqa: E501
        :type: str
        """

        self._optional = optional

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
        if issubclass(PropertyContentFees, dict):
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
        if not isinstance(other, PropertyContentFees):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
