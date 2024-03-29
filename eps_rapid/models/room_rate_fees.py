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

from eps_rapid.models.room_rate_fees_mandatory_fee import RoomRateFeesMandatoryFee  # noqa: F401,E501
from eps_rapid.models.room_rate_fees_mandatory_tax import RoomRateFeesMandatoryTax  # noqa: F401,E501
from eps_rapid.models.room_rate_fees_resort_fee import RoomRateFeesResortFee  # noqa: F401,E501


class RoomRateFees(object):
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
        'mandatory_fee': 'RoomRateFeesMandatoryFee',
        'resort_fee': 'RoomRateFeesResortFee',
        'mandatory_tax': 'RoomRateFeesMandatoryTax'
    }

    attribute_map = {
        'mandatory_fee': 'mandatory_fee',
        'resort_fee': 'resort_fee',
        'mandatory_tax': 'mandatory_tax'
    }

    def __init__(self, mandatory_fee=None, resort_fee=None, mandatory_tax=None):  # noqa: E501
        """RoomRateFees - a model defined in Swagger"""  # noqa: E501

        self._mandatory_fee = None
        self._resort_fee = None
        self._mandatory_tax = None
        self.discriminator = None

        if mandatory_fee is not None:
            self.mandatory_fee = mandatory_fee
        if resort_fee is not None:
            self.resort_fee = resort_fee
        if mandatory_tax is not None:
            self.mandatory_tax = mandatory_tax

    @property
    def mandatory_fee(self):
        """Gets the mandatory_fee of this RoomRateFees.  # noqa: E501


        :return: The mandatory_fee of this RoomRateFees.  # noqa: E501
        :rtype: RoomRateFeesMandatoryFee
        """
        return self._mandatory_fee

    @mandatory_fee.setter
    def mandatory_fee(self, mandatory_fee):
        """Sets the mandatory_fee of this RoomRateFees.


        :param mandatory_fee: The mandatory_fee of this RoomRateFees.  # noqa: E501
        :type: RoomRateFeesMandatoryFee
        """

        self._mandatory_fee = mandatory_fee

    @property
    def resort_fee(self):
        """Gets the resort_fee of this RoomRateFees.  # noqa: E501


        :return: The resort_fee of this RoomRateFees.  # noqa: E501
        :rtype: RoomRateFeesResortFee
        """
        return self._resort_fee

    @resort_fee.setter
    def resort_fee(self, resort_fee):
        """Sets the resort_fee of this RoomRateFees.


        :param resort_fee: The resort_fee of this RoomRateFees.  # noqa: E501
        :type: RoomRateFeesResortFee
        """

        self._resort_fee = resort_fee

    @property
    def mandatory_tax(self):
        """Gets the mandatory_tax of this RoomRateFees.  # noqa: E501


        :return: The mandatory_tax of this RoomRateFees.  # noqa: E501
        :rtype: RoomRateFeesMandatoryTax
        """
        return self._mandatory_tax

    @mandatory_tax.setter
    def mandatory_tax(self, mandatory_tax):
        """Sets the mandatory_tax of this RoomRateFees.


        :param mandatory_tax: The mandatory_tax of this RoomRateFees.  # noqa: E501
        :type: RoomRateFeesMandatoryTax
        """

        self._mandatory_tax = mandatory_tax

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
        if issubclass(RoomRateFees, dict):
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
        if not isinstance(other, RoomRateFees):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
