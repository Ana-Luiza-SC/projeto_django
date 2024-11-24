# Gerenciador de Tarefas com Django

Um projeto simples de gerenciamento de tarefas utilizando Django, criado como parte de um treinamento no framework.

## Funcionalidades
- Adicionar tarefas com título e descrição.
- Listar tarefas cadastradas.
- Marcar tarefas como concluídas.
- Excluir tarefas.

## Pré-requisitos

Certifique-se de ter as seguintes ferramentas instaladas:
- **Python** (versão 3.8 ou superior)
- **Git**

## Instalação e configuração

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/Ana-Luiza-SC/projeto_django
   cd projeto_django
   ```

2. **Crie um ambiente virtual**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Aplique as migrações do banco de dados** (se aplicável):
   Caso o projeto utilize banco de dados, execute:
   ```bash
   python manage.py migrate
   ```

5. **Inicie o servidor**:
   ```bash
   python manage.py runserver
   ```

6. **Acesse o projeto no navegador**:
   Abra [http://127.0.0.1:8000/](http://127.0.0.1:8000/) para visualizar o projeto.

## Estrutura do projeto
- `manage.py`: Comando principal para gerenciar o projeto.
- `requirements.txt`: Lista de dependências necessárias.
- `templates/`: Arquivos HTML para renderização das páginas.
- `static/`: Arquivos CSS e JS para estilização.
- `db.sqlite3` (se aplicável): Banco de dados utilizado pelo Django.

## Contribuição

Sinta-se à vontade para abrir **issues** ou enviar **pull requests** com melhorias!

## Licença

Este projeto é de uso livre para fins educativos.
