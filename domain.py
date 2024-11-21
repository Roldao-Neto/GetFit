from datetime import date
from sqlmodel import Field
from sqlmodel import Relationship
from sqlmodel import SQLModel
from sqlmodel import Session
from sqlmodel import create_engine

class Usuario(SQLModel, table=True):
    __tablename__ = "usuario"

    id: int | None = Field(default=None, primary_key=True)
    nomeUsuario: str | None = Field(max_length=31, unique=True)
    email: str | None = Field(max_length=63, unique=True)
    senha: str | None = Field(max_length=63)
    dataCriacao: date | None = Field(default=None)
    tipoConta: int | None = Field(default=None)
    notificacoes: list["Notificacao"] = Relationship(back_populates="usuario")
    mensagens_recebidas: list["Mensagem"] = Relationship(
        back_populates="receptor",
        sa_relationship_kwargs={"primaryjoin": "Usuario.id == Mensagem.id_receptor"},
    )
    mensagens_enviadas: list["Mensagem"] = Relationship(
        back_populates="remetente",
        sa_relationship_kwargs={"primaryjoin": "Usuario.id == Mensagem.id_remetente"},
    )
    avaliacoes_recebidas: list["Avaliacao"] = Relationship(
        back_populates="nutricionista",
        sa_relationship_kwargs={"primaryjoin": "Usuario.id == Avaliacao.id_nutricionista"},
    )
    avaliacoes_enviadas: list["Avaliacao"] = Relationship(
        back_populates="paciente",
        sa_relationship_kwargs={"primaryjoin": "Usuario.id == Avaliacao.id_paciente"},
    )
    consultasNutri: list["Consulta"] = Relationship(
        back_populates="nutricionista",
        sa_relationship_kwargs={"primaryjoin": "Usuario.id == Consulta.id_nutricionista"},
    )
    consultasPaciente: list["Consulta"] = Relationship(
        back_populates="paciente",
        sa_relationship_kwargs={"primaryjoin": "Usuario.id == Consulta.id_paciente"},
    )

    curriculoNutri: 'Curriculo' = Relationship(
        back_populates="nutricionista",
        sa_relationship_kwargs={"primaryjoin": "Usuario.id == Curriculo.id_nutricionista"},
    )
    curriculoAvaliador: list['Curriculo'] = Relationship(
        back_populates="avaliador",
        sa_relationship_kwargs={"primaryjoin": "Usuario.id == Curriculo.id_avaliador"},
    )
    formulario: 'Formulario' = Relationship(back_populates='paciente')

class Notificacao(SQLModel, table = True):
    __tablename__ = "notificacao"
    id: int | None = Field(default=None, primary_key=True)
    texto: str | None = Field(max_length=255)
    data: date | None = Field(default=None)
    id_usuario: int | None = Field(default=None, foreign_key='usuario.id')
    usuario: "Usuario" = Relationship(back_populates="notificacoes")
    
class Mensagem(SQLModel, table = True):
    __tablename__ = "mensagem"
    conteudo: str | None = Field(max_length=255)
    data: date | None = Field(default=None)
    id: int | None = Field(default=None, primary_key=True)
    receptor: "Usuario" = Relationship(
        back_populates="mensagens_recebidas",
        sa_relationship_kwargs={"primaryjoin": "Usuario.id == Mensagem.id_receptor"},
    )
    remetente: "Usuario" = Relationship(
        back_populates="mensagens_enviadas",
        sa_relationship_kwargs={"primaryjoin": "Usuario.id == Mensagem.id_remetente"},
    )
    id_receptor: int | None = Field(default=None, foreign_key="usuario.id")
    id_remetente: int | None = Field(default=None, foreign_key="usuario.id")

class Avaliacao(SQLModel, table = True):
    __tablename__ = "avaliacao"
    id: int | None = Field(default=None, primary_key=True)
    nota: int | None = Field(default=None)
    comentario: str | None = Field(max_length=255)
    data: date | None = Field(default=None)
    nutricionista: "Usuario" = Relationship(
        back_populates="avaliacoes_recebidas",
        sa_relationship_kwargs={"primaryjoin": "Usuario.id == Avaliacao.id_nutricionista"},
    )
    paciente: "Usuario" = Relationship(
        back_populates="avaliacoes_enviadas",
        sa_relationship_kwargs={"primaryjoin": "Usuario.id == Avaliacao.id_paciente"},
    )
    id_nutricionista: int | None = Field(default=None, foreign_key="usuario.id")
    id_paciente: int | None = Field(default=None, foreign_key="usuario.id")

