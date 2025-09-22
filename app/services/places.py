
from sqlmodel import Session, select
from app.models.place import Place
from app.schemas.place import PlaceCreate, PlaceUpdate
import uuid

def create_place(db: Session, place: PlaceCreate, owner_id: uuid.UUID) -> Place:
    db_place = Place(**place.dict(), owner_id=owner_id)
    db.add(db_place)
    db.commit()
    db.refresh(db_place)
    return db_place

def get_place(db: Session, place_id: uuid.UUID) -> Place | None:
    return db.get(Place, place_id)

def get_places(
    db: Session, skip: int = 0, limit: int = 10, sort: str = "created_at:desc"
) -> list[Place]:
    sort_field, sort_order = sort.split(":")
    query = select(Place)

    if sort_order == "desc":
        query = query.order_by(getattr(Place, sort_field).desc())
    else:
        query = query.order_by(getattr(Place, sort_field).asc())

    return db.exec(query.offset(skip).limit(limit)).all()

def update_place(
    db: Session, place: Place, updates: PlaceUpdate
) -> Place:
    update_data = updates.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(place, key, value)
    db.add(place)
    db.commit()
    db.refresh(place)
    return place

def delete_place(db: Session, place: Place):
    db.delete(place)
    db.commit()
