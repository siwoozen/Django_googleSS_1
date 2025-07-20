import os
import random
from django.shortcuts import render
from django.conf import settings

def home_view(request):
    # 미디어 폴더에서 이미지 파일들을 가져오기
    media_images_path = os.path.join(settings.MEDIA_ROOT, 'images')
    
    # 이미지 파일 확장자
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.webp']
    
    # 사용 가능한 이미지 파일들 찾기
    available_images = []
    if os.path.exists(media_images_path):
        for filename in os.listdir(media_images_path):
            if any(filename.lower().endswith(ext) for ext in image_extensions):
                available_images.append(filename)
    
    # 랜덤 이미지 선택 (기본 이미지가 없으면 None)
    random_image = None
    if available_images:
        random_image = random.choice(available_images)
    
    context = {
        'random_image': random_image,
        'available_images': available_images,
    }
    
    return render(request, 'index.html', context) 