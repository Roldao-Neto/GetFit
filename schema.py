from pydantic import BaseModel
from datetime import date

class Usuario(BaseModel):
    id: int = None
    nomeUsuario: str = None
    email: str = None
    senha: str = None
    dataCriacao: date = None
    tipoConta: int = None
    notificacoes: list['Notificacao'] = []

class Notificacao(BaseModel):
    id: int = None
    texto: str = None
    data: date = None
    remetente: 'Usuario' = None
    receptor: 'Usuario' = None

class Formulario(BaseModel):
    peso: float = None
    altura: float = None
    nascimento: date = None
    rotina: str = None
    alergias: str = None
    paciente: 'Paciente' = None

class Paciente(Usuario):
    formularios: list['Formulario'] = []
    consultas: list['Consulta'] = []

class Nutricionista(Usuario):
    notaMedia: float = None
    especialidades: list[str] = []
    avaliacoes: list['Avaliacao'] = []
    precoConsulta: float = None
    consultas: list['Consulta'] = []
    curriculo: 'Curriculo' = None

class Avaliador(Usuario):
    curriculos: list['Curriculo'] = []

class Curriculo(BaseModel):
    status: bool = False
    verificado: bool = False

class Consulta(BaseModel):
    horario: date = None
    statusConsulta: str = None
    paciente: 'Paciente' = None
    nutricionista: 'Nutricionista' = None

class Avaliacao(BaseModel):
    nota: int = None
    comentario: str = None
    data: date = None
    paciente: 'Paciente' = None
    nutricionista: 'Nutricionista' = None

class Mensagem(BaseModel):
    id: int = None
    remetente: Usuario = None
    receptor: Usuario = None
    conteudo: str = None
    data: date = None

