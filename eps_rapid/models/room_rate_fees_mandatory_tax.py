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


class RoomRateFeesMandatoryTax(object):
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
        'request_currency': 'RoomRateTotalsInclusiveRequestCurrency',
        'scope': 'str',
        'frequency': 'str'
    }

    attribute_map = {
        'billable_currency': 'billable_currency',
        'request_currency': 'request_currency',
        'scope': 'scope',
        'frequency': 'frequency'
    }

    def __init__(self, billable_currency=None, request_currency=None, scope=None, frequency=None):  # noqa: E501
        """RoomRateFeesMandatoryTax - a model defined in Swagger"""  # noqa: E501

        self._billable_currency = None
        self._request_currency = None
        self._scope = None
        self._frequency = None
        self.discriminator = None

        if billable_currency is not None:
            self.billable_currency = billable_currency
        if request_currency is not None:
            self.request_currency = request_currency
        if scope is not None:
            self.scope = scope
        if frequency is not None:
            self.frequency = frequency

    @property
    def billable_currency(self):
        """Gets the billable_currency of this RoomRateFeesMandatoryTax.  # noqa: E501


        :return: The billable_currency of this RoomRateFeesMandatoryTax.  # noqa: E501
        :rtype: RoomRateTotalsInclusiveBillableCurrency
        """
        return self._billable_currency

    @billable_currency.setter
    def billable_currency(self, billable_currency):
        """Sets the billable_currency of this RoomRateFeesMandatoryTax.


        :param billable_currency: The billable_currency of this RoomRateFeesMandatoryTax.  # noqa: E501
        :type: RoomRateTotalsInclusiveBillableCurrency
        """

        self._billable_currency = billable_currency

    @property
    def request_currency(self):
        """Gets the request_currency of this RoomRateFeesMandatoryTax.  # noqa: E501


        :return: The request_currency of this RoomRateFeesMandatoryTax.  # noqa: E501
        :rtype: RoomRateTotalsInclusiveRequestCurrency
        """
        return self._request_currency

    @request_currency.setter
    def request_currency(self, request_currency):
        """Sets the request_currency of this RoomRateFeesMandatoryTax.


        :param request_currency: The request_currency of this RoomRateFeesMandatoryTax.  # noqa: E501
        :type: RoomRateTotalsInclusiveRequestCurrency
        """

        self._request_currency = request_currency

    @property
    def scope(self):
        """Gets the scope of this RoomRateFeesMandatoryTax.  # noqa: E501

        The scope of the fee.  # noqa: E501

        :return: The scope of this RoomRateFeesMandatoryTax.  # noqa: E501
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this RoomRateFeesMandatoryTax.

        The scope of the fee.  # noqa: E501

        :param scope: The scope of this RoomRateFeesMandatoryTax.  # noqa: E501
        :type: str
        """
        allowed_values = ["unknown", "per_person", "per_room", "per_accommodation", "per_house", "per_apartment", "per_adult"]  # noqa: E501
        if scope not in allowed_values:
            raise ValueError(
                "Invalid value for `scope` ({0}), must be one of {1}"  # noqa: E501
                .format(scope, allowed_values)
            )

        self._scope = scope

    @property
    def frequency(self):
        """Gets the frequency of this RoomRateFeesMandatoryTax.  # noqa: E501

        The frequency of the fee.  # noqa: E501

        :return: The frequency of this RoomRateFeesMandatoryTax.  # noqa: E501
        :rtype: str
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        """Sets the frequency of this RoomRateFeesMandatoryTax.

        The frequency of the fee.  # noqa: E501

        :param frequency: The frequency of this RoomRateFeesMandatoryTax.  # noqa: E501
        :type: str
        """
        allowed_values = ["unknown", "per_night", "per_day", "per_stay", "per_week", "round_trip", "one_way"]  # noqa: E501
        if frequency not in allowed_values:
            raise ValueError(
                "Invalid value for `frequency` ({0}), must be one of {1}"  # noqa: E501
                .format(frequency, allowed_values)
            )

        self._frequency = frequency

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
        if issubclass(RoomRateFeesMandatoryTax, dict):
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
        if not isinstance(other, RoomRateFeesMandatoryTax):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
