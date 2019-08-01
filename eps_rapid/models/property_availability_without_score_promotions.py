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

from eps_rapid.models.property_availability_without_score_promotions_deal import PropertyAvailabilityWithoutScorePromotionsDeal  # noqa: F401,E501
from eps_rapid.models.value_add import ValueAdd  # noqa: F401,E501


class PropertyAvailabilityWithoutScorePromotions(object):
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
        'value_adds': 'dict(str, ValueAdd)',
        'deal': 'PropertyAvailabilityWithoutScorePromotionsDeal'
    }

    attribute_map = {
        'value_adds': 'value_adds',
        'deal': 'deal'
    }

    def __init__(self, value_adds=None, deal=None):  # noqa: E501
        """PropertyAvailabilityWithoutScorePromotions - a model defined in Swagger"""  # noqa: E501

        self._value_adds = None
        self._deal = None
        self.discriminator = None

        if value_adds is not None:
            self.value_adds = value_adds
        if deal is not None:
            self.deal = deal

    @property
    def value_adds(self):
        """Gets the value_adds of this PropertyAvailabilityWithoutScorePromotions.  # noqa: E501

        A collection of value adds that apply to this rate.  # noqa: E501

        :return: The value_adds of this PropertyAvailabilityWithoutScorePromotions.  # noqa: E501
        :rtype: dict(str, ValueAdd)
        """
        return self._value_adds

    @value_adds.setter
    def value_adds(self, value_adds):
        """Sets the value_adds of this PropertyAvailabilityWithoutScorePromotions.

        A collection of value adds that apply to this rate.  # noqa: E501

        :param value_adds: The value_adds of this PropertyAvailabilityWithoutScorePromotions.  # noqa: E501
        :type: dict(str, ValueAdd)
        """

        self._value_adds = value_adds

    @property
    def deal(self):
        """Gets the deal of this PropertyAvailabilityWithoutScorePromotions.  # noqa: E501


        :return: The deal of this PropertyAvailabilityWithoutScorePromotions.  # noqa: E501
        :rtype: PropertyAvailabilityWithoutScorePromotionsDeal
        """
        return self._deal

    @deal.setter
    def deal(self, deal):
        """Sets the deal of this PropertyAvailabilityWithoutScorePromotions.


        :param deal: The deal of this PropertyAvailabilityWithoutScorePromotions.  # noqa: E501
        :type: PropertyAvailabilityWithoutScorePromotionsDeal
        """

        self._deal = deal

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
        if issubclass(PropertyAvailabilityWithoutScorePromotions, dict):
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
        if not isinstance(other, PropertyAvailabilityWithoutScorePromotions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other