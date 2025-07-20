import os
import random
import json
from django.shortcuts import render
from django.conf import settings

def home_view(request):
    media_images_path = os.path.join(settings.MEDIA_ROOT, 'images')
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.webp']
    
    available_images = []
    if os.path.exists(media_images_path):
        for filename in os.listdir(media_images_path):
            if any(filename.lower().endswith(ext) for ext in image_extensions):
                available_images.append(filename)
    
    random_image = None
    if available_images:
        random_image = random.choice(available_images)

    image_list_json = json.dumps(available_images)
    
    context = {
        'random_image': random_image,
        'image_list_json': image_list_json,
    }
    
    return render(request, 'index.html', context)