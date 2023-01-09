from types import NoneType
from utils.custom_pdf import PDF
from services.firestore_services import get_assignment_form, get_assignment_response


form = get_assignment_form('20230611427')
response = get_assignment_response('20230611427')

if type(response) == NoneType:
    response = {}

pdf = PDF();

pdf.create_pdf(form=form, response=response)
pdf.output('output.pdf')