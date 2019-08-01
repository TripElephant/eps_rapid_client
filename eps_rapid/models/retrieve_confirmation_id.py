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


class RetrieveConfirmationId(object):
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
        'expedia': 'str',
        '_property': 'str'
    }

    attribute_map = {
        'expedia': 'expedia',
        '_property': 'property'
    }

    def __init__(self, expedia=None, _property=None):  # noqa: E501
        """RetrieveConfirmationId - a model defined in Swagger"""  # noqa: E501

        self._expedia = None
        self.__property = None
        self.discriminator = None

        if expedia is not None:
            self.expedia = expedia
        if _property is not None:
            self._property = _property

    @property
    def expedia(self):
        """Gets the expedia of this RetrieveConfirmationId.  # noqa: E501

        The expedia confirmation id.  # noqa: E501

        :return: The expedia of this RetrieveConfirmationId.  # noqa: E501
        :rtype: str
        """
        return self._expedia

    @expedia.setter
    def expedia(self, expedia):
        """Sets the expedia of this RetrieveConfirmationId.

        The expedia confirmation id.  # noqa: E501

        :param expedia: The expedia of this RetrieveConfirmationId.  # noqa: E501
        :type: str
        """

        self._expedia = expedia

    @property
    def _property(self):
        """Gets the _property of this RetrieveConfirmationId.  # noqa: E501

        The property confirmation id.  # noqa: E501

        :return: The _property of this RetrieveConfirmationId.  # noqa: E501
        :rtype: str
        """
        return self.__property

    @_property.setter
    def _property(self, _property):
        """Sets the _property of this RetrieveConfirmationId.

        The property confirmation id.  # noqa: E501

        :param _property: The _property of this RetrieveConfirmationId.  # noqa: E501
        :type: str
        """

        self.__property = _property

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
        if issubclass(RetrieveConfirmationId, dict):
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
        if not isinstance(other, RetrieveConfirmationId):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
