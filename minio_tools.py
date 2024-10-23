from pathlib import Path
from minio import Minio

# MinIO client configuration
minio_client = Minio(
    endpoint="",  # Replace with your MinIO server endpoint
    access_key="",  # Replace with your MinIO access key
    secret_key="",  # Replace with your MinIO secret key
    secure=False,
    #    secure=settings.MINIO_USE_SSL,  # Set to True if using HTTPS
    #    http_client=urllib3.PoolManager(
    #        cert_reqs="CERT_REQUIRED",  # Require a valid SSL certificate from the server
    #        ca_certs="ca-certificates.crt",  # Use Mozilla's CA Bundle for verification
    #    ),
)


def save_in_minio(location: Path):
    name = location.name
    try:
        result = minio_client.fput_object(
            "images",  # Name of the bucket
            f"{name}",  # Object name in the bucket
            location,
        )
        return result.object_name
    except Exception as exc:
        return None
