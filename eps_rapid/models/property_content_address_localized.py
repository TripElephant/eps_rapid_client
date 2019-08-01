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


class PropertyContentAddressLocalized(object):
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
        'links': 'dict(str, Link)'
    }

    attribute_map = {
        'links': 'links'
    }

    def __init__(self, links=None):  # noqa: E501
        """PropertyContentAddressLocalized - a model defined in Swagger"""  # noqa: E501

        self._links = None
        self.discriminator = None

        if links is not None:
            self.links = links

    @property
    def links(self):
        """Gets the links of this PropertyContentAddressLocalized.  # noqa: E501

        Keyed by the language, a map of links to the property’s localized address(es) based on the primary language(s) spoken in the property’s country. Only languages supported by the Rapid API are provided.  # noqa: E501

        :return: The links of this PropertyContentAddressLocalized.  # noqa: E501
        :rtype: dict(str, Link)
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this PropertyContentAddressLocalized.

        Keyed by the language, a map of links to the property’s localized address(es) based on the primary language(s) spoken in the property’s country. Only languages supported by the Rapid API are provided.  # noqa: E501

        :param links: The links of this PropertyContentAddressLocalized.  # noqa: E501
        :type: dict(str, Link)
        """

        self._links = links

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
        if issubclass(PropertyContentAddressLocalized, dict):
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
        if not isinstance(other, PropertyContentAddressLocalized):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
