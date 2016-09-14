from commentengine.models import MasterComment

from rest_framework import serializers
from rest_framework.compat import six


class MasterCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterComment
