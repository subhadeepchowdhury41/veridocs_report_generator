from .firebase import db

def get_assignment_response(id):
    response_ref = db.collection('assignments').document(id).collection('form_data').document('response')
    response = response_ref.get()
    return response.to_dict()

def get_assignment_form(id):
    form_ref = db.collection('assignments').document(id).collection('form_data').document('data')
    form = form_ref.get()
    return form.to_dict()