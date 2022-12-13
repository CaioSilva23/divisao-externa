<div align="center" id="top"> 
  <img src="./public/logo.png" alt="Freelaway" />

<!-- &#xa0; -->


</div>

<div align="center"> 
  <h1 align="center">SISTEMA DE CONTROLE - PREGÕES E EMPENHOS</h1>
  <!-- <img src="./public/pystack_week.png" alt="Freelaway" width=200 /> -->
</div>

<p align="center">
  <img alt="Principal linguagem do projeto" src="https://img.shields.io/github/languages/top/navegantes/freelaway?color=56BEB8" />

  <img alt="Quantidade de linguagens utilizadas" src="https://img.shields.io/github/languages/count/navegantes/freelaway?color=56BEB8" />

  <img alt="Tamanho do repositório" src="https://img.shields.io/github/repo-size/navegantes/freelaway?color=56BEB8" />

  <img alt="Licença" src="https://img.shields.io/github/license/navegantes/freelaway?color=56BEB8" />

  <!-- <img alt="Github issues" src="https://img.shields.io/github/issues/navegantes/freelaway?color=56BEB8" /> -->

  <!-- <img alt="Github forks" src="https://img.shields.io/github/forks/navegantes/freelaway?color=56BEB8" /> -->

  <!-- <img alt="Github stars" src="https://img.shields.io/github/stars/navegantes/freelaway?color=56BEB8" /> -->
</p>

<!-- Status -->

<!-- <h4 align="center">
	🚧  Freelaway 🚀 Em construção...  🚧
</h4>

<hr> -->

<p align="center">
  <a href="#dart-sobre">Sobre</a> &#xa0; | &#xa0; 
  <a href="#sparkles-funcionalidades">Funcionalidades</a> &#xa0; | &#xa0;
  <a href="#rocket-tecnologias">Tecnologias</a> &#xa0; | &#xa0;
  <a href="#white_check_mark-pré-requisitos">Pré requisitos</a> &#xa0; | &#xa0;
  <a href="#checkered_flag-começando">Começando</a> &#xa0; | &#xa0;
  <a href="#memo-licença">Licença</a> &#xa0; | &#xa0;
  <a href="https://github.com/navegantes" target="_blank">Autor</a>
</p>

<p align="center">
  <img alt="Login" src="public/login.png" width=250>
  <img alt="cadastrar" src="public/cadastrar.png" width=250>
  <img alt="Recuprerar senha" src="public/recuperar_senha.png" width=250>
  <img alt="Encontrar job" src="public/encontrar_jobs.png" width=250>
  <img alt="Job" src="public/job.png" width=250>
  <img alt="Perfil" src="public/perfil.png" width=250>
</p>

## 🎯 Sobre

O projeto inicial foi desenvolvindo para gerenciar e controlar a emissão de Pregões Eletrônicos e Notas de Empenhos.\
Além proposta inicial, foi desenvolvido também, o controle de crédito e fornecedor.

## ✨ Funcionalidades

✔️ Login/Logout;\
✔️ CRUD de Om (Organização Militar);\
✔️ CRUD de Empenho;\
✔️ CRUD de Pregões;\
✔️ CRUD de Fornecedor;\
✔️ CRUD de Nota de Crédito;\
✔️ CRUD de Plano Interno;\


## 🚀 Tecnologias

As seguintes ferramentas foram usadas na construção do projeto:

- [Python](https://www.python.org/)
- [Django](https://nodejs.org/en/)
- [JavaScript](https://www.javascript.com/)
- [SQLite](https://www.sqlite.org/index.html)
- [Bootstrap](https://getbootstrap.com/)

## ✅ Pré requisitos

Antes de começar 🏁, você precisa ter o [Python](https://www.python.org/downloads/) instalado em sua maquina.

## 🏁 Começando

1 - Primeiro clone o repositório e entre na pasta do projeto.

```bash
# Clone este repositório
$ git clone https://github.com/CaioSilva23/divisao-externa.git

# Entre na pasta
$ cd divisao-externa
```

2 - Segundo inicie um ambiente virtual

```bash
# Criar
  # Linux
    $ python3 -m venv venv
  # Windows
    $ python -m venv venv

#Ativar
  # Linux
    $ source venv/bin/activate
  # Windows
    $ venv/Scripts/Activate

# Caso algum comando retorne um erro de permissão execute o código e tente novamente:

  $ Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

3 - Instale as dependências

```bash
# Instale as dependências
# Linux
$ pip3 install -r requirements.txt
# Windows
$ pip install -r requirements.txt
```

4 - Faça as migrações.

```bash
# Linux
python3 manage.py migrate
# Windows
python manage.py migrate
```

5 - Crie um super usuário

```bash
$ python3 .\manage.py createsuperuser
$ python .\manage.py createsuperuser
```

6 - Inicie a aplicação

```bash
# Para iniciar o projeto
# Linux
$ python3 manage.py runserver
# Windows
$ python manage.py runserver

# O app vai inicializar em <http://127.0.0.1:8000/>

# Para iniciar o projeto em uma porta especifica
$ python manage.py runserver <porta>

# O app vai inicializar em <http://127.0.0.1:<porta>/>

```

## 📝 Licença

Este projeto está sob licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

Desenvolvido por <a href="https://github.com/caiosilva23" target="_blank">Caio Silva</a>

&#xa0;

<a href="#top">Voltar para o topo</a>
