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

from eps_rapid.models.room_rate_totals_inclusive_billable_currency import RoomRateTotalsInclusiveBillableCurrency  # noqa: F401,E501
from eps_rapid.models.room_rate_totals_inclusive_request_currency import RoomRateTotalsInclusiveRequestCurrency  # noqa: F401,E501


class RoomRateTotalsMarketingFee(object):
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
        'billable_currency': 'RoomRateTotalsInclusiveBillableCurrency',
        'request_currency': 'RoomRateTotalsInclusiveRequestCurrency'
    }

    attribute_map = {
        'billable_currency': 'billable_currency',
        'request_currency': 'request_currency'
    }

    def __init__(self, billable_currency=None, request_currency=None):  # noqa: E501
        """RoomRateTotalsMarketingFee - a model defined in Swagger"""  # noqa: E501

        self._billable_currency = None
        self._request_currency = None
        self.discriminator = None

        if billable_currency is not None:
            self.billable_currency = billable_currency
        if request_currency is not None:
            self.request_currency = request_currency

    @property
    def billable_currency(self):
        """Gets the billable_currency of this RoomRateTotalsMarketingFee.  # noqa: E501


        :return: The billable_currency of this RoomRateTotalsMarketingFee.  # noqa: E501
        :rtype: RoomRateTotalsInclusiveBillableCurrency
        """
        return self._billable_currency

    @billable_currency.setter
    def billable_currency(self, billable_currency):
        """Sets the billable_currency of this RoomRateTotalsMarketingFee.


        :param billable_currency: The billable_currency of this RoomRateTotalsMarketingFee.  # noqa: E501
        :type: RoomRateTotalsInclusiveBillableCurrency
        """

        self._billable_currency = billable_currency

    @property
    def request_currency(self):
        """Gets the request_currency of this RoomRateTotalsMarketingFee.  # noqa: E501


        :return: The request_currency of this RoomRateTotalsMarketingFee.  # noqa: E501
        :rtype: RoomRateTotalsInclusiveRequestCurrency
        """
        return self._request_currency

    @request_currency.setter
    def request_currency(self, request_currency):
        """Sets the request_currency of this RoomRateTotalsMarketingFee.


        :param request_currency: The request_currency of this RoomRateTotalsMarketingFee.  # noqa: E501
        :type: RoomRateTotalsInclusiveRequestCurrency
        """

        self._request_currency = request_currency

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
        if issubclass(RoomRateTotalsMarketingFee, dict):
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
        if not isinstance(other, RoomRateTotalsMarketingFee):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other