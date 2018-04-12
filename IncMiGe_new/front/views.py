import os

from django.http import StreamingHttpResponse
from django.shortcuts import render

#from .util import query_select_items, query_search_item
from .models import LncCeRBase

# Create your views here.
def index_view(request):
    return render(request, 'front/index.html')


def contact_view(request):
    return render(request, 'front/contact.html')


def search(request):
    return render(request, 'front/search_page.html')

def search_view(request):
    select_items = LncCeRBase.objects.all()
    mirnas = select_items.order_by('mirnas').values('mirnas').distinct()
    lncrnas = select_items.order_by('lncrnas').values('lncrnas').distinct()
    genes = select_items.order_by('genes').values('genes').distinct()
    #gene_ids = select_items.order_by('gene_ids').values('gene_ids').distinct()
    diseases = select_items.order_by('diseases').values('diseases').distinct()
    option_value = request.GET.get('option', None)
    query_value = request.GET.get('query', None)
    data = {}
    if option_value and query_value:

        right_params = True
        if option_value == "MiRNA":
            query = select_items.filter(mirnas=query_value)
        elif option_value == "LncRNA":
            query = select_items.filter(lncrnas=query_value)
        elif option_value == "Gene":
            query = select_items.filter(gene_ids__contains=query_value)
        elif option_value == "Disease":
            query = select_items.filter(diseases=query_value)
        else:
            query = None
        if query:
            data = query
    return render(request, 'front/search.html', {
                        'mirnas': mirnas,
                        'lncrnas': lncrnas,
                        'genes': genes,
                        'diseases': diseases,
                        'data': data
                    })


def download(request):
    p = request.GET.get('p', None)
    if p == 'page':
        return render(request, 'front/download.html')
    else:
        excel_file_name = 'lncRNA-miRNA-mRNA_assciations.xlsx'

        def file_iterator(file_name, chunk_size=512):
            with open(file_name, 'rb') as f:
                while True:
                    c = f.read(chunk_size)
                    if c:
                        yield c
                    else:
                        break
                f.close()

        dir_path = os.path.dirname(os.path.realpath(__file__))
        the_file_name = dir_path + '/' + excel_file_name
        response = StreamingHttpResponse(file_iterator(the_file_name))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="{0}"'.format(excel_file_name)
        return response


def links(request):

    return render(request, 'front/links.html')
