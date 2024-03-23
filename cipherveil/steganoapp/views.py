from django.shortcuts import render, redirect
from django.http import HttpResponse


from PIL import Image
from stegano import lsb
from django.core.files.storage import default_storage
from django.shortcuts import get_object_or_404
from django.conf import settings
import os
import base64

# Create your views here.

def steganoencode(request):
    if request.method == 'POST':
        
        encrypted_text_str = request.session.get('encrypted_text_str', None)
        print("5) CIPHERTEXT STR = ",encrypted_text_str,"   END")
        if encrypted_text_str is None:
            # Redirect to keygenerate if the key is not available
            return redirect('encryptionkeygenerate')  # Adjust the URL name as needed

        
        Encoded_Image_File_Name = request.POST.get('Encoded_Image_File_Name', '')
        image = request.FILES.get('image')

        # Open the image
        img = Image.open(image)

        
        
        encoded_image = lsb.hide(img, encrypted_text_str)

        # Save the encoded image
        Encoded_Image_File_Name = f'{Encoded_Image_File_Name}.png'
        encoded_image_path = f'media/{Encoded_Image_File_Name}'
        encoded_image.save(encoded_image_path)


       

        return render(request, 'steganoapp/steganoencode.html', {'Encoded_Image_File_Name':Encoded_Image_File_Name})

    return render(request, 'steganoapp/steganoencode.html')


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
    
    
    

def steganodecode(request):
    if request.method == 'POST':
        image = request.FILES.get('image')

        # Open the encoded image
        encoded_img = Image.open(image)

        # Retrieve the hidden binary text using LSB
        # binary_text = retrieve_text(encoded_img)

        # Convert binary text to ASCII
        # text = ''.join(chr(int(binary_text[i:i + 8], 2)) for i in range(0, len(binary_text), 8))

        decoded_data = lsb.reveal(encoded_img)
        print("Decoded text = encrypted_text_str @ steganodecode =",decoded_data)
        request.session['decryption_text_str'] = decoded_data
        
        print("6)) CIPHERTEXT STR = ",decoded_data,"   END")
        
        #return render(request, 'steganoapp/steganodecode.html', {'decoded_text': decoded_data})
        return redirect('decryptionkeygenerate')
    return render(request, 'steganoapp/steganodecode.html')
