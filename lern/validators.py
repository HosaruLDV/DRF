from rest_framework import serializers


class YouTubeLinkValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if 'https://www.youtube.com' in value.get('view_link'):
            return True
        else:
            raise serializers.ValidationError('Eto ne ssilka na YT')
