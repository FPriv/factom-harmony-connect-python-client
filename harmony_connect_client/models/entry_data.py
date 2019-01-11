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


class EntryData(object):
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
        'entry_hash': 'str',
        'chain': 'EntryLinkChain',
        'created_at': 'str',
        'external_ids': 'list[str]',
        'content': 'str',
        'stage': 'str',
        'eblock': 'EntryDataEblock'
    }

    attribute_map = {
        'entry_hash': 'entry_hash',
        'chain': 'chain',
        'created_at': 'created_at',
        'external_ids': 'external_ids',
        'content': 'content',
        'stage': 'stage',
        'eblock': 'eblock'
    }

    def __init__(self, entry_hash=None, chain=None, created_at=None, external_ids=None, content=None, stage=None, eblock=None):  # noqa: E501
        """EntryData - a model defined in OpenAPI"""  # noqa: E501

        self._entry_hash = None
        self._chain = None
        self._created_at = None
        self._external_ids = None
        self._content = None
        self._stage = None
        self._eblock = None
        self.discriminator = None

        if entry_hash is not None:
            self.entry_hash = entry_hash
        if chain is not None:
            self.chain = chain
        if created_at is not None:
            self.created_at = created_at
        if external_ids is not None:
            self.external_ids = external_ids
        if content is not None:
            self.content = content
        if stage is not None:
            self.stage = stage
        if eblock is not None:
            self.eblock = eblock

    @property
    def entry_hash(self):
        """Gets the entry_hash of this EntryData.  # noqa: E501

        The SHA256 Hash of this entry.  # noqa: E501

        :return: The entry_hash of this EntryData.  # noqa: E501
        :rtype: str
        """
        return self._entry_hash

    @entry_hash.setter
    def entry_hash(self, entry_hash):
        """Sets the entry_hash of this EntryData.

        The SHA256 Hash of this entry.  # noqa: E501

        :param entry_hash: The entry_hash of this EntryData.  # noqa: E501
        :type: str
        """

        self._entry_hash = entry_hash

    @property
    def chain(self):
        """Gets the chain of this EntryData.  # noqa: E501


        :return: The chain of this EntryData.  # noqa: E501
        :rtype: EntryLinkChain
        """
        return self._chain

    @chain.setter
    def chain(self, chain):
        """Sets the chain of this EntryData.


        :param chain: The chain of this EntryData.  # noqa: E501
        :type: EntryLinkChain
        """

        self._chain = chain

    @property
    def created_at(self):
        """Gets the created_at of this EntryData.  # noqa: E501

        The time when this entry was created. Sent in [ISO 8601 Format](https://en.wikipedia.org/wiki/ISO_8601). For example: `YYYY-MM-DDThh:mm:ssZ`  # noqa: E501

        :return: The created_at of this EntryData.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this EntryData.

        The time when this entry was created. Sent in [ISO 8601 Format](https://en.wikipedia.org/wiki/ISO_8601). For example: `YYYY-MM-DDThh:mm:ssZ`  # noqa: E501

        :param created_at: The created_at of this EntryData.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def external_ids(self):
        """Gets the external_ids of this EntryData.  # noqa: E501

        Tags that can be used to identify your entry. You can search for records that contain a particular external_id using Connect. External IDs are returned in Base64.  # noqa: E501

        :return: The external_ids of this EntryData.  # noqa: E501
        :rtype: list[str]
        """
        return self._external_ids

    @external_ids.setter
    def external_ids(self, external_ids):
        """Sets the external_ids of this EntryData.

        Tags that can be used to identify your entry. You can search for records that contain a particular external_id using Connect. External IDs are returned in Base64.  # noqa: E501

        :param external_ids: The external_ids of this EntryData.  # noqa: E501
        :type: list[str]
        """

        self._external_ids = external_ids

    @property
    def content(self):
        """Gets the content of this EntryData.  # noqa: E501

        This is the data that is stored by the entry. Content will be sent in Base64 format.  # noqa: E501

        :return: The content of this EntryData.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this EntryData.

        This is the data that is stored by the entry. Content will be sent in Base64 format.  # noqa: E501

        :param content: The content of this EntryData.  # noqa: E501
        :type: str
        """

        self._content = content

    @property
    def stage(self):
        """Gets the stage of this EntryData.  # noqa: E501

        The level of immutability that this entry has reached.  # noqa: E501

        :return: The stage of this EntryData.  # noqa: E501
        :rtype: str
        """
        return self._stage

    @stage.setter
    def stage(self, stage):
        """Sets the stage of this EntryData.

        The level of immutability that this entry has reached.  # noqa: E501

        :param stage: The stage of this EntryData.  # noqa: E501
        :type: str
        """

        self._stage = stage

    @property
    def eblock(self):
        """Gets the eblock of this EntryData.  # noqa: E501


        :return: The eblock of this EntryData.  # noqa: E501
        :rtype: EntryDataEblock
        """
        return self._eblock

    @eblock.setter
    def eblock(self, eblock):
        """Sets the eblock of this EntryData.


        :param eblock: The eblock of this EntryData.  # noqa: E501
        :type: EntryDataEblock
        """

        self._eblock = eblock

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
        if not isinstance(other, EntryData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other