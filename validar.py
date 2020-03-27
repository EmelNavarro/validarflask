def validar(request,contrasegna):
	
		xpresionregular=re.compile(r'(([A-Z]{1,1})([1-9]{3,3})([a-z]*)(\W{3,3}))')
		if xpresionregular.match(contrasegna)is not None:
			return HttpResponse("%s, es una contraseña valida" %contrasegna)
		else:
			return HttpResponse("%s, no es una contraseña correcta"%contrasegna)