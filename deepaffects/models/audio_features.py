# coding: utf-8

"""
    DeepAffects

    OpenAPI Specification of DeepAffects APIs  # noqa: E501

    OpenAPI spec version: 0.1.0

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class AudioFeatures(object):
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
        'mfccs': 'list[list[float]]',
        'zcr': 'list[float]',
        'energy': 'list[float]'
    }

    attribute_map = {
        'mfccs': 'mfccs',
        'zcr': 'zcr',
        'energy': 'energy'
    }

    def __init__(self, mfccs=None, zcr=None, energy=None):  # noqa: E501
        """AudioFeatures - a model defined in Swagger"""  # noqa: E501

        self._mfccs = None
        self._zcr = None
        self._energy = None
        self.discriminator = None


    @property
    def mfccs(self):
        """Gets the mfccs of this AudioFeatures.  # noqa: E501

        mel frequency cepstral coefficients  # noqa: E501

        :return: The mfccs of this AudioFeatures.  # noqa: E501
        :rtype: list[list[float]]
        """
        return self._mfccs

    @mfccs.setter
    def mfccs(self, mfccs):
        """Sets the mfccs of this AudioFeatures.

        mel frequency cepstral coefficients  # noqa: E501

        :param mfccs: The mfccs of this AudioFeatures.  # noqa: E501
        :type: list[list[float]]
        """
        if mfccs is None:
            raise ValueError("Invalid value for `mfccs`, must not be `None`")  # noqa: E501

        self._mfccs = mfccs

    @property
    def zcr(self):
        """Gets the zcr of this AudioFeatures.  # noqa: E501

        zero crossing rate  # noqa: E501

        :return: The zcr of this AudioFeatures.  # noqa: E501
        :rtype: list[float]
        """
        return self._zcr

    @zcr.setter
    def zcr(self, zcr):
        """Sets the zcr of this AudioFeatures.

        zero crossing rate  # noqa: E501

        :param zcr: The zcr of this AudioFeatures.  # noqa: E501
        :type: list[float]
        """
        if zcr is None:
            raise ValueError("Invalid value for `zcr`, must not be `None`")  # noqa: E501

        self._zcr = zcr

    @property
    def energy(self):
        """Gets the energy of this AudioFeatures.  # noqa: E501

        energy  # noqa: E501

        :return: The energy of this AudioFeatures.  # noqa: E501
        :rtype: list[float]
        """
        return self._energy

    @energy.setter
    def energy(self, energy):
        """Sets the energy of this AudioFeatures.

        energy  # noqa: E501

        :param energy: The energy of this AudioFeatures.  # noqa: E501
        :type: list[float]
        """
        if energy is None:
            raise ValueError("Invalid value for `energy`, must not be `None`")  # noqa: E501

        self._energy = energy

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AudioFeatures):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
