from main.models import ToDo

obj = ToDo(text="jeden")
obj.save()

for i in ToDo.objects.all():
    print(i.text)



