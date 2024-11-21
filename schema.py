from datetime import date
from sqlmodel import Field, Relationship, SQLModel, Session, create_engine


# Tabelas intermediárias para os relacionamentos
class UsuarioNotificacao(SQLModel, table=True):
    __tablename__ = "usuario_notificacao"
    usuario_id: int = Field(foreign_key="usuario.id", primary_key=True)
    notificacao_id: int = Field(foreign_key="notificacao.id", primary_key=True)


class UsuarioConsulta(SQLModel, table=True):
    __tablename__ = "usuario_consulta"
    usuario_id: int = Field(foreign_key="usuario.id", primary_key=True)
    consulta_id: int = Field(foreign_key="consulta.id", primary_key=True)


class UsuarioFormulario(SQLModel, table=True):
    __tablename__ = "usuario_formulario"
    usuario_id: int = Field(foreign_key="usuario.id", primary_key=True)
    formulario_id: int = Field(foreign_key="formulario.id", primary_key=True)


class UsuarioAvaliacao(SQLModel, table=True):
    __tablename__ = "usuario_avaliacao"
    usuario_id: int = Field(foreign_key="usuario.id", primary_key=True)
    avaliacao_id: int = Field(foreign_key="avaliacao.id", primary_key=True)


class UsuarioCurriculo(SQLModel, table=True):
    __tablename__ = "usuario_curriculo"
    usuario_id: int = Field(foreign_key="usuario.id", primary_key=True)
    curriculo_id: int = Field(foreign_key="curriculo.id", primary_key=True)


# Tabelas principais
class Usuario(SQLModel, table=True):
    __tablename__ = "usuario"
    id: int | None = Field(default=None, primary_key=True)
    nomeUsuario: str | None = Field(max_length=31)
    email: str | None = Field(max_length=63)
    senha: str | None = Field(max_length=63)
    dataCriacao: date | None = Field(default=None)
    tipoConta: int | None = Field(default=None)  # 1: Paciente, 2: Nutricionista, 3: Avaliador
    notificacoes: list["Notificacao"] = Relationship(
        back_populates="usuarios", link_model=UsuarioNotificacao
    )
    consultas: list["Consulta"] = Relationship(
        back_populates="usuarios", link_model=UsuarioConsulta
    )
    formularios: list["Formulario"] = Relationship(
        back_populates="usuarios", link_model=UsuarioFormulario
    )
    avaliacoes: list["Avaliacao"] = Relationship(
        back_populates="usuarios", link_model=UsuarioAvaliacao
    )
    curriculos: list["Curriculo"] = Relationship(
        back_populates="usuarios", link_model=UsuarioCurriculo
    )


class Notificacao(SQLModel, table=True):
    __tablename__ = "notificacao"
    id: int | None = Field(default=None, primary_key=True)
    texto: str | None = Field(max_length=255)
    usuarios: list["Usuario"] = Relationship(
        back_populates="notificacoes", link_model=UsuarioNotificacao
    )


class Formulario(SQLModel, table=True):
    __tablename__ = "formulario"
    id: int | None = Field(default=None, primary_key=True)
    peso: float | None = Field(default=None)
    altura: float | None = Field(default=None)
    nascimento: date | None = Field(default=None)
    rotina: str | None = Field(max_length=511)
    alergias: str | None = Field(max_length=511)
    usuarios: list["Usuario"] = Relationship(
        back_populates="formularios", link_model=UsuarioFormulario
    )


class Curriculo(SQLModel, table=True):
    __tablename__ = "curriculo"
    id: int | None = Field(default=None, primary_key=True)
    status: bool | None = Field(default=False)
    verificado: bool | None = Field(default=False)
    usuarios: list["Usuario"] = Relationship(
        back_populates="curriculos", link_model=UsuarioCurriculo
    )


class Consulta(SQLModel, table=True):
    __tablename__ = "consulta"
    id: int | None = Field(default=None, primary_key=True)
    horario: date | None = Field(default=None)
    statusConsulta: str | None = Field(max_length=31)
    usuarios: list["Usuario"] = Relationship(
        back_populates="consultas", link_model=UsuarioConsulta
    )


class Avaliacao(SQLModel, table=True):
    __tablename__ = "avaliacao"
    id: int | None = Field(default=None, primary_key=True)
    nota: int | None = Field(default=None)
    comentario: str | None = Field(max_length=255)
    data: date | None = Field(default=None)
    usuarios: list["Usuario"] = Relationship(
        back_populates="avaliacoes", link_model=UsuarioAvaliacao
    )


class Mensagem(SQLModel, table=True):
    __tablename__ = "mensagem"
    id: int | None = Field(default=None, primary_key=True)
    conteudo: str | None = Field(max_length=255)
    data: date | None = Field(default=None)
    remetente_id: int | None = Field(foreign_key="usuario.id")
    receptor_id: int | None = Field(foreign_key="usuario.id")


if __name__ == "__main__":
    usuario_bd = "getfit"
    senha_bd = "getfit"
    host_bd = "localhost"
    banco_bd = "getfit"
    url_bd = f"mariadb+pymysql://{usuario_bd}:{senha_bd}@{host_bd}:3306/{banco_bd}?charset=utf8mb4"
    engine = create_engine(url_bd, echo=True)

    SQLModel.metadata.create_all(engine)

    with Session(engine) as session:
        pass
