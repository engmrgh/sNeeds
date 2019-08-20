from rest_framework import serializers
from .models import TicketMessage

from sNeeds.apps.customAuth.serializers import SafeUserDataSerializer

from .models import Ticket


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = [
            'id',
            'title',
            'user',
            'consultant',
            'created',
        ]

        extra_kwargs = {
            'user': {'read_only': True},
            'created': {'read_only': True},
        }

    def create(self, validated_data):
        request = self.context.get("request")
        user = request.user

        obj = Ticket.objects.create(
            title=validated_data.get('title'),
            user=user,
            consultant=validated_data.get('consultant'),
        )

        return obj


class TicketMessageSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="ticket:ticketMessages-detail", lookup_field='id'
    )
    user = serializers.SerializerMethodField()
    consultant = serializers.SerializerMethodField()

    class Meta:
        model = TicketMessage
        fields = [
            'id',
            'url',
            'ticket',
            'user',
            'consultant',
            'file',
            'text',
        ]

    def get_user(self, obj):
        request = self.context.get("request")
        return SafeUserDataSerializer(
            obj.ticket.user, context={"request": request}
        ).data

    def get_consultant(self, obj):
        request = self.context.get("request")
        return SafeUserDataSerializer(
            obj.ticket.consultant, context={"request": request}
        ).data