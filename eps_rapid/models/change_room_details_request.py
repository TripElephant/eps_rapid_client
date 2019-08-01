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

from eps_rapid.models.phone import Phone  # noqa: F401,E501


class ChangeRoomDetailsRequest(object):
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
        'given_name': 'str',
        'family_name': 'str',
        'phone': 'Phone',
        'smoking': 'bool',
        'special_request': 'str'
    }

    attribute_map = {
        'given_name': 'given_name',
        'family_name': 'family_name',
        'phone': 'phone',
        'smoking': 'smoking',
        'special_request': 'special_request'
    }

    def __init__(self, given_name=None, family_name=None, phone=None, smoking=None, special_request=None):  # noqa: E501
        """ChangeRoomDetailsRequest - a model defined in Swagger"""  # noqa: E501

        self._given_name = None
        self._family_name = None
        self._phone = None
        self._smoking = None
        self._special_request = None
        self.discriminator = None

        if given_name is not None:
            self.given_name = given_name
        if family_name is not None:
            self.family_name = family_name
        if phone is not None:
            self.phone = phone
        if smoking is not None:
            self.smoking = smoking
        if special_request is not None:
            self.special_request = special_request

    @property
    def given_name(self):
        """Gets the given_name of this ChangeRoomDetailsRequest.  # noqa: E501

        First name of room guest.  # noqa: E501

        :return: The given_name of this ChangeRoomDetailsRequest.  # noqa: E501
        :rtype: str
        """
        return self._given_name

    @given_name.setter
    def given_name(self, given_name):
        """Sets the given_name of this ChangeRoomDetailsRequest.

        First name of room guest.  # noqa: E501

        :param given_name: The given_name of this ChangeRoomDetailsRequest.  # noqa: E501
        :type: str
        """

        self._given_name = given_name

    @property
    def family_name(self):
        """Gets the family_name of this ChangeRoomDetailsRequest.  # noqa: E501

        Last name of room guest.  # noqa: E501

        :return: The family_name of this ChangeRoomDetailsRequest.  # noqa: E501
        :rtype: str
        """
        return self._family_name

    @family_name.setter
    def family_name(self, family_name):
        """Sets the family_name of this ChangeRoomDetailsRequest.

        Last name of room guest.  # noqa: E501

        :param family_name: The family_name of this ChangeRoomDetailsRequest.  # noqa: E501
        :type: str
        """

        self._family_name = family_name

    @property
    def phone(self):
        """Gets the phone of this ChangeRoomDetailsRequest.  # noqa: E501


        :return: The phone of this ChangeRoomDetailsRequest.  # noqa: E501
        :rtype: Phone
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this ChangeRoomDetailsRequest.


        :param phone: The phone of this ChangeRoomDetailsRequest.  # noqa: E501
        :type: Phone
        """

        self._phone = phone

    @property
    def smoking(self):
        """Gets the smoking of this ChangeRoomDetailsRequest.  # noqa: E501

        If the room guest would prefer a smoking room.  # noqa: E501

        :return: The smoking of this ChangeRoomDetailsRequest.  # noqa: E501
        :rtype: bool
        """
        return self._smoking

    @smoking.setter
    def smoking(self, smoking):
        """Sets the smoking of this ChangeRoomDetailsRequest.

        If the room guest would prefer a smoking room.  # noqa: E501

        :param smoking: The smoking of this ChangeRoomDetailsRequest.  # noqa: E501
        :type: bool
        """

        self._smoking = smoking

    @property
    def special_request(self):
        """Gets the special_request of this ChangeRoomDetailsRequest.  # noqa: E501

        Special requests to send to hotel (not guaranteed). Do not use this field to communicate B2B customer service requests or pass any sensitive personal or financial information (PII).  # noqa: E501

        :return: The special_request of this ChangeRoomDetailsRequest.  # noqa: E501
        :rtype: str
        """
        return self._special_request

    @special_request.setter
    def special_request(self, special_request):
        """Sets the special_request of this ChangeRoomDetailsRequest.

        Special requests to send to hotel (not guaranteed). Do not use this field to communicate B2B customer service requests or pass any sensitive personal or financial information (PII).  # noqa: E501

        :param special_request: The special_request of this ChangeRoomDetailsRequest.  # noqa: E501
        :type: str
        """

        self._special_request = special_request

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
        if issubclass(ChangeRoomDetailsRequest, dict):
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
        if not isinstance(other, ChangeRoomDetailsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
