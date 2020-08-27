# coding: utf-8

"""
    Argo

    Python client for Argo Workflows  # noqa: E501

    The version of the OpenAPI document: 2.10.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from argo.workflows.client.configuration import Configuration


class V1alpha1CronWorkflowStatus(object):
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
        'active': 'list[V1ObjectReference]',
        'conditions': 'list[V1alpha1Condition]',
        'last_scheduled_time': 'datetime'
    }

    attribute_map = {
        'active': 'active',
        'conditions': 'conditions',
        'last_scheduled_time': 'lastScheduledTime'
    }

    def __init__(self, active=None, conditions=None, last_scheduled_time=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha1CronWorkflowStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._active = None
        self._conditions = None
        self._last_scheduled_time = None
        self.discriminator = None

        if active is not None:
            self.active = active
        if conditions is not None:
            self.conditions = conditions
        if last_scheduled_time is not None:
            self.last_scheduled_time = last_scheduled_time

    @property
    def active(self):
        """Gets the active of this V1alpha1CronWorkflowStatus.  # noqa: E501

        Active is a list of active workflows stemming from this CronWorkflow  # noqa: E501

        :return: The active of this V1alpha1CronWorkflowStatus.  # noqa: E501
        :rtype: list[V1ObjectReference]
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this V1alpha1CronWorkflowStatus.

        Active is a list of active workflows stemming from this CronWorkflow  # noqa: E501

        :param active: The active of this V1alpha1CronWorkflowStatus.  # noqa: E501
        :type: list[V1ObjectReference]
        """

        self._active = active

    @property
    def conditions(self):
        """Gets the conditions of this V1alpha1CronWorkflowStatus.  # noqa: E501

        Conditions is a list of conditions the CronWorkflow may have  # noqa: E501

        :return: The conditions of this V1alpha1CronWorkflowStatus.  # noqa: E501
        :rtype: list[V1alpha1Condition]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this V1alpha1CronWorkflowStatus.

        Conditions is a list of conditions the CronWorkflow may have  # noqa: E501

        :param conditions: The conditions of this V1alpha1CronWorkflowStatus.  # noqa: E501
        :type: list[V1alpha1Condition]
        """

        self._conditions = conditions

    @property
    def last_scheduled_time(self):
        """Gets the last_scheduled_time of this V1alpha1CronWorkflowStatus.  # noqa: E501

        LastScheduleTime is the last time the CronWorkflow was scheduled  # noqa: E501

        :return: The last_scheduled_time of this V1alpha1CronWorkflowStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._last_scheduled_time

    @last_scheduled_time.setter
    def last_scheduled_time(self, last_scheduled_time):
        """Sets the last_scheduled_time of this V1alpha1CronWorkflowStatus.

        LastScheduleTime is the last time the CronWorkflow was scheduled  # noqa: E501

        :param last_scheduled_time: The last_scheduled_time of this V1alpha1CronWorkflowStatus.  # noqa: E501
        :type: datetime
        """

        self._last_scheduled_time = last_scheduled_time

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
        if not isinstance(other, V1alpha1CronWorkflowStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1CronWorkflowStatus):
            return True

        return self.to_dict() != other.to_dict()
