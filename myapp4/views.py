from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from .forms import ProductForm



def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.cleaned_data['product']
            fs = FileSystemStorage()
            fs.save(product.name, product)
            
    else:
        form = ProductForm()
    return render(request, 'create_product.html', {'form': form})



