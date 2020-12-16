from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from .models import Movie, Rating
from .serializers import MovieSerializer, RatingSerializer, UserSerializer
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (AllowAny, )



class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    @action(methods=["POST"], detail=True)
    def rate_movie(self, request, pk=None):
        if 'stars' in request.data:
            movie = Movie.objects.get(id=pk)
            user = request.user
            print('user ', user)
            stars = request.data['stars']
            try:
                rating = Rating.objects.get(movie=movie.id, user=user.id)
                rating.stars = stars
                rating.save()
                serializers = RatingSerializer(rating, many=False)
                response = {"message": "Update successful",
                            "result": serializers.data}
                return Response(response, status=status.HTTP_200_OK)

            except:
                rating = Rating.objects.create(movie=movie, user=user, stars=stars)
                serializers = RatingSerializer(rating, many=False)
                response = {"message": "Created successful",
                            "result": serializers.data}
                return Response(response, status=status.HTTP_200_OK)


        else:
            response = {"message": "You need to input stars field"}
            return Response(response, status=status.HTTP_200_OK)


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated,)
