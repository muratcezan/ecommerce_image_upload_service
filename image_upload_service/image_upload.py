import os
import uuid
from werkzeug.utils import secure_filename


class ImageUploadService:
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "webp"}
    MAX_SIZE = 2 * 1024 * 1024  # 2 MB

    @classmethod
    def save(cls, file, inst_id: str, image_type: str, base_folder: str = "static/uploads/institutions") -> str:
        """
        Kaydedilecek dosyayı diske yazar ve URL path'ini döner.

        Args:
            file: Flask `request.files['file']` objesi
            inst_id: Kurum ID'si veya klasör adı
            image_type: 'logo', 'banner', 'gallery', vs.
            base_folder: (Opsiyonel) Kök upload klasörü
        """
        if not file or not file.filename:
            raise ValueError("Dosya bulunamadı")

        # Boyut kontrolü
        file.seek(0, os.SEEK_END)
        size = file.tell()
        file.seek(0)
        if size > cls.MAX_SIZE:
            raise ValueError("Dosya boyutu 2 MB'den büyük olamaz")

        # Uzantı kontrolü
        filename = secure_filename(file.filename)
        if "." not in filename:
            raise ValueError("Dosya uzantısı eksik")
        ext = filename.rsplit(".", 1)[-1].lower()
        if ext not in cls.ALLOWED_EXTENSIONS:
            raise ValueError("Desteklenmeyen dosya türü")

        # Klasör oluştur
        folder = os.path.join(base_folder, inst_id)
        os.makedirs(folder, exist_ok=True)

        # Dosya adı üretimi
        unique_name = f"{image_type}_{uuid.uuid4().hex}.{ext}"
        save_path = os.path.join(folder, unique_name)
        file.save(save_path)

        # Web için path dönüşü
        return "/" + save_path.replace("\\", "/")

