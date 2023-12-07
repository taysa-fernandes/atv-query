from django.shortcuts import render
from .models import Book, Author, Tag, Review,Profile
from django.db.models import Count



def query_examples(request):
    # Consulta simples com filter
    books_by_title = Book.objects.filter(title__icontains='teste')

    # Consulta com lookup para buscar autores por nome
    authors_by_name = Author.objects.filter(name__icontains='nome do autor')

    # Consulta many-to-many (livros com uma determinada tag)
    books_with_tag = Book.objects.filter(tags__name='nome da tag')

    # Consulta com relacionamento reverso (todos os livros de um autor)
    books_of_author = Book.objects.filter(author__name='nome do autor')

    # Consulta agregada (por exemplo, número de livros de um autor)
    num_books_of_author = Book.objects.filter(author__name='nome do autor').count()

    # Envie todas as consultas para o template
    context = {
        'books_by_title': books_by_title,
        'authors_by_name': authors_by_name,
        'books_with_tag': books_with_tag,
        'books_of_author': books_of_author,
        'num_books_of_author': num_books_of_author,
    }

    return render(request, 'core/teste1.html', context)
def questao01(request):
    books_of_author = Book.objects.filter(author__name = 'Larissa Moura')
    
    context = {
        'books_of_author': books_of_author,
    }
    return render(request, 'core/q1.html', context)
def questao02(request):
    books_with_tag = Book.objects.filter(tags__name='Educação')
    
    context = {
        'books_with_tag': books_with_tag
    }
    return render(request, 'core/q2.html', context)
def questao03(request):
    author_with_bio = Author.objects.filter(bio__icontains='Quo')
    
    context = {
        'author_with_bio': author_with_bio
    }
    return render(request, 'core/q3.html', context)
def questao04(request):
    num_books_of_assessment = Review.objects.filter(rating__gte=4)
    context ={
        'num_books_of_assessment': num_books_of_assessment
    }
    return render(request, 'core/q4.html', context)
def questao05(request):
    user_profile_with_specific_websites = Profile.objects.filter(website__iexact='http://viana.net/')
    context = {
        'user_profile': user_profile_with_specific_websites
    }
    return render(request, 'core/q5.html', context)
def questao06(request):
    list_books_without_reviews = Review.objects.filter(rating__isnull=True)
    context = {
        'list_books_without_reviews': list_books_without_reviews
    }
    return render(request, 'core/q6.html', context)
def questao07(request):
    authors_with_the_largest_number_of_books = Author.objects.annotate(num_books=Count('books')).order_by('-num_books')
    context = {
        'authors': authors_with_the_largest_number_of_books 
    }
    return render(request, 'core/q7.html', context)
def questao08(request):
    books = Book.objects.all()
    books_with_long_summaries = []

    for book in books:
        words_in_summary = book.summary.split()  
        if len(words_in_summary) > 150:  
            books_with_long_summaries.append(book)

    context = {
        'books_with_long_summaries': books_with_long_summaries
    }
    return render(request, 'core/q8.html', context)
def questao09(request):
    reviews_of_author_books = Review.objects.filter(book__author__name='Larissa Moura')
    
    context = {
        'reviews_of_author_books': reviews_of_author_books,
    }
    return render(request, 'core/q9.html', context)
def questao10(request):
    tag_names = ['Ficção', 'Ciência']

    books_with_specific_tags = Book.objects.filter(tags__name__in=tag_names).annotate(tag_count=Count('tags')).filter(tag_count=len(tag_names))

    context = {
        'books_with_specific_tags': books_with_specific_tags,
    }
    return render(request, 'core/q10.html', context)