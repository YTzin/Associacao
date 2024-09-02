from django.shortcuts import render, redirect
from django.http import HttpResponse
from usuarios.models import Usuario
from .models import Pessoas
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from io import BytesIO
import urllib.parse
from django.shortcuts import render, get_object_or_404
from .models import Pessoas, Dependentes, Conjuge
from . forms import CadastroPessoa, FormConjuge, FormDependente



def home(request):
    form = CadastroPessoa()
    pessoas = Pessoas.objects.all()
    return render(request, 'home.html', {'pessoas': pessoas , 'form': form} )
    


def ver_pessoa(request, id):
    pessoas = Pessoas.objects.get(id = id)
    return render(request, 'ver_pessoa.html', {'pessoa': pessoas})


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return result.getvalue()
    return None

def gerar_pdf_pessoa(request, pessoa_id):
    pessoa = Pessoas.objects.get(id=pessoa_id)
    context = {'pessoa': pessoa}
    pdf = render_to_pdf('ver_pessoa.html', context)
    
    if pdf:
        # Cria um nome de arquivo seguro para o PDF
        nome_arquivo = f'{urllib.parse.quote(pessoa.nome)}.pdf'
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{nome_arquivo}"'
        return response
    
    return HttpResponse("Error generating PDF", status=500)




def detalhes_pessoa(request, id):
    pessoa = get_object_or_404(Pessoas, id=id)
    return render(request, 'detalhes_pessoa.html', {'pessoa': pessoa})



def filtar_pessoa(request):
    search_query = request.GET.get('search_query', '')

    if search_query:
        pessoas = Pessoas.objects.filter(nome__icontains=search_query)
    else:
        pessoas = Pessoas.objects.all()

    context = {
        'pessoas': pessoas,
        'search_query': search_query,
    }
    
    return render(request, 'home.html', context)

def cadastrar_pessoa(request):
    if request.method == 'POST':
        form = CadastroPessoa(request.POST)
        
        if form.is_valid():
            # Aqui você pode salvar o formulário ou realizar outra ação
            form.save()
            return HttpResponse('success_url')  # Redirecionar para uma URL de sucesso ou outra página
        else:
            return HttpResponse('Formulário inválido', status=400)
    
    else:
        form = CadastroPessoa()
    
    return render(request, 'cadastrar_pessoa.html', {'form': form})


def adicionar_conjuge(request):
    if request.method == 'POST':
        form = FormConjuge(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # ou outra URL apropriada
    else:
        form = FormConjuge()
    return HttpResponse('erro')

def adicionar_dependente(request):
    if request.method == 'POST':
        form = FormDependente(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # ou outra URL apropriada
    else:
        form = FormDependente()
    return HttpResponse("erro")
