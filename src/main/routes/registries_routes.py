from fastapi import APIRouter, Query, Path
from fastapi.responses import JSONResponse

from src.main.composer.delete_registry_composer import delete_registry_composer
from src.main.composer.get_by_period_composer import get_by_period_composer
from src.main.composer.get_by_period_plate_composer  import get_by_period_plate_composer
from src.main.composer.get_opened_composer import get_opened_composer
from src.main.composer.insert_registry_composer import insert_registry_composer
from src.main.composer.register_exit_composer import register_exit_composer
from src.main.composer.update_registry_composer import upadate_registry_composer
from src.domains.models.registry import Registry

router = APIRouter(
    prefix="/registries",
    tags=["registries"],
    responses={404: {"description": "Not found"}},
)

@router.post('/')
def register_entry(registry: Registry):
    capture = insert_registry_composer()
    response = capture(registry)
    return JSONResponse(status_code=response['status'], content=response['data'])

@router.put('/exit')
def register_exit(car_plate: str = Query(...)):
    capture = register_exit_composer()
    response = capture(car_plate)
    return JSONResponse(status_code=response['status'], content=response['data'])

@router.delete('/delete/{id}')
def delete_registry(
    id: int = Path(..., gt=0, description="Registry ID (must be a positive integer)")
):
    capture = delete_registry_composer()
    response = capture(id)
    return JSONResponse(status_code=response['status'], content=response['data'])

@router.put('/update/{id}')
def update_registry(
    registry: Registry,
    id: int = Path(..., gt=0, description="Registry ID (must be a positive integer)")

):
    capture = upadate_registry_composer()
    response = capture(id,registry)
    return JSONResponse(status_code=response['status'], content=response['data'])

@router.get('/period')
def get_by_period(
    start_date: str = Query(..., description="Start date in YYYY-MM-DD"),
    end_date: str = Query(..., description="End date in YYYY-MM-DD")
):
    capture = get_by_period_composer()
    response = capture(start_date, end_date)
    return JSONResponse(status_code=response['status'], content=response['data'])

@router.get('/search')
def search_registry(
    start_date: str | None = Query(default=None, description="Start date in YYYY-MM-DD"),
    end_date: str | None = Query(default=None, description="End date in YYYY-MM-DD"),
    car_plate: str = ...
):
    capture = get_by_period_plate_composer()
    response = capture(start_date, end_date,car_plate)
    return JSONResponse(status_code=response['status'], content=response['data'])

@router.get('/opened')
def get_opened():
    capture = get_opened_composer()
    response = capture()
    return JSONResponse(status_code=response['status'], content=response['data'])
