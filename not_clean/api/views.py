from datetime import datetime, timedelta

import pytz
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

from .serializers import PostSerializer
from blog.models import Post


class ExpiredTokenAuthentication(TokenAuthentication):
    def authenticate_credentials(self, key):
        user, token = super(ExpiredTokenAuthentication, self).authenticate_credentials(key=key)
        utc_now = datetime.utcnow()
        utc_now = utc_now.replace(tzinfo=pytz.utc)
        if token.created + timedelta(minutes=2) < utc_now:
            raise AuthenticationFailed('token has expired')
        return user, token


class PostViewSet(ModelViewSet):
    queryset = Post.objects.filter(is_published=True)
    serializer_class = PostSerializer
    authentication_classes = [ExpiredTokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]


class ExpiredObtainAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        try:
            token = Token.objects.get(user=user)
        except Token.DoesNotExist:
            pass
        else:
            token.delete()
        token = Token(
            user=user,
        )
        token.save()
        return Response({'token': token.key})


expired_obtain_auth_token = ExpiredObtainAuthToken.as_view()
