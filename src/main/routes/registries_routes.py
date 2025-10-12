from fastapi import APIRouter, Query, Path
from fastapi.responses import JSONResponse

from src.main.composer.registries_manager import registries_manager_composer
from src.domains.models.registry import Registry

router = APIRouter(
    prefix="/registries",
    tags=["registries"],
    responses={404: {"description": "Not found"}},
)

@router.post('/')
def register_entry(registry: Registry):
    compose = registries_manager_composer()
    response = compose.insert_registry(registry)
    return JSONResponse(status_code=response['status'], content=response['data'])

@router.put('/exit')
def register_exit(plate_car: str = Query(...)):
    compose = registries_manager_composer()
    response = compose.register_exit(plate_car)
    return JSONResponse(status_code=response['status'], content=response['data'])

@router.delete('/delete/{id}')
def delete_registry(
    id: int = Path(..., gt=0, description="Registry ID (must be a positive integer)")
):
    compose = registries_manager_composer()
    response = compose.delete_registry(id)
    return JSONResponse(status_code=response['status'], content=response['data'])

@router.put('/update/{id}')
def update_registry(
    registry: Registry,
    id: int = Path(..., gt=0, description="Registry ID (must be a positive integer)")

):
    compose = registries_manager_composer()
    response = compose.update_registry(id,registry)
    return JSONResponse(status_code=response['status'], content=response['data'])

@router.get('/period')
def get_by_period(
    start_date: str = Query(..., description="Start date in YYYY-MM-DD"),
    end_date: str = Query(..., description="End date in YYYY-MM-DD")
):
    compose = registries_manager_composer()
    response = compose.get_registries_by_period(start_date, end_date)
    return JSONResponse(status_code=response['status'], content=response['data'])

@router.get('/search')
def search_registry(
    start_date: str | None = Query(default=None, description="Start date in YYYY-MM-DD"),
    end_date: str | None = Query(default=None, description="End date in YYYY-MM-DD"),
    plate_car: str = ...
):
    compose = registries_manager_composer()
    response = compose.get_registries_specifics(start_date, end_date,plate_car)
    return JSONResponse(status_code=response['status'], content=response['data'])

@router.get('/opened')
def get_opened():
    compose = registries_manager_composer()
    response = compose.get_opened_registries()
    return JSONResponse(status_code=response['status'], content=response['data'])
