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


class EntryDataEblock(object):
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
        'keymr': 'str',
        'href': 'str'
    }

    attribute_map = {
        'keymr': 'keymr',
        'href': 'href'
    }

    def __init__(self, keymr=None, href=None):  # noqa: E501
        """EntryDataEblock - a model defined in OpenAPI"""  # noqa: E501

        self._keymr = None
        self._href = None
        self.discriminator = None

        if keymr is not None:
            self.keymr = keymr
        if href is not None:
            self.href = href

    @property
    def keymr(self):
        """Gets the keymr of this EntryDataEblock.  # noqa: E501

        The Key Merkle Root for this entry block.  # noqa: E501

        :return: The keymr of this EntryDataEblock.  # noqa: E501
        :rtype: str
        """
        return self._keymr

    @keymr.setter
    def keymr(self, keymr):
        """Sets the keymr of this EntryDataEblock.

        The Key Merkle Root for this entry block.  # noqa: E501

        :param keymr: The keymr of this EntryDataEblock.  # noqa: E501
        :type: str
        """

        self._keymr = keymr

    @property
    def href(self):
        """Gets the href of this EntryDataEblock.  # noqa: E501

        An API link to retrieve all information about this entry block.  # noqa: E501

        :return: The href of this EntryDataEblock.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this EntryDataEblock.

        An API link to retrieve all information about this entry block.  # noqa: E501

        :param href: The href of this EntryDataEblock.  # noqa: E501
        :type: str
        """

        self._href = href

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
        if not isinstance(other, EntryDataEblock):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
