#coding:utf-8
import xlrd
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE","IncMiGe.settings")

if django.VERSION >= (1, 7):
    django.setup()

def main():
    from front.models import LncCeRBase
    bk = xlrd.open_workbook('1.xls')
    sh = bk.sheet_by_name('Sheet1')
    nrows = sh.nrows
    for i in range(1,nrows):
        print("正在导入第",i,"条数据......")
        lncrnas = sh.cell_value(i, 0)
        mirnas = sh.cell_value(i, 1)
        genes = sh.cell_value(i, 2)
        gene_ids = sh.cell_value(i, 3)
        pathway_name = sh.cell_value(i, 4)
        diseases = sh.cell_value(i, 5)
        Description = sh.cell_value(i, 6)
        try:
            PubMed_ID = str(int(sh.cell_value(i, 7)))
        except:
            PubMed_ID = str(sh.cell_value(i, 7))
        Year = int(sh.cell_value(i, 8))
        Journal = sh.cell_value(i, 9)
        Title = sh.cell_value(i, 10)
        LncCeRBase.objects.get_or_create(lncrnas=lncrnas, mirnas=mirnas, genes=genes, gene_ids=gene_ids, pathway_name=pathway_name,
                                         diseases=diseases,Description=Description, PubMed_ID=PubMed_ID, Year=Year,
                                         Journal=Journal,Title=Title)

if __name__ == "__main__":
    main()
    print ('done!')

