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
    diseases = select_items['diseases']
    new_genes = []
    for gene in genes:
        new_genes.append(gene)

    req_lncrna = request.GET.get('lncrna', None)
    req_mirna = request.GET.get('mirna', None)
    req_gene = request.GET.get('gene', None)
    req_disease = request.GET.get('disease', None)

    data = []
    query = None
    if req_mirna:
        query = query_search_item(req_mirna, 'MiRNA')
    elif req_lncrna:
        query = query_search_item(req_lncrna, 'LncRNA')
    elif req_gene:
        query = query_search_item(req_gene, 'Gene')
    elif req_disease:
        query = query_search_item(req_disease, 'Disease_Tissue')

    if query:
        for d in query:
            temp = dict()
            temp['MiRNA'] = d['MiRNA']
            temp['LncRNA'] = d['LncRNA']
            temp['Gene'] = d['Gene']
            temp['Disease_Tissue'] = d['Disease_Tissue']
            temp['Journal'] = d['Journal']
            temp['Title'] = d['Title']
            temp['PubMed_ID'] = d['PubMed_ID']
            temp['Pathway_Name'] = d['Pathway_Name']
            data.append(temp)
    return render(request, 'front/search.html',
                  {
                      'mirnas': mirnas,
                      'lncrnas': lncrnas,
                      'genes': new_genes[0],
                      'diseases': diseases,
                      'data': data
                  })


def download(req):
    excel_file_name = 'lncRNA-miRNA-mRNA.xlsx'

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
