# API de Gerenciamento de Carros com Flask

## Descrição
Esta é uma API simples de gerenciamento de carros desenvolvida com Flask em Python. Utiliza a classe `Carros` para representar carros e fornece endpoints para listar, detalhar, criar, editar e excluir carros. A API inicia com uma lista de carros predefinidos.

## Tecnologias Utilizadas
- Python
- Flask

## Endpoints
- **Listar Carros:** `/api/carros/` (GET)
- **Detalhar Carro:** `/api/carros/<int:id>/` (GET)
- **Deletar Carro:** `/api/carros/<int:id>/` (DELETE)
- **Criar Carro:** `/api/carros/` (POST)
- **Editar Carro:** `/api/carros/<int:id>/` (PUT)
- **Editar Parcialmente Carro:** `/api/carros/<int:id>/` (PATCH)

## Exemplos de Uso
- Listar todos os carros: `GET /api/carros/`
- Detalhar um carro específico: `GET /api/carros/<int:id>/`
- Deletar um carro específico: `DELETE /api/carros/<int:id>/`
- Criar um novo carro: `POST /api/carros/`
  - Exemplo de payload:
    ```json
    {
        "marca": "Ford",
        "ano": 2020,
        "status": "DISPONIVEL"
    }
    ```
- Editar um carro existente: `PUT /api/carros/<int:id>/`
  - Exemplo de payload:
    ```json
    {
        "marca": "Chevrolet",
        "ano": 2021,
        "status": "NEGOCIANDO"
    }
    ```
- Editar parcialmente um carro existente: `PATCH /api/carros/<int:id>/`
  - Exemplo de payload:
    ```json
    {
        "ano": 2022
    }
    ```
