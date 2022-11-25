from flask import abort, make_response

from config import db
from models import Person, people_schema, person_schema


def read_all():
    people = Person.query.all()
    return people_schema.dump(people)


def create(person):
    cpf = person.get("cpf")

    existing_person = Person.query.filter(Person.cpf == cpf).one_or_none()

    if existing_person is None:
        new_person = person_schema.load(person, session=db.session)
        db.session.add(new_person)
        db.session.commit()
        return person_schema.dump(new_person), 201
    else:
        abort(
            406,
            f"Person with cpf number {cpf} already exists",
        )


def read_one(id):
    person = Person.query.filter(Person.id_pessoa == id).one_or_none()

    if person is not None:
        return person_schema.dump(person)
    else:
        abort(
            404, f"Person with id number {id} not found"
        )


def update(id, person):
    existing_person = Person.query.filter(Person.id_pessoa == id).one_or_none()

    if existing_person:
        update_person = person_schema.load(person, session=db.session)
        existing_person.nome = update_person.nome
        existing_person.rg = update_person.rg
        existing_person.cpf = update_person.cpf
        existing_person.data_nascimento = update_person.data_nascimento
        existing_person.data_admissao = update_person.data_admissao
        existing_person.funcao = update_person.funcao

        db.session.merge(existing_person)
        db.session.commit()
        return person_schema.dump(existing_person), 201
    else:
        abort(
            404,
            f"Person with ID number {id} not found"
        )


def delete(id):
    existing_person = Person.query.filter(Person.id_pessoa == id).one_or_none()

    if existing_person:
        db.session.delete(existing_person)
        db.session.commit()
        return make_response(f"{id} successfully deleted", 200)
    else:
        abort(
            404,
            f"Person with cpf number {id} not found"
        )
