"""Route for Users"""

# Third party imports


from fastapi import APIRouter


router = APIRouter()
valid_file_types = ["image/png", "image/jpeg", "image/webp"]
