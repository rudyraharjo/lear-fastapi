from fastapi import APIRouter

route = APIRouter()

@route.post("/create",)
def create_material():
    return {"message": "Create Material"}


@route.get("/",)
def get_material():
    return {"message": "List of Material"}


@route.get("/view",)
def get_detail_material():
    return {"message": "Detail Material"}


@route.put("/update",)
def update_material():
    return {"message": "Update Material"}


@route.delete("/delete",)
def delete_material():
    return {"message": "Delete Material"}
