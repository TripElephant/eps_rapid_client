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

from eps_rapid.models.room_rate_totals_exclusive import RoomRateTotalsExclusive  # noqa: F401,E501
from eps_rapid.models.room_rate_totals_gross_profit import RoomRateTotalsGrossProfit  # noqa: F401,E501
from eps_rapid.models.room_rate_totals_inclusive import RoomRateTotalsInclusive  # noqa: F401,E501
from eps_rapid.models.room_rate_totals_marketing_fee import RoomRateTotalsMarketingFee  # noqa: F401,E501
from eps_rapid.models.room_rate_totals_minimum_selling_price import RoomRateTotalsMinimumSellingPrice  # noqa: F401,E501
from eps_rapid.models.room_rate_totals_strikethrough import RoomRateTotalsStrikethrough  # noqa: F401,E501


class RoomRateTotals(object):
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
        'inclusive': 'RoomRateTotalsInclusive',
        'exclusive': 'RoomRateTotalsExclusive',
        'strikethrough': 'RoomRateTotalsStrikethrough',
        'marketing_fee': 'RoomRateTotalsMarketingFee',
        'gross_profit': 'RoomRateTotalsGrossProfit',
        'minimum_selling_price': 'RoomRateTotalsMinimumSellingPrice'
    }

    attribute_map = {
        'inclusive': 'inclusive',
        'exclusive': 'exclusive',
        'strikethrough': 'strikethrough',
        'marketing_fee': 'marketing_fee',
        'gross_profit': 'gross_profit',
        'minimum_selling_price': 'minimum_selling_price'
    }

    def __init__(self, inclusive=None, exclusive=None, strikethrough=None, marketing_fee=None, gross_profit=None, minimum_selling_price=None):  # noqa: E501
        """RoomRateTotals - a model defined in Swagger"""  # noqa: E501

        self._inclusive = None
        self._exclusive = None
        self._strikethrough = None
        self._marketing_fee = None
        self._gross_profit = None
        self._minimum_selling_price = None
        self.discriminator = None

        self.inclusive = inclusive
        self.exclusive = exclusive
        if strikethrough is not None:
            self.strikethrough = strikethrough
        if marketing_fee is not None:
            self.marketing_fee = marketing_fee
        if gross_profit is not None:
            self.gross_profit = gross_profit
        if minimum_selling_price is not None:
            self.minimum_selling_price = minimum_selling_price

    @property
    def inclusive(self):
        """Gets the inclusive of this RoomRateTotals.  # noqa: E501


        :return: The inclusive of this RoomRateTotals.  # noqa: E501
        :rtype: RoomRateTotalsInclusive
        """
        return self._inclusive

    @inclusive.setter
    def inclusive(self, inclusive):
        """Sets the inclusive of this RoomRateTotals.


        :param inclusive: The inclusive of this RoomRateTotals.  # noqa: E501
        :type: RoomRateTotalsInclusive
        """
        if inclusive is None:
            raise ValueError("Invalid value for `inclusive`, must not be `None`")  # noqa: E501

        self._inclusive = inclusive

    @property
    def exclusive(self):
        """Gets the exclusive of this RoomRateTotals.  # noqa: E501


        :return: The exclusive of this RoomRateTotals.  # noqa: E501
        :rtype: RoomRateTotalsExclusive
        """
        return self._exclusive

    @exclusive.setter
    def exclusive(self, exclusive):
        """Sets the exclusive of this RoomRateTotals.


        :param exclusive: The exclusive of this RoomRateTotals.  # noqa: E501
        :type: RoomRateTotalsExclusive
        """
        if exclusive is None:
            raise ValueError("Invalid value for `exclusive`, must not be `None`")  # noqa: E501

        self._exclusive = exclusive

    @property
    def strikethrough(self):
        """Gets the strikethrough of this RoomRateTotals.  # noqa: E501


        :return: The strikethrough of this RoomRateTotals.  # noqa: E501
        :rtype: RoomRateTotalsStrikethrough
        """
        return self._strikethrough

    @strikethrough.setter
    def strikethrough(self, strikethrough):
        """Sets the strikethrough of this RoomRateTotals.


        :param strikethrough: The strikethrough of this RoomRateTotals.  # noqa: E501
        :type: RoomRateTotalsStrikethrough
        """

        self._strikethrough = strikethrough

    @property
    def marketing_fee(self):
        """Gets the marketing_fee of this RoomRateTotals.  # noqa: E501


        :return: The marketing_fee of this RoomRateTotals.  # noqa: E501
        :rtype: RoomRateTotalsMarketingFee
        """
        return self._marketing_fee

    @marketing_fee.setter
    def marketing_fee(self, marketing_fee):
        """Sets the marketing_fee of this RoomRateTotals.


        :param marketing_fee: The marketing_fee of this RoomRateTotals.  # noqa: E501
        :type: RoomRateTotalsMarketingFee
        """

        self._marketing_fee = marketing_fee

    @property
    def gross_profit(self):
        """Gets the gross_profit of this RoomRateTotals.  # noqa: E501


        :return: The gross_profit of this RoomRateTotals.  # noqa: E501
        :rtype: RoomRateTotalsGrossProfit
        """
        return self._gross_profit

    @gross_profit.setter
    def gross_profit(self, gross_profit):
        """Sets the gross_profit of this RoomRateTotals.


        :param gross_profit: The gross_profit of this RoomRateTotals.  # noqa: E501
        :type: RoomRateTotalsGrossProfit
        """

        self._gross_profit = gross_profit

    @property
    def minimum_selling_price(self):
        """Gets the minimum_selling_price of this RoomRateTotals.  # noqa: E501


        :return: The minimum_selling_price of this RoomRateTotals.  # noqa: E501
        :rtype: RoomRateTotalsMinimumSellingPrice
        """
        return self._minimum_selling_price

    @minimum_selling_price.setter
    def minimum_selling_price(self, minimum_selling_price):
        """Sets the minimum_selling_price of this RoomRateTotals.


        :param minimum_selling_price: The minimum_selling_price of this RoomRateTotals.  # noqa: E501
        :type: RoomRateTotalsMinimumSellingPrice
        """

        self._minimum_selling_price = minimum_selling_price

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
        if issubclass(RoomRateTotals, dict):
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
        if not isinstance(other, RoomRateTotals):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
