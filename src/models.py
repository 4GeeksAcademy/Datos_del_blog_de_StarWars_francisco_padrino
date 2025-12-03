from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "User"

    ID: Mapped[int] = mapped_column(primary_key=True)
    Favotite: Mapped["Favotite"] = relationship(back_populates="User")
    username: Mapped[str] = mapped_column(
        String(75), index=True, nullable=False)
    firstname: Mapped[str] = mapped_column(
        String(75), unique=False, nullable=False)
    lastname: Mapped[str] = mapped_column(unique=False, nullable=False)
    email: Mapped[str] = mapped_column(String(75), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(
        String(100), unique=True, nullable=False)
    phone: Mapped[str] = mapped_column(String(75), unique=True, nullable=False)

    def serialize(self):
        return {
            "ID": self.ID,
            "username": self.username,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email,
            "password": self.password,
            "phone": self.phone

        }


class Favotite(db.Model):
    __tablename__ = "Favotite"

    ID: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("User.ID"))
    user: Mapped["User"] = relationship(back_populates="Favotite")
    films_id: Mapped[int] = mapped_column(ForeignKey("Films.ID"))
    Films: Mapped["Films"] = relationship(back_populates="Favotite")
    people_id: Mapped[int] = mapped_column(ForeignKey("People.ID"))
    people: Mapped["People"] = relationship(back_populates="Favotite")
    species_id: Mapped[int] = mapped_column(unique=False, nullable=False)
    starships_id: Mapped[int] = mapped_column(ForeignKey("Starship.ID"))
    starship: Mapped["Starship"] = relationship(back_populates="Favotite")
    planets_id: Mapped[int] = mapped_column(ForeignKey("Planet.ID"))
    planet: Mapped["Planet"] = relationship(back_populates="Favotite")

    def serialize(self):
        return {
            "ID": self.ID,
            "user_id": self.user_id,
            "films_id": self.films_id,
            "people_id": self.people_id,
            "species_id": self.species_id,
            "starships_id": self.starships_id
        }


class Films(db.Model):
    __tablename__ = "Films"

    ID: Mapped[int] = mapped_column(primary_key=True)
    films_id: Mapped["Films"] = relationship(back_populates="Favotite")

    charatecrs: Mapped[str] = mapped_column(
        String(300), unique=True, nullable=False)
    creacted: Mapped[str] = mapped_column(
        String(75), unique=True, nullable=False)
    director: Mapped[str] = mapped_column(
        String(75), unique=True, nullable=False)
    episode: Mapped[str] = mapped_column(
        String(10), unique=True, nullable=False)
    opening_crawl: Mapped[str] = mapped_column(
        String(30), unique=True, nullable=False)
    people_id: Mapped[int] = mapped_column(ForeignKey("People.ID"))
    people: Mapped["People"] = relationship(back_populates="Films")
    planets: Mapped[str] = mapped_column(
        String(300), unique=True, nullable=False)
    planets_id: Mapped[int] = mapped_column(ForeignKey("Planet.ID"))
    planet: Mapped["Planet"] = relationship(back_populates="Films")
    producer: Mapped[str] = mapped_column(
        String(10), unique=True, nullable=False)
    release_date: Mapped[str] = mapped_column(
        String(30), unique=True, nullable=False)
    species: Mapped[str] = mapped_column(
        String(300), unique=True, nullable=False)
    species_id: Mapped[int] = mapped_column(unique=False, nullable=False)
    starships: Mapped[str] = mapped_column(
        String(300), unique=True, nullable=False)
    starships_id: Mapped[int] = mapped_column(ForeignKey("Starship.ID"))
    starship: Mapped["Starship"] = relationship(back_populates="Films")
    title: Mapped[str] = mapped_column(
        String(150), unique=True, nullable=False)

    def serialize(self):
        return {
            "ID": self.ID,
            "charatecrs": self.charatecrs,
            "creacted": self.creacted,
            "director": self.director,
            "episode": self.episode,
            "opening_crawl": self.opening_crawl,
            "people_id": self.people_id,
            "planets": self.planets,
            "planets_id": self.planets_id,
            "producer": self.producer,
            "release_date": self.release_date,
            "species": self.species,
            "species_id": self.species_id,
            "starships": self.starships,
            "starships_id": self.starships_id,
            "title": self.title
        }


