from django.shortcuts import render
from django.http import JsonResponse
from .models import Book
from firebase_admin import exceptions
import firebase_admin
from firebase_admin import db, credentials
import json
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404

@csrf_exempt
def insert_book(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        titulo = data.get('titulo')
        autor = data.get('autor')
        paginas = data.get('paginas')
        ano = data.get('ano')

        if not titulo or not autor or not paginas or not ano:
            return JsonResponse({'error': 'Dados inválidos'}, status=400)

        try:
            paginas = int(paginas)
            ano = int(ano)
        except ValueError:
            return JsonResponse({'error': 'Páginas e Ano precisam ser números inteiros'}, status=400)

        book = Book(titulo=titulo, autor=autor, paginas=paginas, ano=ano)
        book.save()

        try:
            ref = db.reference(f'/Books/{book.id}')
            ref.set({
                'titulo': book.titulo,
                'autor': book.autor,
                'paginas': book.paginas,
                'ano': book.ano,
            })
            print("Dados do livro salvos no Realtime Database com sucesso!")
        except exceptions.FirebaseError as e:
            print(f"Erro ao salvar dados no Realtime Database: {e}")
            return JsonResponse({'error': f'Erro ao salvar no Firebase: {e}'}, status=500)

        return JsonResponse({'message': 'Livro criado com sucesso'}, status=201)
    else:
        return JsonResponse({'error': 'Método não permitido'}, status=405)

def read_books(request, book_id=None):
    if book_id:
        # Retorna os dados de um livro específico
        try:
            livro = Book.objects.get(id=book_id)
            data = {
                'id': livro.id,
                'titulo': livro.titulo,
                'autor': livro.autor,
                'paginas': livro.paginas,
                'ano': livro.ano
            }
            return JsonResponse(data, status=200)
        except Book.DoesNotExist:
            return JsonResponse({'error': 'Livro não encontrado'}, status=404)
    else:
        # Retorna todos os livros (ou filtra por autor)
        autor = request.GET.get('autor')  # Obtém o parâmetro 'autor' da URL
        ref = db.reference('/Books/')
        livros = ref.get()

        if livros:
            livros_list = [{'id': livro_id, **livro_data} for livro_id, livro_data in livros.items()]

            if autor:  # Filtra os livros pelo autor, se o parâmetro 'autor' foi fornecido
                livros_list = [livro for livro in livros_list if autor.lower() in livro['autor'].lower()]

            return JsonResponse(livros_list, safe=False)
        else:
            return JsonResponse([], safe=False)
@csrf_exempt
def update_book(request, book_id):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            titulo = data.get('titulo')
            autor = data.get('autor')
            paginas = data.get('paginas')
            ano = data.get('ano')

            # Verifica se todos os campos foram fornecidos
            if not titulo or not autor or not paginas or not ano:
                return JsonResponse({'error': 'Todos os campos são obrigatórios'}, status=400)

            # Converte páginas e ano para inteiros
            try:
                paginas = int(paginas)
                ano = int(ano)
            except ValueError:
                return JsonResponse({'error': 'Páginas e Ano devem ser números inteiros'}, status=400)

            # Busca o livro pelo ID
            try:
                book = Book.objects.get(id=book_id)
            except Book.DoesNotExist:
                return JsonResponse({'error': 'Livro não encontrado'}, status=404)

            # Atualiza os dados do livro
            book.titulo = titulo
            book.autor = autor
            book.paginas = paginas
            book.ano = ano
            book.save()

            # Atualiza os dados no Firebase (se estiver usando)
            try:
                ref = db.reference(f'/Books/{book.id}')
                ref.set({
                    'titulo': book.titulo,
                    'autor': book.autor,
                    'paginas': book.paginas,
                    'ano': book.ano,
                })
                print("Dados do livro atualizados no Firebase com sucesso!")
            except Exception as e:
                print(f"Erro ao atualizar dados no Firebase: {e}")

            return JsonResponse({'message': 'Livro atualizado com sucesso'}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Método não permitido'}, status=405)
    
@csrf_exempt
def delete_book(request, book_id):
    if request.method == 'DELETE':
        try:
            # Busca o livro pelo ID
            book = Book.objects.get(id=book_id)
            book.delete()

            # Remove o livro do Firebase (se estiver usando)
            try:
                ref = db.reference(f'/Books/{book_id}')
                ref.delete()
                print("Livro removido do Firebase com sucesso!")
            except Exception as e:
                print(f"Erro ao remover livro do Firebase: {e}")

            return JsonResponse({'message': 'Livro removido com sucesso'}, status=200)
        except Book.DoesNotExist:
            return JsonResponse({'error': 'Livro não encontrado'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Método não permitido'}, status=405)
