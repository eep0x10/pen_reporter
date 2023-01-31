#import markdown2  # para converter markdown para HTML
import pdfkit     # para converter HTML para PDF
import io
from markdown2 import markdown
from bs4 import BeautifulSoup
path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

# Leitura do arquivo markdown como entrada
texto = io.open('./topics-out/00-capa.md', mode="r", encoding="utf-8").read()
texto += io.open('./topics-out/01-indice.md', mode="r", encoding="utf-8").read()
texto += io.open('./topics-out/02-infos.md', mode="r", encoding="utf-8").read()
texto += io.open('./topics-out/03-checklist.md', mode="r", encoding="utf-8").read()
texto += io.open('./topics-out/04-historico.md', mode="r", encoding="utf-8").read()
texto += io.open('./topics-out/05-vulnerabilidades.md', mode="r", encoding="utf-8").read()
texto += io.open('./topics-out/06-matriz.md', mode="r", encoding="utf-8").read()
#texto = io.open('./report.md', mode="r", encoding="utf-8")

# Parse da entrada markdown para HTML
html_texto = markdown(texto,True,15,None)


# Html precisa ser mais formatado
formatted_html = BeautifulSoup(html_texto, features="html.parser")
#print(formatted_html)
# Gerando o PDF
pdfkit.from_string(formatted_html.prettify(), 'reportFinal.pdf', configuration=config)

print("Sucesso: Markdown convertido para PDF")