class Consulta(SQLModel, table=True):
    __tablename__ = "consulta"

    id: int | None = Field(default=None, primary_key=True)
    horario: date | None = Field(default=None)
    statusConsulta: str | None = Field(max_length=31)
    id_nutricionista: int | None = Field(default=None, foreign_key="usuario.id")
    id_paciente: int | None = Field(default=None, foreign_key="usuario.id")

    nutricionista: "Usuario" = Relationship(
        back_populates="consultasNutri",
        sa_relationship_kwargs={"primaryjoin": "Usuario.id == Consulta.id_nutricionista"},
    )
    paciente: "Usuario" = Relationship(
        back_populates="consultasPaciente",
        sa_relationship_kwargs={"primaryjoin": "Usuario.id == Consulta.id_paciente"},
    )

class Curriculo(SQLModel, table = True):
    __tablename__ = "curriculo"
    id: int | None = Field(default=None, primary_key=True)
    status: bool | None = Field(default=None)
    verificado: bool | None = Field(default=None)
    nutricionista: "Usuario" = Relationship(
        back_populates="curriculoNutri",
        sa_relationship_kwargs={"primaryjoin": "Usuario.id == Curriculo.id_nutricionista"},
    )
    avaliador: "Usuario" = Relationship(
        back_populates="curriculoAvaliador",
        sa_relationship_kwargs={"primaryjoin": "Usuario.id == Curriculo.id_avaliador"},
    )
    id_nutricionista: int | None = Field(default=None, foreign_key="usuario.id")
    id_avaliador: int | None = Field(default=None, foreign_key="usuario.id")

class Formulario(SQLModel, table = True):
    __tablename__ = "formulario"
    peso: float | None = Field(default=None)
    altura: float | None = Field(default=None)
    nascimento: date | None = Field(default=None)
    rotina: str | None = Field(max_length=511)
    alergias: str | None = Field(max_length=511)

    id_paciente: int | None = Field(default=None, primary_key=True, foreign_key="usuario.id")
    paciente: 'Usuario' = Relationship(back_populates='formulario')

if __name__ == "__main__":
    usuario_bd="getfit"
    senha_bd="getfit"
    host_bd="localhost"
    banco_bd="getfit"
    url_bd = f"mariadb+pymysql://{usuario_bd}:{senha_bd}@{host_bd}:3306/{banco_bd}?charset=utf8mb4"
    engine = create_engine(url_bd, echo=True)

    SQLModel.metadata.create_all(engine)

    with Session(engine) as se:

        n1 = Notificacao(id=1, texto="essa e a n1")
        n2 = Notificacao(id=2, texto="essa e a n2")
        n3 = Notificacao(id=3, texto="essa e a n3")

        nutri = Usuario(id=1, nomeUsuario="Nutri", email="nutri@a.com", dataCriacao= date.today(), tipoConta= 1, notificacoes = [n1, n2])
        paciente = Usuario(id=2, nomeUsuario="Paciente", email="paciente@a.com", dataCriacao= date.today(), tipoConta= 2, notificacoes = [n3])
        avaliador = Usuario(id=3, nomeUsuario="Avaliador", email="avaliador@a.com", dataCriacao= date.today(), tipoConta= 3)
        
        m1 = Mensagem(id=1, receptor=paciente, remetente=nutri, data=date.today(), conteudo="aqui esta a dieta")
        nutri.mensagens_enviadas.append(m1)
        paciente.mensagens_recebidas.append(m1)

        m2 = Mensagem(id=2, receptor=nutri, remetente=paciente, data=date.today(), conteudo="fiz a dieta e perdi 2 Kg!")
        nutri.mensagens_recebidas.append(m2)
        paciente.mensagens_enviadas.append(m2)

        aval = Avaliacao(id=0, nota=5, comentario="achei otimo", data=date.today(), nutricionista=nutri, paciente=paciente)
        nutri.avaliacoes_recebidas.append(aval)
        paciente.avaliacoes_enviadas.append(aval)

        cons = Consulta(id=0, horario=date.isoformat(date.today()), statusConsulta= "Em andamento", nutricionista=nutri, paciente=paciente)
        nutri.consultasNutri.append(cons)
        paciente.consultasPaciente.append(cons)

        curriculo = Curriculo(id=1, status=True, verificado=True, nutricionista=nutri, avaliador= avaliador)
        nutri.curriculoNutri = curriculo
        avaliador.curriculoAvaliador.append(curriculo)

        form = Formulario(peso=80.0, altura=1.77, nascimento=date.today(), rotina='Exercícios frequentes', alergias='nehuma', paciente=paciente)
        
        se.add(n1)
        se.add(n2)
        se.add(n3)
        se.add(nutri)
        se.add(paciente)
        se.add(avaliador)
        se.add(m1)
        se.add(m2)
        se.add(aval)
        se.add(cons)
        se.add(curriculo)
        se.add(form)

        se.commit()
