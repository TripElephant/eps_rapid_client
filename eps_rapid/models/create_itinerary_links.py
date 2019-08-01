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

from eps_rapid.models.create_itinerary_links_complete_payment_session import CreateItineraryLinksCompletePaymentSession  # noqa: F401,E501
from eps_rapid.models.create_itinerary_links_resume import CreateItineraryLinksResume  # noqa: F401,E501
from eps_rapid.models.create_itinerary_links_retrieve import CreateItineraryLinksRetrieve  # noqa: F401,E501
from eps_rapid.models.retrieve_links_cancel import RetrieveLinksCancel  # noqa: F401,E501


class CreateItineraryLinks(object):
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
        'retrieve': 'CreateItineraryLinksRetrieve',
        'resume': 'CreateItineraryLinksResume',
        'complete_payment_session': 'CreateItineraryLinksCompletePaymentSession',
        'cancel': 'RetrieveLinksCancel'
    }

    attribute_map = {
        'retrieve': 'retrieve',
        'resume': 'resume',
        'complete_payment_session': 'complete_payment_session',
        'cancel': 'cancel'
    }

    def __init__(self, retrieve=None, resume=None, complete_payment_session=None, cancel=None):  # noqa: E501
        """CreateItineraryLinks - a model defined in Swagger"""  # noqa: E501

        self._retrieve = None
        self._resume = None
        self._complete_payment_session = None
        self._cancel = None
        self.discriminator = None

        if retrieve is not None:
            self.retrieve = retrieve
        if resume is not None:
            self.resume = resume
        if complete_payment_session is not None:
            self.complete_payment_session = complete_payment_session
        if cancel is not None:
            self.cancel = cancel

    @property
    def retrieve(self):
        """Gets the retrieve of this CreateItineraryLinks.  # noqa: E501


        :return: The retrieve of this CreateItineraryLinks.  # noqa: E501
        :rtype: CreateItineraryLinksRetrieve
        """
        return self._retrieve

    @retrieve.setter
    def retrieve(self, retrieve):
        """Sets the retrieve of this CreateItineraryLinks.


        :param retrieve: The retrieve of this CreateItineraryLinks.  # noqa: E501
        :type: CreateItineraryLinksRetrieve
        """

        self._retrieve = retrieve

    @property
    def resume(self):
        """Gets the resume of this CreateItineraryLinks.  # noqa: E501


        :return: The resume of this CreateItineraryLinks.  # noqa: E501
        :rtype: CreateItineraryLinksResume
        """
        return self._resume

    @resume.setter
    def resume(self, resume):
        """Sets the resume of this CreateItineraryLinks.


        :param resume: The resume of this CreateItineraryLinks.  # noqa: E501
        :type: CreateItineraryLinksResume
        """

        self._resume = resume

    @property
    def complete_payment_session(self):
        """Gets the complete_payment_session of this CreateItineraryLinks.  # noqa: E501


        :return: The complete_payment_session of this CreateItineraryLinks.  # noqa: E501
        :rtype: CreateItineraryLinksCompletePaymentSession
        """
        return self._complete_payment_session

    @complete_payment_session.setter
    def complete_payment_session(self, complete_payment_session):
        """Sets the complete_payment_session of this CreateItineraryLinks.


        :param complete_payment_session: The complete_payment_session of this CreateItineraryLinks.  # noqa: E501
        :type: CreateItineraryLinksCompletePaymentSession
        """

        self._complete_payment_session = complete_payment_session

    @property
    def cancel(self):
        """Gets the cancel of this CreateItineraryLinks.  # noqa: E501


        :return: The cancel of this CreateItineraryLinks.  # noqa: E501
        :rtype: RetrieveLinksCancel
        """
        return self._cancel

    @cancel.setter
    def cancel(self, cancel):
        """Sets the cancel of this CreateItineraryLinks.


        :param cancel: The cancel of this CreateItineraryLinks.  # noqa: E501
        :type: RetrieveLinksCancel
        """

        self._cancel = cancel

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
        if issubclass(CreateItineraryLinks, dict):
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
        if not isinstance(other, CreateItineraryLinks):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
