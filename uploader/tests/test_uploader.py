from io import BytesIO
from unittest.mock import patch

import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import RequestFactory
from PIL import Image

from uploader.views import upload_form_view


@pytest.mark.django_db(True)
class TestUploader:
    def test_upload_form_view_success(self):
        image_file = self.create_mock_image()
        uploaded_image = SimpleUploadedFile(
            name="test_image.png", content=image_file.read(), content_type="image/png"
        )
        data = {"mail": "test@mail.com", "file": uploaded_image}
        with patch("uploader.views.async_task") as mock_async:
            factory = RequestFactory()
            request = factory.post("/", data)
            response = upload_form_view(request)
            assert mock_async.call_count == 1
            assert response.status_code == 302
            assert response.url == "/success/"

    def create_mock_image(self):
        image_file = BytesIO()
        image = Image.new("RGBA", size=(100, 100), color=(155, 0, 0))
        image.save(image_file, "png")
        image_file.seek(0)
        return image_file
