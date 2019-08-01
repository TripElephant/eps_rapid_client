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


class Review(object):
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
        'verification_source': 'str',
        'title': 'str',
        'date_submitted': 'str',
        'rating': 'str',
        'reviewer_name': 'str',
        'text': 'str'
    }

    attribute_map = {
        'verification_source': 'verification_source',
        'title': 'title',
        'date_submitted': 'date_submitted',
        'rating': 'rating',
        'reviewer_name': 'reviewer_name',
        'text': 'text'
    }

    def __init__(self, verification_source=None, title=None, date_submitted=None, rating=None, reviewer_name=None, text=None):  # noqa: E501
        """Review - a model defined in Swagger"""  # noqa: E501

        self._verification_source = None
        self._title = None
        self._date_submitted = None
        self._rating = None
        self._reviewer_name = None
        self._text = None
        self.discriminator = None

        if verification_source is not None:
            self.verification_source = verification_source
        if title is not None:
            self.title = title
        if date_submitted is not None:
            self.date_submitted = date_submitted
        if rating is not None:
            self.rating = rating
        if reviewer_name is not None:
            self.reviewer_name = reviewer_name
        if text is not None:
            self.text = text

    @property
    def verification_source(self):
        """Gets the verification_source of this Review.  # noqa: E501

        Where this review has been verified from.  # noqa: E501

        :return: The verification_source of this Review.  # noqa: E501
        :rtype: str
        """
        return self._verification_source

    @verification_source.setter
    def verification_source(self, verification_source):
        """Sets the verification_source of this Review.

        Where this review has been verified from.  # noqa: E501

        :param verification_source: The verification_source of this Review.  # noqa: E501
        :type: str
        """

        self._verification_source = verification_source

    @property
    def title(self):
        """Gets the title of this Review.  # noqa: E501

        Title of this review.  # noqa: E501

        :return: The title of this Review.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Review.

        Title of this review.  # noqa: E501

        :param title: The title of this Review.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def date_submitted(self):
        """Gets the date_submitted of this Review.  # noqa: E501

        When this review was made, in ISO 8601 format.  # noqa: E501

        :return: The date_submitted of this Review.  # noqa: E501
        :rtype: str
        """
        return self._date_submitted

    @date_submitted.setter
    def date_submitted(self, date_submitted):
        """Sets the date_submitted of this Review.

        When this review was made, in ISO 8601 format.  # noqa: E501

        :param date_submitted: The date_submitted of this Review.  # noqa: E501
        :type: str
        """

        self._date_submitted = date_submitted

    @property
    def rating(self):
        """Gets the rating of this Review.  # noqa: E501

        The rating for this property given by the reviewer.  # noqa: E501

        :return: The rating of this Review.  # noqa: E501
        :rtype: str
        """
        return self._rating

    @rating.setter
    def rating(self, rating):
        """Sets the rating of this Review.

        The rating for this property given by the reviewer.  # noqa: E501

        :param rating: The rating of this Review.  # noqa: E501
        :type: str
        """

        self._rating = rating

    @property
    def reviewer_name(self):
        """Gets the reviewer_name of this Review.  # noqa: E501

        The name of the person who wrote this review.  # noqa: E501

        :return: The reviewer_name of this Review.  # noqa: E501
        :rtype: str
        """
        return self._reviewer_name

    @reviewer_name.setter
    def reviewer_name(self, reviewer_name):
        """Sets the reviewer_name of this Review.

        The name of the person who wrote this review.  # noqa: E501

        :param reviewer_name: The reviewer_name of this Review.  # noqa: E501
        :type: str
        """

        self._reviewer_name = reviewer_name

    @property
    def text(self):
        """Gets the text of this Review.  # noqa: E501

        The text of the review itself.  # noqa: E501

        :return: The text of this Review.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this Review.

        The text of the review itself.  # noqa: E501

        :param text: The text of this Review.  # noqa: E501
        :type: str
        """

        self._text = text

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
        if issubclass(Review, dict):
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
        if not isinstance(other, Review):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
