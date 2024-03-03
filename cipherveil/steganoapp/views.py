from django.shortcuts import render
from django.http import HttpResponse


from PIL import Image
from stegano import lsb
from django.core.files.storage import default_storage
from django.shortcuts import get_object_or_404
from django.conf import settings
import os
# Create your views here.

def encrypt(request):
    if request.method == 'POST':
        text = request.POST.get('text', '')
        Encrypted_Image_File_Name = request.POST.get('Encrypted_Image_File_Name', '')
        image = request.FILES.get('image')

        # Open the image
        img = Image.open(image)


        encrypted_image = lsb.hide(img, text)

        # Save the encrypted image
        Encrypted_Image_File_Name = f'{Encrypted_Image_File_Name}.png'
        encrypted_image_path = f'media/{Encrypted_Image_File_Name}'
        encrypted_image.save(encrypted_image_path)


       

        return render(request, 'steganoapp/encrypt.html', {'Encrypted_Image_File_Name':Encrypted_Image_File_Name})

    return render(request, 'steganoapp/encrypt.html')


def download_image_view(request, image_name):
    # Assuming your images are stored in a folder named 'images' within your media directory
    image_path = os.path.join(settings.MEDIA_ROOT, image_name)

    if os.path.exists(image_path):
        with open(image_path, 'rb') as image_file:
            response = HttpResponse(image_file.read(), content_type='image/png')  # Adjust content type based on your image format
            response['Content-Disposition'] = 'attachment; filename={}'.format(image_name)
            return response
    else:
        return HttpResponse("Image not found", status=404)
    
    
    

def decrypt(request):
    if request.method == 'POST':
        image = request.FILES.get('image')

        # Open the encrypted image
        encrypted_img = Image.open(image)

        # Retrieve the hidden binary text using LSB
        # binary_text = retrieve_text(encrypted_img)

        # Convert binary text to ASCII
        # text = ''.join(chr(int(binary_text[i:i + 8], 2)) for i in range(0, len(binary_text), 8))

        decrypted_data = lsb.reveal(encrypted_img)

        return render(request, 'steganoapp/decrypt.html', {'decrypted_text': decrypted_data})

    return render(request, 'steganoapp/decrypt.html')
