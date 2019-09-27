from django.utils import timezone
from django.db import models, transaction
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator

from sNeeds.apps.account.models import ConsultantProfile

User = get_user_model()

FILE_TYPES = (
    ('file', 'File'),
    ('picture', 'Picture'),
    ('voice', 'Voice'),
)


def get_file_upload_path(instance, filename):
    return "files/chats/{}/{}/{}".format(instance.chat, timezone.datetime.now(), filename)


def get_image_upload_path(instance, filename):
    return "images/chats/{}/{}/{}".format(instance.chat, timezone.datetime.now(), filename)


def get_voice_upload_path(instance, filename):
    return "voices/chats/{}/{}/{}".format(instance.chat, timezone.datetime.now(), filename)


class Chat(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    consultant = models.ForeignKey(ConsultantProfile, null=True, on_delete=models.SET_NULL)


class AbstractMessage(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='+')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if self.sender != self.chat.user and self.sender != self.chat.consultant:
            raise ValidationError("Sender is not user or consultant.")

    class Meta:
        abstract = True


class Message(AbstractMessage):
    message = models.CharField(max_length=2048)


class File(AbstractMessage):
    file = models.FileField(
        upload_to=get_file_upload_path,
    )


class Voice(AbstractMessage):
    file = models.FileField(
        upload_to=get_voice_upload_path,
        validators=[FileExtensionValidator(allowed_extensions=['mp3'])]
    )


class Image(AbstractMessage):
    image = models.ImageField(
        upload_to=get_image_upload_path,
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])]
    )
