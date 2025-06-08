Loja Virtual com django

Este projeto é uma aplicação de e-commerce desenvolvida com Django. 
Ele permite o cadastro e exibição de produtos de informática, organização por categorias, filtragem e busca, 
além de um sistema de carrinho de compras e checkout.

## Funcionalidades

- **Cadastro de Usuário**: Registro, login e logout.
- **Catálogo de Produtos**: Listagem de produtos com imagens e preços.
- **Filtro por Categoria**: Visualize produtos de uma categoria específica.
- **Busca Inteligente**: Encontre produtos pelo nome ou descrição.
- **Carrinho de Compras**: Adicione, visualize e remova produtos via sessão.


## Tecnologias utilizadas

- **Django**: Framework web principal.
- **Pillow**: Manipulação de imagens e criação de thumbnails.
- **PyMySQL**: Driver MySQL usado como backend de banco de dados.
- **HTML**: Layout simples e responsivo.
- **Session Storage**: Armazena dados do carrinho.


## Instalação

1. **Clone o repositório**
```bash
git clone https://github.com/Naiarapacheco/Loja.git
```

2. **Instale as dependências**
```bash
pip install -r requirements.txt
```

3. **Aplique as migrações**
```bash
python manage.py migrate
```

4. **Crie um superusuário**
```bash
python manage.py createsuperuser
```

5. **Inicie o servidor de desenvolvimento**
```bash
python manage.py runserver 
```
