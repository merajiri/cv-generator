import pdfkit
from io import BytesIO
from xhtml2pdf import pisa
from django.template import loader
config = pdfkit.configuration(wkhtmltopdf="C:\\wkhtmltox\\bin\\wkhtmltopdf.exe")
def html_to_pdf(template,context={}):
    Template = loader.get_template(template)
    html = Template.render(context)
    # PDF = pdfkit.from_string(html,False,configuration=config)
    # filename="resume.pdf"
    result = BytesIO()
    PDF = pisa.pisaDocument(BytesIO(html.encode("UTF-8")),result)
    return result.getvalue()