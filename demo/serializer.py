from rest_framework import serializers
from .models import Book, BookNumber, Character, Author

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model=Character
        fields=['name', 'book']

class BookNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookNumber
        fields = ['id', 'isbn_10', 'isbn_13']


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Author
        fields=['first_name', 'id', 'last_name']

class BookSerializer(serializers.ModelSerializer):
    number = BookNumberSerializer(many=False)
    characters=CharacterSerializer(many=True)
    authors = AuthorSerializer(many=True)
    class Meta:
        model = Book
        fields = ['id', 'title', 'description', 'price', 'is_published', 'number',
                    'characters', 'authors']


class BookMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model= Book
        fields = ['id', 'title']
