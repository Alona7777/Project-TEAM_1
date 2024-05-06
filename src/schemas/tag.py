from pydantic import BaseModel, Field


class TagModel(BaseModel):
    id: int
    name: str


class TagResponse(TagModel):
    name: str

    class Config:
        from_attributes = True



""" 
додати в class ImageResponse
    tags: List[TagResponse]
    ---
додати в class ImageModel:
    tags: List[str]
"""