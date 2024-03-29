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

from eps_rapid.models.create_itinerary_request_rooms import CreateItineraryRequestRooms  # noqa: F401,E501


class CreateItineraryRequest(object):
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
        'affiliate_reference_id': 'str',
        'hold': 'bool',
        'rooms': 'list[CreateItineraryRequestRooms]',
        'payments': 'object',
        'affiliate_metadata': 'str',
        'tax_registration_number': 'str',
        'traveler_handling_instructions': 'str'
    }

    attribute_map = {
        'affiliate_reference_id': 'affiliate_reference_id',
        'hold': 'hold',
        'rooms': 'rooms',
        'payments': 'payments',
        'affiliate_metadata': 'affiliate_metadata',
        'tax_registration_number': 'tax_registration_number',
        'traveler_handling_instructions': 'traveler_handling_instructions'
    }

    def __init__(self, affiliate_reference_id=None, hold=None, rooms=None, payments=None, affiliate_metadata=None, tax_registration_number=None, traveler_handling_instructions=None):  # noqa: E501
        """CreateItineraryRequest - a model defined in Swagger"""  # noqa: E501

        self._affiliate_reference_id = None
        self._hold = None
        self._rooms = None
        self._payments = None
        self._affiliate_metadata = None
        self._tax_registration_number = None
        self._traveler_handling_instructions = None
        self.discriminator = None

        if affiliate_reference_id is not None:
            self.affiliate_reference_id = affiliate_reference_id
        if hold is not None:
            self.hold = hold
        self.rooms = rooms
        if payments is not None:
            self.payments = payments
        if affiliate_metadata is not None:
            self.affiliate_metadata = affiliate_metadata
        if tax_registration_number is not None:
            self.tax_registration_number = tax_registration_number
        if traveler_handling_instructions is not None:
            self.traveler_handling_instructions = traveler_handling_instructions

    @property
    def affiliate_reference_id(self):
        """Gets the affiliate_reference_id of this CreateItineraryRequest.  # noqa: E501

        Your unique reference value. This field supports a maximum of 28 characters and is required to be unique (if provided).  # noqa: E501

        :return: The affiliate_reference_id of this CreateItineraryRequest.  # noqa: E501
        :rtype: str
        """
        return self._affiliate_reference_id

    @affiliate_reference_id.setter
    def affiliate_reference_id(self, affiliate_reference_id):
        """Sets the affiliate_reference_id of this CreateItineraryRequest.

        Your unique reference value. This field supports a maximum of 28 characters and is required to be unique (if provided).  # noqa: E501

        :param affiliate_reference_id: The affiliate_reference_id of this CreateItineraryRequest.  # noqa: E501
        :type: str
        """

        self._affiliate_reference_id = affiliate_reference_id

    @property
    def hold(self):
        """Gets the hold of this CreateItineraryRequest.  # noqa: E501

        Flag for placing a booking on hold. The booking will be released if the resume link is not followed within the hold period. Please refer to our Hold and Resume documentation.  # noqa: E501

        :return: The hold of this CreateItineraryRequest.  # noqa: E501
        :rtype: bool
        """
        return self._hold

    @hold.setter
    def hold(self, hold):
        """Sets the hold of this CreateItineraryRequest.

        Flag for placing a booking on hold. The booking will be released if the resume link is not followed within the hold period. Please refer to our Hold and Resume documentation.  # noqa: E501

        :param hold: The hold of this CreateItineraryRequest.  # noqa: E501
        :type: bool
        """

        self._hold = hold

    @property
    def rooms(self):
        """Gets the rooms of this CreateItineraryRequest.  # noqa: E501


        :return: The rooms of this CreateItineraryRequest.  # noqa: E501
        :rtype: list[CreateItineraryRequestRooms]
        """
        return self._rooms

    @rooms.setter
    def rooms(self, rooms):
        """Sets the rooms of this CreateItineraryRequest.


        :param rooms: The rooms of this CreateItineraryRequest.  # noqa: E501
        :type: list[CreateItineraryRequestRooms]
        """
        if rooms is None:
            raise ValueError("Invalid value for `rooms`, must not be `None`")  # noqa: E501

        self._rooms = rooms

    @property
    def payments(self):
        """Gets the payments of this CreateItineraryRequest.  # noqa: E501


        :return: The payments of this CreateItineraryRequest.  # noqa: E501
        :rtype: object
        """
        return self._payments

    @payments.setter
    def payments(self, payments):
        """Sets the payments of this CreateItineraryRequest.


        :param payments: The payments of this CreateItineraryRequest.  # noqa: E501
        :type: object
        """

        self._payments = payments

    @property
    def affiliate_metadata(self):
        """Gets the affiliate_metadata of this CreateItineraryRequest.  # noqa: E501

        Field that stores up to 256 characters of additional metadata with the itinerary. Will be returned on all retrieve responses for this itinerary. The data must be in the format 'key1:value|key2:value|key3:value'.  # noqa: E501

        :return: The affiliate_metadata of this CreateItineraryRequest.  # noqa: E501
        :rtype: str
        """
        return self._affiliate_metadata

    @affiliate_metadata.setter
    def affiliate_metadata(self, affiliate_metadata):
        """Sets the affiliate_metadata of this CreateItineraryRequest.

        Field that stores up to 256 characters of additional metadata with the itinerary. Will be returned on all retrieve responses for this itinerary. The data must be in the format 'key1:value|key2:value|key3:value'.  # noqa: E501

        :param affiliate_metadata: The affiliate_metadata of this CreateItineraryRequest.  # noqa: E501
        :type: str
        """

        self._affiliate_metadata = affiliate_metadata

    @property
    def tax_registration_number(self):
        """Gets the tax_registration_number of this CreateItineraryRequest.  # noqa: E501

        The customer's taxpayer identification number that is provided by the government to nationals or resident aliens. This number should be collected from individuals that pay taxes or participate in activities that provide revenue for one or more tax types.  Note: This value is only needed from Brazilian customers.  # noqa: E501

        :return: The tax_registration_number of this CreateItineraryRequest.  # noqa: E501
        :rtype: str
        """
        return self._tax_registration_number

    @tax_registration_number.setter
    def tax_registration_number(self, tax_registration_number):
        """Sets the tax_registration_number of this CreateItineraryRequest.

        The customer's taxpayer identification number that is provided by the government to nationals or resident aliens. This number should be collected from individuals that pay taxes or participate in activities that provide revenue for one or more tax types.  Note: This value is only needed from Brazilian customers.  # noqa: E501

        :param tax_registration_number: The tax_registration_number of this CreateItineraryRequest.  # noqa: E501
        :type: str
        """

        self._tax_registration_number = tax_registration_number

    @property
    def traveler_handling_instructions(self):
        """Gets the traveler_handling_instructions of this CreateItineraryRequest.  # noqa: E501

        Custom traveler handling instructions for the hotel. Do not include PCI sensitive data, such as credit card numbers, in this field.  # noqa: E501

        :return: The traveler_handling_instructions of this CreateItineraryRequest.  # noqa: E501
        :rtype: str
        """
        return self._traveler_handling_instructions

    @traveler_handling_instructions.setter
    def traveler_handling_instructions(self, traveler_handling_instructions):
        """Sets the traveler_handling_instructions of this CreateItineraryRequest.

        Custom traveler handling instructions for the hotel. Do not include PCI sensitive data, such as credit card numbers, in this field.  # noqa: E501

        :param traveler_handling_instructions: The traveler_handling_instructions of this CreateItineraryRequest.  # noqa: E501
        :type: str
        """

        self._traveler_handling_instructions = traveler_handling_instructions

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
        if issubclass(CreateItineraryRequest, dict):
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
        if not isinstance(other, CreateItineraryRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
