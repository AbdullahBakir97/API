from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated
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

from .serializers import (
    SignupSerializer,
    LoginSerializer,
    ChangePasswordSerializer,
    PasswordResetSerializer,
    PasswordResetConfirmSerializer
)



class SignupAPIView(generics.CreateAPIView):
    serializer_class = SignupSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            if get_user_model().objects.filter(email=email).exists():
                return Response({"error": "Email address already exists"}, status=status.HTTP_400_BAD_REQUEST)
            user = serializer.save(request=self.request)
            return Response({"detail": "Verification e-mail sent"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    # permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # Perform custom authentication logic here if needed
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class LogoutAPIView(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        # Delete the user's authentication token
        request.user.auth_token.delete()
        return Response({"detail": "Successfully logged out."}, status=status.HTTP_200_OK)

class ChangePasswordAPIView(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

class PasswordResetAPIView(generics.CreateAPIView):
    serializer_class = PasswordResetSerializer
    permission_classes = [IsAuthenticated]

class PasswordResetConfirmAPIView(generics.GenericAPIView):
    serializer_class = PasswordResetConfirmSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"detail": "Password has been reset successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
