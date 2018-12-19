import pandas as pd
import json
import slate3k as slate
import PyPDF2
import re

pdf_Wharf_obj = open('./data/hsie.pdf', 'rb')
pdf_Wharf = PyPDF2.PdfFileReader(pdf_Wharf_obj)
page_Wharf = pdf_Wharf.getPage(1)
a=0