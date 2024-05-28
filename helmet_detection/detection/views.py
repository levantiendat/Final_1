from django.shortcuts import render
from django.http import HttpResponse
from .forms import UploadImageForm
import cv2
from PIL import Image
import numpy as np

def detect_objects(image):
    # Đặt logic xử lý detection tại đây
    # Ví dụ đơn giản sử dụng OpenCV để chuyển hình ảnh thành grayscale
    image_np = np.array(image)
    gray_image = cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)
    return gray_image

def upload_image(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            image = Image.open(image)
            processed_image = detect_objects(image)
            # Chuyển đổi lại thành Image để hiển thị
            processed_image = Image.fromarray(processed_image)
            response = HttpResponse(content_type="image/png")
            processed_image.save(response, "PNG")
            return response
    else:
        form = UploadImageForm()
    return render(request, 'upload_image.html', {'form': form})