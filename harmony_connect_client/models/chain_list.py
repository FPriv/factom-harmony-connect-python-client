# coding: utf-8

"""
    Harmony Connect

    An easy to use API that helps you access the Factom blockchain.  # noqa: E501

    OpenAPI spec version: 1.0.17
    Contact: harmony-support@factom.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class ChainList(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'data': 'list[ChainListData]',
        'offset': 'int',
        'limit': 'int',
        'count': 'int'
    }

    attribute_map = {
        'data': 'data',
        'offset': 'offset',
        'limit': 'limit',
        'count': 'count'
    }

    def __init__(self, data=None, offset=None, limit=None, count=None):  # noqa: E501
        """ChainList - a model defined in OpenAPI"""  # noqa: E501

        self._data = None
        self._offset = None
        self._limit = None
        self._count = None
        self.discriminator = None

        self.data = data
        self.offset = offset
        self.limit = limit
        self.count = count

    @property
    def data(self):
        """Gets the data of this ChainList.  # noqa: E501

        An array that contains the chains on this page.  # noqa: E501

        :return: The data of this ChainList.  # noqa: E501
        :rtype: list[ChainListData]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this ChainList.

        An array that contains the chains on this page.  # noqa: E501

        :param data: The data of this ChainList.  # noqa: E501
        :type: list[ChainListData]
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data

    @property
    def offset(self):
        """Gets the offset of this ChainList.  # noqa: E501

        The index of the first chain returned from the total set (Starting from 0).  # noqa: E501

        :return: The offset of this ChainList.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ChainList.

        The index of the first chain returned from the total set (Starting from 0).  # noqa: E501

        :param offset: The offset of this ChainList.  # noqa: E501
        :type: int
        """
        if offset is None:
            raise ValueError("Invalid value for `offset`, must not be `None`")  # noqa: E501

        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ChainList.  # noqa: E501

        The number of chains returned.  # noqa: E501

        :return: The limit of this ChainList.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ChainList.

        The number of chains returned.  # noqa: E501

        :param limit: The limit of this ChainList.  # noqa: E501
        :type: int
        """
        if limit is None:
            raise ValueError("Invalid value for `limit`, must not be `None`")  # noqa: E501

        self._limit = limit

    @property
    def count(self):
        """Gets the count of this ChainList.  # noqa: E501

        The total number of chains seen.  # noqa: E501

        :return: The count of this ChainList.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ChainList.

        The total number of chains seen.  # noqa: E501

        :param count: The count of this ChainList.  # noqa: E501
        :type: int
        """
        if count is None:
            raise ValueError("Invalid value for `count`, must not be `None`")  # noqa: E501

        self._count = count

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ChainList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
