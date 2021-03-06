from rest_framework import serializers

from .models import Message
from .models import Ticket
from .custom_serializer import ConsultantFieldSerializer, UserFilteredPrimaryKeyRelatedField

from sNeeds.apps.customAuth.serializers import SafeUserDataSerializer
from sNeeds.apps.account.serializers import ShortConsultantProfileSerializer
from sNeeds.apps.account.models import ConsultantProfile


class TicketSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    consultant = ConsultantFieldSerializer()
    url = serializers.HyperlinkedIdentityField(
        view_name="tickets:ticket-detail", lookup_field='id'
    )

    class Meta:
        model = Ticket
        fields = [
            'id',
            'url',
            'title',
            'user',
            'consultant',
            'created',
        ]

        extra_kwargs = {
            'user': {'read_only': True},
            'created': {'read_only': True},
            'url': {'read_only': True},
        }

    def get_user(self, obj):
        request = self.context.get("request")
        return SafeUserDataSerializer(
            obj.user, context={"request": request}
        ).data

    def create(self, validated_data):
        request = self.context.get("request")
        user = request.user

        obj = Ticket.objects.create(
            title=validated_data.get('title'),
            user=user,
            consultant=validated_data.get('consultant'),
        )

        return obj


class MessageSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    consultant = serializers.SerializerMethodField()
    ticket = UserFilteredPrimaryKeyRelatedField(queryset=Ticket.objects.all())
    url = serializers.HyperlinkedIdentityField(
        view_name="tickets:message-detail", lookup_field='id'
    )
    is_consultant = serializers.SerializerMethodField()


    class Meta:
        model = Message
        fields = [
            'id',
            'url',
            'ticket',
            'user',
            'consultant',
            'file',
            'text',
            'created',
            'is_consultant'
        ]


    def get_user(self, obj):
        request = self.context.get("request")
        return SafeUserDataSerializer(
            obj.ticket.user, context={"request": request}
        ).data

    def get_consultant(self, obj):
        request = self.context.get("request")
        return ShortConsultantProfileSerializer(
            obj.ticket.consultant, context={"request": request}
        ).data

    def get_is_consultant(self, obj):
        sender = obj.sender
        return ConsultantProfile.objects.filter(user=sender).count() > 0

    def create(self, validated_data):
        message = super(MessageSerializer, self).create(validated_data)
        message.sender = self.context.get("request").user
        message.save()
        return message
