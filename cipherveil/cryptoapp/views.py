from django.shortcuts import render,redirect
from contactapp.models import ContactBook
from .crypto_code import derive_key,encrypt,decrypt
import base64
from decouple import config
from django.contrib import messages

def encryptionkeygenerate(request):
    if request.user.is_authenticated:
        contacts = ContactBook.objects.all()
        if request.method == 'POST':
            selected_tag = request.POST.get('tag')
            password = request.POST.get('password') 
            print("TAG @ENC = ",selected_tag)
            print("PAS @ENC = ",password)
            encryption_key = derive_key(password=password, salt=selected_tag.encode())
            print("1) KEY =",encryption_key,"   END")
            print("KEY @ENC = ",encryption_key)
            encryption_key_str = base64.b64encode(encryption_key).decode('utf-8')
            request.session['encryption_key_str'] = encryption_key_str
            return redirect('messageencrypt')
        return render(request, 'cryptoapp/encryptionkeygenerate.html', {'contacts': contacts})
    else:
        return redirect('signin')


def messageencrypt(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            plaintext = request.POST.get('text', '')
            encryption_key_str = request.session.get('encryption_key_str', None)   
            if encryption_key_str is None:
                return redirect('encryptionkeygenerate')  # Adjust the URL name as needed
            encryption_key = base64.b64decode(encryption_key_str)
            print("2) KEY =",encryption_key,"   END")
            encrypted_text = encrypt(plaintext.encode(), encryption_key)
            print("3) CIPHERTEXT = ",encrypted_text,"   END")
            encrypted_text_str = base64.b64encode(encrypted_text).decode('utf-8')
            request.session['encrypted_text_str'] = encrypted_text_str
            print("4) CIPHERTEXT STR = ",encrypted_text_str,"   END")
            return redirect('steganoencode')
        return render(request, 'cryptoapp/messageencrypt.html')
    else:
        # Redirect to the signin page if the user is not authenticated
        return redirect('signin')


def decryptionkeygenerate(request):
    if request.user.is_authenticated:
        decryption_text_str = request.session.get('decryption_text_str', None)
        if decryption_text_str is None:
            return redirect('steganodecode')  # Adjust the URL name as needed
        user_tag = config('USER_TAG', default='')
        print("USER TAG = ",user_tag)
        if request.method == 'POST':
            password = request.POST.get('password')
            print("TAG @DEC = ",user_tag)
            print("PAS @DEC = ",password)
            decryption_key = derive_key(password=password, salt=user_tag.encode())
            print("8)) KEY =",decryption_key,"   END")
            print("KEY @DEC = ",decryption_key)
            decryption_key_str = base64.b64encode(decryption_key).decode('utf-8')
            request.session['decryption_key_str'] = decryption_key_str
            print("9)) KEY STR=",decryption_key_str,"   END")
            return redirect('messagedecrypt')
        return render(request, 'cryptoapp/decryptionkeygenerate.html', {})
    
    else:
        return redirect('signin')


def messagedecrypt(request):
    if request.user.is_authenticated:
        decryption_text_str = request.session.get('decryption_text_str', None)
        decryption_key_str = request.session.get('decryption_key_str', None)
        print("10)) CIPHERTEXT STR = ",decryption_text_str,"   END")
        print("11)) KEY STR=",decryption_key_str,"   END")
        if decryption_text_str is None or decryption_key_str is None:
            return redirect('steganodecode')  # Adjust the URL name as needed
        decryption_key = base64.b64decode(decryption_key_str)
        decryption_text = base64.b64decode(decryption_text_str)
        print("12)) CIPHERTEXT = ",decryption_text,"   END")
        print("13)) KEY =",decryption_key,"   END")
        decrypted_message = decrypt(decryption_text[28:], decryption_key, decryption_text[12:28], decryption_text[:12])
        print(decrypted_message.decode())
        return render(request, 'cryptoapp/messagedecrypt.html', {'decrypted_message':decrypted_message.decode()})
    else:
        return redirect('signin')