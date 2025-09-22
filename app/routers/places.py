
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlmodel import Session
from app.database import get_db
from app.schemas.place import PlaceCreate, PlaceRead, PlaceUpdate
from app.services import places as place_service
from app.models.user import User
from app.models.place import Place
from app.utils.deps import get_current_user
import uuid

router = APIRouter()

@router.post("/", response_model=PlaceRead)
def create_place(place: PlaceCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return place_service.create_place(db=db, place=place, owner_id=current_user.id)

@router.get("/", response_model=list[PlaceRead])
def read_places(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = Query(default=10, lte=100),
    sort: str = Query(default="created_at:desc", regex="^\w+:(asc|desc)$"),
):
    return place_service.get_places(db=db, skip=skip, limit=limit, sort=sort)

@router.get("/{place_id}", response_model=PlaceRead)
def read_place(place_id: uuid.UUID, db: Session = Depends(get_db)):
    db_place = place_service.get_place(db, place_id=place_id)
    if db_place is None:
        raise HTTPException(status_code=404, detail="Place not found")
    return db_place

@router.put("/{place_id}", response_model=PlaceRead)
def update_place(
    place_id: uuid.UUID,
    place: PlaceUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    db_place = place_service.get_place(db, place_id=place_id)
    if db_place is None:
        raise HTTPException(status_code=404, detail="Place not found")
    if db_place.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to update this place")
    return place_service.update_place(db=db, place=db_place, updates=place)

@router.delete("/{place_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_place(
    place_id: uuid.UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    db_place = place_service.get_place(db, place_id=place_id)
    if db_place is None:
        raise HTTPException(status_code=404, detail="Place not found")
    if db_place.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to delete this place")
    place_service.delete_place(db=db, place=db_place)
