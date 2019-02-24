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


class ChainData(object):
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
        'chain_id': 'str',
        'content': 'str',
        'external_ids': 'list[str]',
        'stage': 'str',
        'entries': 'ChainDataEntries',
        'eblock': 'ChainDataEblock',
        'dblock': 'ChainDataDblock',
        'created_at': 'str'
    }

    attribute_map = {
        'chain_id': 'chain_id',
        'content': 'content',
        'external_ids': 'external_ids',
        'stage': 'stage',
        'entries': 'entries',
        'eblock': 'eblock',
        'dblock': 'dblock',
        'created_at': 'created_at'
    }

    def __init__(self, chain_id=None, content=None, external_ids=None, stage=None, entries=None, eblock=None, dblock=None, created_at=None):  # noqa: E501
        """ChainData - a model defined in OpenAPI"""  # noqa: E501

        self._chain_id = None
        self._content = None
        self._external_ids = None
        self._stage = None
        self._entries = None
        self._eblock = None
        self._dblock = None
        self._created_at = None
        self.discriminator = None

        self.chain_id = chain_id
        self.content = content
        self.external_ids = external_ids
        self.stage = stage
        self.entries = entries
        if eblock is not None:
            self.eblock = eblock
        if dblock is not None:
            self.dblock = dblock
        self.created_at = created_at

    @property
    def chain_id(self):
        """Gets the chain_id of this ChainData.  # noqa: E501

        This is the unique identifier created for each chain.  # noqa: E501

        :return: The chain_id of this ChainData.  # noqa: E501
        :rtype: str
        """
        return self._chain_id

    @chain_id.setter
    def chain_id(self, chain_id):
        """Sets the chain_id of this ChainData.

        This is the unique identifier created for each chain.  # noqa: E501

        :param chain_id: The chain_id of this ChainData.  # noqa: E501
        :type: str
        """
        if chain_id is None:
            raise ValueError("Invalid value for `chain_id`, must not be `None`")  # noqa: E501

        self._chain_id = chain_id

    @property
    def content(self):
        """Gets the content of this ChainData.  # noqa: E501

        This is the data that was stored in the first entry of this chain.  # noqa: E501

        :return: The content of this ChainData.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this ChainData.

        This is the data that was stored in the first entry of this chain.  # noqa: E501

        :param content: The content of this ChainData.  # noqa: E501
        :type: str
        """
        if content is None:
            raise ValueError("Invalid value for `content`, must not be `None`")  # noqa: E501

        self._content = content

    @property
    def external_ids(self):
        """Gets the external_ids of this ChainData.  # noqa: E501

        Tags that have been used to identify this entry.  # noqa: E501

        :return: The external_ids of this ChainData.  # noqa: E501
        :rtype: list[str]
        """
        return self._external_ids

    @external_ids.setter
    def external_ids(self, external_ids):
        """Sets the external_ids of this ChainData.

        Tags that have been used to identify this entry.  # noqa: E501

        :param external_ids: The external_ids of this ChainData.  # noqa: E501
        :type: list[str]
        """
        if external_ids is None:
            raise ValueError("Invalid value for `external_ids`, must not be `None`")  # noqa: E501

        self._external_ids = external_ids

    @property
    def stage(self):
        """Gets the stage of this ChainData.  # noqa: E501

        The immutability stage that this chain has reached.  # noqa: E501

        :return: The stage of this ChainData.  # noqa: E501
        :rtype: str
        """
        return self._stage

    @stage.setter
    def stage(self, stage):
        """Sets the stage of this ChainData.

        The immutability stage that this chain has reached.  # noqa: E501

        :param stage: The stage of this ChainData.  # noqa: E501
        :type: str
        """
        if stage is None:
            raise ValueError("Invalid value for `stage`, must not be `None`")  # noqa: E501

        self._stage = stage

    @property
    def entries(self):
        """Gets the entries of this ChainData.  # noqa: E501


        :return: The entries of this ChainData.  # noqa: E501
        :rtype: ChainDataEntries
        """
        return self._entries

    @entries.setter
    def entries(self, entries):
        """Sets the entries of this ChainData.


        :param entries: The entries of this ChainData.  # noqa: E501
        :type: ChainDataEntries
        """
        if entries is None:
            raise ValueError("Invalid value for `entries`, must not be `None`")  # noqa: E501

        self._entries = entries

    @property
    def eblock(self):
        """Gets the eblock of this ChainData.  # noqa: E501


        :return: The eblock of this ChainData.  # noqa: E501
        :rtype: ChainDataEblock
        """
        return self._eblock

    @eblock.setter
    def eblock(self, eblock):
        """Sets the eblock of this ChainData.


        :param eblock: The eblock of this ChainData.  # noqa: E501
        :type: ChainDataEblock
        """

        self._eblock = eblock

    @property
    def dblock(self):
        """Gets the dblock of this ChainData.  # noqa: E501


        :return: The dblock of this ChainData.  # noqa: E501
        :rtype: ChainDataDblock
        """
        return self._dblock

    @dblock.setter
    def dblock(self, dblock):
        """Sets the dblock of this ChainData.


        :param dblock: The dblock of this ChainData.  # noqa: E501
        :type: ChainDataDblock
        """

        self._dblock = dblock

    @property
    def created_at(self):
        """Gets the created_at of this ChainData.  # noqa: E501

        The time at which this chain was created. Sent in [ISO 8601 Format](https://en.wikipedia.org/wiki/ISO_8601). For example: `YYYY-MM-DDThh:mm:ss.ssssssZ` This will be null if the chain is not at least at the `factom` immutability stage.  # noqa: E501

        :return: The created_at of this ChainData.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ChainData.

        The time at which this chain was created. Sent in [ISO 8601 Format](https://en.wikipedia.org/wiki/ISO_8601). For example: `YYYY-MM-DDThh:mm:ss.ssssssZ` This will be null if the chain is not at least at the `factom` immutability stage.  # noqa: E501

        :param created_at: The created_at of this ChainData.  # noqa: E501
        :type: str
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

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
        if not isinstance(other, ChainData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
