from minio import Minio
from settings.config import settings

# Initialize MinIO client
minio_client = Minio(
    settings.MINIO_ENDPOINT,
    access_key=settings.MINIO_ACCESS_KEY,
    secret_key=settings.MINIO_SECRET_KEY,
    secure=settings.MINIO_USE_SSL
)

def upload_profile_picture(file_data, file_name):
    """
    Uploads a profile picture to MinIO.

    Args:
        file_data (bytes): File content to upload.
        file_name (str): Name of the file.

    Returns:
        str: URL to the uploaded file.

    Raises:
        ValueError: If the file type is unsupported.
    """
    # Validate file type
    allowed_extensions = {"jpg", "jpeg", "png", "gif"}
    file_extension = file_name.split(".")[-1].lower()
    if file_extension not in allowed_extensions:
        raise ValueError("Unsupported file type")

    # Upload the file
    minio_client.put_object(
        settings.MINIO_BUCKET_NAME,
        file_name,
        file_data,
        length=-1,
        part_size=10 * 1024 * 1024
    )

    # Return the file URL
    return f"{settings.MINIO_ENDPOINT}/{settings.MINIO_BUCKET_NAME}/{file_name}"


def get_profile_picture_url(file_name):
    """
    Generates a presigned URL for a profile picture.

    Args:
        file_name (str): Name of the file.

    Returns:
        str: Presigned URL for the file.
    """
    return minio_client.get_presigned_url('GET', settings.MINIO_BUCKET_NAME, file_name)
