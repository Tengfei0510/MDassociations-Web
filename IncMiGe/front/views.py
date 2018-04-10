import os

from django.http import StreamingHttpResponse
from django.shortcuts import render

from .util import query_select_items, query_search_item


# Create your views here.
def index_view(request):
    return render(request, 'front/index.html')


def contact_view(request):
    return render(request, 'front/contact.html')


def search_view(request):
    select_items = query_select_items()
    mirnas = select_items['mirnas']
    lncrnas = select_items['lncrnas']
    genes = select_items['genes'],
    gene_ids = select_items['gene_ids']
    diseases = select_items['diseases']
    new_genes = []
    for gene in genes:
        new_genes.append(gene)

    option_value = request.GET.get('option', None)
    query_value = request.GET.get('query', None)

    data = []
    if option_value is not None and option_value != '' and \
            query_value is not None and query_value != '':

        right_params = True
        query = query_search_item(query_value, option_value.lower())
        if query:
            for d in query:
                temp = dict()
                temp['MiRNA'] = d['MiRNA']
                temp['LncRNA'] = d['LncRNA']
                temp['Gene'] = d['Gene']
                temp['Gene_ID'] = d['Gene_ID']
                temp['Disease_Tissue'] = d['Disease_Tissue']
                temp['Journal'] = d['Journal']
                temp['Title'] = d['Title']
                temp['PubMed_ID'] = d['PubMed_ID']
                temp['Pathway_Name'] = d['Pathway_Name']
                data.append(temp)

    return render(request, 'front/search.html', {
                        'mirnas': mirnas,
                        'lncrnas': lncrnas,
                        'genes': new_genes[0],
                        'gene_ids': gene_ids,
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
