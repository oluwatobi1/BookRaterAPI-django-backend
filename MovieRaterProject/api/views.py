from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Movie, Rating
from .serializers import MovieSerializer, RatingSerializer
from rest_framework import viewsets, status
from django.contrib.auth.models import User


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    @action(methods=["POST"], detail=True)
    def rate_movie(self, request, pk=None):
        if 'stars' in request.data:
            movie = Movie.objects.get(id=pk)
            user = User.objects.get(pk=1)
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
                rating = Rating.objects.create(movie=movie.id, user=user.id, stars=stars)
                serializers = RatingSerializer(rating, many=False)
                response = {"message": "Created successful",
                            "result": serializers.data}
                return Response(response, status=status.HTTP_200_OK)

            #do stuff
        else:
            response = {"message": "You need to input stars field"}
            return Response(response, status=status.HTTP_200_OK)


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
