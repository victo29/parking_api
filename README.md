# 🚗 Parking API

![Python](https://img.shields.io/badge/Python-3.12+-blue?logo=python)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue?logo=docker)
![FastAPI](https://img.shields.io/badge/FastAPI-Framework-0ba360?logo=fastapi)

A **Parking API** é uma aplicação desenvolvida com **FastAPI** que gerencia o fluxo de veículos em um estacionamento.
Ela permite o **registro de entradas e saídas**, **cálculo automático do valor a pagar** com base no tempo de permanência e **consulta de registros** por períodos ou placa.

---

## 🧩 Principais Funcionalidades

- Registrar a **entrada** de um veículo.
- Registrar a **saída** e calcular o **valor total** com base no tempo de permanência e na configuração de valor por hora.
- **Excluir** e **atualizar** registros existentes.
- Consultar registros por **período de tempo** ou **placa específica**.
- Obter todos os registros **abertos (veículos ainda estacionados)**.

---

## 🧱 Tecnologias Utilizadas

- **Python 3.12+**
- **FastAPI**
- **SQLAlchemy**
- **Pydantic**
- **PostgreSQL**
- **Docker**

---

## 🚀 Como Executar o Projeto

### 1. Clone o repositório

```bash
git clone https://github.com/victo29/parking_api.git
cd parking_api
```

### 2. Crie um arquivo `.env`

Crie um arquivo `.env` na raiz do projeto e adicione as seguintes variáveis:

```bash
DB_USER=parking_user
DB_PASSWORD=root
DB_HOST=db        # ou localhost, se rodar sem Docker
DB_PORT=5432
DB_NAME=parking_db
```
---

### 3. Executando com Docker

O projeto já possui um arquivo `docker-compose.yml` configurado.
Para subir os containers, basta rodar:

```bash
docker compose up -d
```
A API ficará disponível em:
👉 **http://127.0.0.1:8000**


---

### 4. Acesse a documentação interativa da API

```
 http://localhost:8000/docs
```
---

## 🧠 Endpoints

| Método | Rota | Descrição |
|--------|------|------------|
| **POST** | `/registries/` | Registra a **entrada** de um veículo |
| **PUT** | `/registries/exit` | Registra a **saída** e calcula o pagamento |
| **DELETE** | `/registries/delete/{id}` | Exclui um registro pelo ID |
| **PUT** | `/registries/update/{id}` | Atualiza um registro existente |
| **GET** | `/registries/period` | Retorna registros entre duas datas |
| **GET** | `/registries/search` | Busca registros por período e placa |
| **GET** | `/registries/opened` | Lista todos os registros **abertos** |

---

## 🧾 Exemplo de Uso

### Registro de Entrada

**POST** `/registries/`

```json
{
  "car_plate": "ABC1234",
  "proprietor": "Iasmin",
  "model": "Civic"
}
```

**Resposta:**

```json
{
  "success": "registry added successfully"
}
```

---

### Registro de Saída

**PUT** `/registries/exit?car_plate=ABC1234`

**Resposta:**

```json
{
  "success": "exit time successfully registered",
  "registry": {
    "id": 1,
    "car_plate": "ABC1234",
    "proprietor": "IASMIN",
    "model": "CIVIC"
    "entry_time": "2025-10-17 12:34",
    "exit_time": "2025-10-17 14:20",
    "value": 15.0
  }
}
```
---

## 🧑‍💻 Autor

**Victor Souza de Queiroz Tavares** --
Desenvolvedor
📧 [victor.sq.tavares@gmail.com]
🌐 [github.com/victo29](https://github.com/victo29)


## ⭐ Contribuição

Sinta-se à vontade para abrir *issues* e *pull requests* com melhorias ou correções.
Contribuições são bem-vindas! 🚀
