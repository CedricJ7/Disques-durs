from browser import document, ajax

def execute_flask_function():
	ajax.get('http://localhost:5000/', oncomplete=handle_response)

def handle_response(request):
	if request.status == 200:
		document['response'].text = request.text
	else:
		document['response'].text = 'Erreur de requête AJAX'

document['1'].bind('click', lambda evt: execute_flask_function())