from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import get_db
from typing import List

router = APIRouter()

@router.post("/", response_model=schemas.Game)
def create_game(game: schemas.GameCreate, db: Session = Depends(get_db)):
    db_game = models.Game(**game.dict())
    db.add(db_game)
    db.commit()
    db.refresh(db_game)
    return db_game

@router.get("/", response_model=list[schemas.Game])
def read_games(db: Session = Depends(get_db)):
    return db.query(models.Game).all()

@router.put("/{game_id}", response_model=schemas.Game)
def update_game(
    game_id: int = Path(..., title="The ID of the game to update"),
    updated_game: schemas.GameCreate = ...,
    db: Session = Depends(get_db)
):
    game = db.query(models.Game).filter(models.Game.id == game_id).first()
    if not game:
        raise HTTPException(status_code=404, detail="Game not found")
    game.name = updated_game.name
    game.category = updated_game.category
    game.release_date = updated_game.release_date
    game.price = updated_game.price
    db.commit()
    db.refresh(game)
    return game

@router.delete("/{game_id}", status_code=204)
def delete_game(game_id: int, db: Session = Depends(get_db)):
    game = db.query(models.Game).filter(models.Game.id == game_id).first()
    if not game:
        raise HTTPException(status_code=404, detail="Game not found")
    db.delete(game)
    db.commit()
    return
