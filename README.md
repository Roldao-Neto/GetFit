# Projeto: GetFit - Plataforma de Conexão entre Nutricionistas e Clientes

## Visão Geral
O **GetFit** é uma plataforma web projetada para conectar clientes com metas de saúde a profissionais especializados, como nutricionistas. O sistema permite interações por chat, agendamento de consultas e gerenciamento de progressos, além de avaliações e recomendações personalizadas baseadas em questionários preenchidos pelos clientes.

## Funcionalidades Principais
1. **Cadastro e Login**:
   - Registro de contas diferenciadas para clientes e profissionais.
   - Mecanismos de autenticação seguros, incluindo recuperação de senha.

2. **Questionário Personalizado**:
   - Coleta de informações sobre saúde, objetivos e hábitos alimentares dos clientes.
   - Geração de listas de profissionais adequados.

3. **Agendamento e Gerenciamento de Consultas**:
   - Agenda dinâmica para profissionais.
   - Controle de consultas e histórico para clientes.

4. **Comunicação via Chat**:
   - Suporte a mensagens em texto, áudio e imagens entre clientes e profissionais.

5. **Sistema de Avaliações**:
   - Clientes podem avaliar os serviços dos profissionais e deixar comentários.

6. **Gerenciamento de Currículos**:
   - Validação de credenciais de profissionais.
   - Controle rigoroso contra falsificações.

## Tecnologias Utilizadas
- **Linguagem**: Python
- **Framework**: FastAPI
- **Banco de Dados**: MariaDB com SQLModel
- **Outros**: PyMySQL para integração com o banco de dados.

## Estrutura do Projeto
- **main.py**: Contém as rotas e a lógica principal da API, incluindo:
  - Operações de CRUD para entidades como `Usuario`, `Notificacao`, `Mensagem`, entre outras.
  - Dependência de banco de dados gerenciada pelo SQLModel.
- **domain.py**: Define os modelos do banco de dados usando SQLModel.

## Pré-requisitos
1. **Python 3.9 ou superior**.
2. **Banco de dados MariaDB**.
3. **Bibliotecas Python**:
   - FastAPI
   - SQLModel
   - PyMySQL

## Como Configurar
1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/getfit.git
   cd getfit
   ```
2. Configure o banco de dados:
   - Instale o XAMPP Control Panel:
     ```Link
     https://www.apachefriends.org/pt_br/index.html
     ```
   - Inicie o Apache e o MySQL
   - Clique em admin no MySQL
   - Crie um banco de dados clicando em contas do usuário -> adicionar contas de usuário -> selecione o nome, a senha e marque a opção criar banco de dados com o mesmo nome.
   - Atualize as credenciais no arquivo `main.py`:
     ```python
     usuario_bd = "seu_usuario"
     senha_bd = "sua_senha"
     host_bd = "localhost"
     banco_bd = "getfit"
     ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Execute as migrações para criar as tabelas:
   ```bash
   python domain.py
   ```

5. Inicie o servidor:
   ```bash
   uvicorn main:app --reload
   ```

## Como Usar
- Acesse o endpoint principal: [http://127.0.0.1:8000](http://127.0.0.1:8000).
- Use ferramentas como **Postman** ou **Swagger UI** (disponível em `/docs`) para testar as rotas da API.

## Rotas Principais
### Entidade `Usuario`
- **GET** `/usuario/all`: Retorna todos os usuários.
- **POST** `/usuario`: Adiciona um novo usuário.
- **PUT** `/usuario/{id}`: Atualiza as informações do usuário com o ID especificado.
- **DELETE** `/usuario/{id}`: Remove o usuário com o ID especificado.

### Outras Entidades
- Rotas similares estão disponíveis para `Notificacao`, `Mensagem`, `Avaliacao`, `Consulta`, `Curriculo` e `Formulario`.