class People(db.Model):
    __tablename__ = "People"

    ID: Mapped[int] = mapped_column(primary_key=True)
    favotite: Mapped["Favotite"] = relationship(back_populates="People")
    films: Mapped["Films"] = relationship(back_populates="People")
    birth_year: Mapped[str] = mapped_column(
        String(25), unique=True, nullable=False)
    creacted: Mapped[str] = mapped_column(
        String(100), unique=True, nullable=False)
    eye_color: Mapped[str] = mapped_column(
        String(10), unique=True, nullable=False)
    Films: Mapped[str] = mapped_column(
        String(500), unique=True, nullable=False)
    gender: Mapped[str] = mapped_column(
        String(15), unique=True, nullable=False)
    heir_color: Mapped[str] = mapped_column(
        String(25), unique=True, nullable=False)
    height: Mapped[str] = mapped_column(
        String(25), unique=True, nullable=False)
    homeworld: Mapped[str] = mapped_column(
        String(250), unique=True, nullable=False)
    skin_color: Mapped[str] = mapped_column(
        String(25), unique=True, nullable=False)
    species: Mapped[str] = mapped_column(
        String(300), unique=True, nullable=False)
    starships: Mapped[int] = mapped_column(
        String(500), unique=True, nullable=False)
    url: Mapped[str] = mapped_column(
        String(500), unique=True, nullable=False)

    def serialize(self):
        return {
            "ID": self.ID,
            "birth_year": self.birth_year,
            "creacted": self.creacted,
            "eye_color": self.eye_color,
            "Films": self.Films,
            "gender": self.gender,
            "heir_color": self.heir_color,
            "height": self.height,
            "homeworld": self.homeworld,
            "skin_color": self.skin_color,
            "species": self.species,
            "starships": self.starships,
            "url": self.url
        }


class Starship(db.Model):
    __tablename__ = "Starship"

    ID: Mapped[int] = mapped_column(primary_key=True)
    favotite: Mapped["Favotite"] = relationship(back_populates="Starship")
    films: Mapped["Films"] = relationship(back_populates="Starship")

    MGLT: Mapped[str] = mapped_column(
        String(25), unique=True, nullable=False)
    cargo_capacity: Mapped[str] = mapped_column(
        String(50), unique=True, nullable=False)
    consumable: Mapped[str] = mapped_column(
        String(10), unique=True, nullable=False)
    Films: Mapped[str] = mapped_column(
        String(500), unique=True, nullable=False)
    coult_in_credits: Mapped[str] = mapped_column(
        String(50), unique=True, nullable=False)
    created: Mapped[str] = mapped_column(
        String(75), unique=True, nullable=False)
    crew: Mapped[str] = mapped_column(
        String(25), unique=True, nullable=False)
    homeworld: Mapped[str] = mapped_column(
        String(250), unique=True, nullable=False)
    starships_type: Mapped[int] = mapped_column(
        String(500), unique=True, nullable=False)
    url: Mapped[str] = mapped_column(
        String(500), unique=True, nullable=False)

    def serialize(self):
        return {
            "ID": self.ID,
            "MGLT": self.MGLT,
            "cargo_capacity": self.cargo_capacity,
            "consumable": self.consumable,
            "Films": self.Films,
            "coult_in_credits": self.coult_in_credits,
            "created": self.created,
            "crew": self.crew,
            "homeworld": self.homeworld,
            "starships_type": self.starships_type,
            "url": self.url
        }


class Planet(db.Model):
    __tablename__ = "Planet"

    ID: Mapped[int] = mapped_column(primary_key=True)
    favotite: Mapped["Favotite"] = relationship(back_populates="Planet")
    films: Mapped["Films"] = relationship(back_populates="Planet")
    resource: Mapped[str] = mapped_column(
        String(300), unique=True, nullable=False)
    poblation: Mapped[str] = mapped_column(
        String(50), unique=True, nullable=False)
    consumable: Mapped[str] = mapped_column(
        String(10), unique=True, nullable=False)
    films: Mapped[str] = mapped_column(
        String(500), unique=True, nullable=False)
    coult_in_credits: Mapped[str] = mapped_column(
        String(50), unique=True, nullable=False)
    height: Mapped[str] = mapped_column(
        String(75), unique=True, nullable=False)
    homeworld: Mapped[str] = mapped_column(
        String(250), unique=True, nullable=False)
    climatic_conditions: Mapped[int] = mapped_column(
        String(500), unique=True, nullable=False)
    url: Mapped[str] = mapped_column(
        String(500), unique=True, nullable=False)

    def serialize(self):
        return {
            "ID": self.ID,
            "resource": self.resource,
            "poblation": self.poblation,
            "consumable": self.consumable,
            "Films": self.Films,
            "coult_in_credits": self.coult_in_credits,
            "height": self.height,
            "crew": self.crew,
            "homeworld": self.homeworld,
            " climatic_conditions": self.climatic_conditions,
            "url": self.url
        }
