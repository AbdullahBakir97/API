from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication
from .models import Team, Player, Match, FantasyTeam, Contest, ContestEntry
from .serializers import TeamSerializer, PlayerSerializer, MatchSerializer, FantasyTeamSerializer, ContestSerializer, ContestEntrySerializer
from .filters import TeamFilter, PlayerFilter, MatchFilter, FantasyTeamFilter, ContestFilter, ContestEntryFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from allauth.account.views import ConfirmEmailView
from allauth.account import app_settings as allauth_settings
from allauth.account.utils import complete_signup
from django.contrib.auth import get_user_model
from dj_rest_auth.views import (
    LoginView, LogoutView, PasswordChangeView,
    PasswordResetView, PasswordResetConfirmView,
)
from dj_rest_auth.registration.serializers import RegisterSerializer
from .serializers import (
    SignupSerializer,
    LoginSerializer,
    ChangePasswordSerializer,
    PasswordResetSerializer,
    PasswordResetConfirmSerializer
)



class SignupAPIView(generics.CreateAPIView):
    """
    View for user registration.
    """
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def perform_create(self, serializer):
        serializer.save(request=self.request)

class LoginAPIView(LoginView):
    """
    View for user login.
    Inherits from dj_rest_auth's LoginView.
    """

class LogoutAPIView(LogoutView):
    """
    View for user logout.
    Inherits from dj_rest_auth's LogoutView.
    """

class PasswordChangeAPIView(PasswordChangeView):
    """
    View for changing password.
    Inherits from dj_rest_auth's PasswordChangeView.
    """

class PasswordResetAPIView(PasswordResetView):
    """
    View for initiating password reset process.
    Inherits from dj_rest_auth's PasswordResetView.
    """

class PasswordResetConfirmAPIView(PasswordResetConfirmView):
    """
    View for confirming password reset process.
    Inherits from dj_rest_auth's PasswordResetConfirmView.
    """
class TeamList(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    filter_class = TeamFilter
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = '__all__'
    search_fields = ['name', 'country']
    pagination_class = PageNumberPagination
    # permission_classes = (IsAuthenticated,)


class TeamDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = (IsAuthenticated,)


class PlayerList(generics.ListCreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    filter_class = PlayerFilter
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = '__all__'
    search_fields = ['name', 'team__name']
    pagination_class = PageNumberPagination
    # permission_classes = (IsAuthenticated,)


class PlayerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    # permission_classes = (IsAuthenticated,)


class MatchList(generics.ListCreateAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
    filter_class = MatchFilter
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = '__all__'
    search_fields = ['team1__name', 'team2__name', 'venue']
    pagination_class = PageNumberPagination
    # permission_classes = (IsAuthenticated,)


class MatchDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
    # permission_classes = (IsAuthenticated,)


class FantasyTeamList(generics.ListCreateAPIView):
    queryset = FantasyTeam.objects.all()
    serializer_class = FantasyTeamSerializer
    filter_class = FantasyTeamFilter
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = '__all__'
    search_fields = ['name', 'user__username']
    pagination_class = PageNumberPagination
    # permission_classes = (IsAuthenticated,)


class FantasyTeamDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FantasyTeam.objects.all()
    serializer_class = FantasyTeamSerializer
    # permission_classes = (IsAuthenticated,)


class ContestList(generics.ListCreateAPIView):
    queryset = Contest.objects.all()
    serializer_class = ContestSerializer
    filter_class = ContestFilter
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = '__all__'
    search_fields = ['name']
    pagination_class = PageNumberPagination
    # permission_classes = (IsAuthenticated,)


class ContestDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contest.objects.all()
    serializer_class = ContestSerializer
    # permission_classes = (IsAuthenticated,)


class ContestEntryList(generics.ListCreateAPIView):
    queryset = ContestEntry.objects.all()
    serializer_class = ContestEntrySerializer
    filter_class = ContestEntryFilter
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = '__all__'
    search_fields = ['user__username', 'contest__name', 'fantasy_team__name']
    pagination_class = PageNumberPagination
    # permission_classes = (IsAuthenticated,)


class ContestEntryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ContestEntry.objects.all()
    serializer_class = ContestEntrySerializer
    # permission_classes = (IsAuthenticated,)
