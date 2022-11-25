from config import db, ma


class Person(db.Model):
    __tablename__ = "pessoas"
    id_pessoa = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    rg = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(100), nullable=False)
    data_nascimento = db.Column(db.DateTime(), nullable=False)
    data_admissao = db.Column(db.DateTime(), nullable=False)
    funcao = db.Column(db.String(100), nullable=True)

    def __init__(self, nome, rg, cpf, data_nascimento, data_admissao, funcao):
        self.nome = nome
        self.rg = rg
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.data_admissao = data_admissao
        self.funcao = funcao

    def __repr__(self):
        return '<Person %r>' % self.nome


class PersonSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Person
        load_instance = True
        sqla_session = db.session


person_schema = PersonSchema()
people_schema = PersonSchema(many=True)
