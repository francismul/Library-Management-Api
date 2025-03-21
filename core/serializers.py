from rest_framework import serializers

from .models import Book, Borrow, Return


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class BorrowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrow
        fields = '__all__'
        read_only_fields = ['borrow_date', 'return_date']

    def create(self, validated_date):
        book = validated_date["book"]
        if book.available_copies == 0:
            raise serializers.ValidationError(
                "No copies available for borrowing.")
        return super().create(validated_date)


class ReturnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Return
        fields = '__all__'
        read_only_fields = ['return_date']

    def create(self, validated_date):
        borrow = validated_date["borrow"]
        if borrow.returned:
            raise serializers.ValidationError(
                "Book already returned.")
        return super().create(validated_date)