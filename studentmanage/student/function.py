def handle_uploaded_file(f):
    with open('student/static/adminResources/image/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)