# ATV09_BEATRIZ_MAISA
Projeto MAITRIZ de Beatriz e Maísa, da turma 523. Junção do site MAITRIZ (ATV06) com o projeto Django.

# ATV09 - Migração do Portal para Django

## Identificação da dupla

- **Alunas:** Beatriz de Araújo Bezerra e Maísa Alves de Melo
- **Turma:** 523
- **Instituição:** IFAL - Campus Palmeira dos Índios
- **Curso:** Técnico Integrado ao Ensino Médio em Informática

## Descrição do projeto

O **Maitriz** é o portal desenvolvido na ATV06, agora migrado para o framework **Django**. O portal mantém a identidade visual, o layout e a responsividade da versão anterior, mas passou a funcionar de forma dinâmica:

- Os conteúdos das páginas (currículos, contos e filmes) ficam armazenados no banco de dados, no Model `Conteudo`, e são cadastrados pelo Django Admin.
- O menu de navegação é gerado dinamicamente a partir do Model `Menu`, que pode apontar para um conteúdo interno ou para um link externo.
- A navegação entre os conteúdos usa o sistema de URLs e Views do Django (`/conteudo/<slug>/`).
- A estrutura do portal (`header`, `nav`, `main`, `footer`) fica em templates com herança.
- CSS e imagens ficam organizados como arquivos estáticos.

## Tecnologias utilizadas

- Python 3
- Django
- SQLite
- HTML5 (semântico)
- CSS3 (Flexbox e Media Queries)
- Git e GitHub
- Visual Studio Code

## Estrutura do projeto

```
ATV09_BEATRIZ_MAISA/
├── README.md
├── requirements.txt
└── maitriz/                  # pasta do projeto Django (onde está o manage.py)
    ├── manage.py
    ├── maitriz/              # configurações do projeto (settings.py, urls.py)
    └── site_maitriz/         # aplicação (models, views, urls, admin)
        ├── templates/site_maitriz/
        └── static/site_maitriz/
            ├── css/
            └── img/
```

## Como executar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/bia-bezerra/ATV09_BEATRIZ_MAISA.git
cd ATV09_BEATRIZ_MAISA
```

### 2. Criar e ativar o ambiente virtual

Criar:

```bash
python -m venv venv
```

Ativar no **Linux/Mac**:

```bash
source venv/bin/activate
```

Ativar no **Windows (PowerShell)**:

```powershell
venv\Scripts\Activate.ps1
```

Ativar no **Windows (CMD)**:

```cmd
venv\Scripts\activate.bat
```

Quando o ambiente estiver ativo, aparece `(venv)` no início da linha do terminal.

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 4. Entrar na pasta do projeto

```bash
cd maitriz
```

### 5. Executar as migrations

```bash
python manage.py migrate
```

### 6. Criar o superusuário

```bash
python manage.py createsuperuser
```

O terminal vai pedir um nome de usuário, um e-mail (opcional) e uma senha. A senha não aparece na tela enquanto é digitada.

### 7. Executar o servidor

```bash
python manage.py runserver
```

## Acesso

- **Aplicação:** http://127.0.0.1:8000/
- **Django Admin:** http://127.0.0.1:8000/admin/

No Django Admin, entre com o superusuário criado no passo 6.

## Como cadastrar conteúdos e menus

1. Acesse o Django Admin.
2. Em **Conteúdos**, cadastre as páginas: título, slug (ex.: `curriculo-beatriz`) e o HTML interno da página (somente o conteúdo, sem `<html>`, `<head>`, `<body>`, `<header>`, `<nav>` ou `<footer>`).
3. Em **Menus**, cadastre os itens da navegação: título, tipo de destino (conteúdo interno ou link externo), ordem, conteúdo relacionado (se interno) ou URL (se externo).
4. As alterações aparecem automaticamente no portal.

## Conteúdo cadastrado

- 4 conteúdos internos: Currículo de Beatriz, Currículo de Maísa, Contos de Beatriz e Filmes de Maísa.
- 2 links externos no menu.
- Página inicial na URL `/`.