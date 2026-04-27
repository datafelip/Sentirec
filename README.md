# 🚀 Sentirec - Sistema Inteligente de Recomendação com Análise de Sentimentos

O **Sentirec** é um sistema de recomendação desenvolvido em Python que combina técnicas de **Machine Learning**, **Processamento de Linguagem Natural (PLN)** e **Análise de Sentimentos** para sugerir produtos personalizados aos usuários com base em suas avaliações textuais.

O projeto utiliza comentários e notas armazenados em um banco de dados **MySQL** para identificar o sentimento das avaliações e gerar recomendações mais precisas e relevantes. Além disso, conta com uma **API REST desenvolvida em FastAPI** e uma interface web para interação com o sistema.

---

## ✨ Funcionalidades

- 📥 Coleta automática de avaliações armazenadas no MySQL
- 🧹 Pré-processamento textual com técnicas de PLN
- 😊 Análise de sentimentos utilizando bibliotecas especializadas
- 🎯 Sistema de recomendação personalizado por usuário
- 🌐 API REST construída com FastAPI
- 💻 Interface web para consulta de avaliações e recomendações
- 🔗 Integração completa entre banco de dados, backend e frontend

---

## 🛠 Tecnologias Utilizadas

- Python 3.11
- FastAPI
- Pandas
- NLTK
- MySQL
- HTML5
- CSS3
- JavaScript

---

## 📂 Estrutura do Projeto

```bash
sentirec/
├── src/
│   ├── api/
│   │   ├── app.py
│   │   ├── coletar.py
│   │   ├── preprocess.py
│   │   ├── recomendacoes.py
│   │   └── db.py
│   └── frontend/
│       ├── index.html
│       ├── style.css
│       └── script.js

⚙️ Como Executar
1️⃣ Clone o repositório
git clone <url-do-repositorio>
cd sentirec
2️⃣ Instale as dependências
pip install -r requirements.txt
3️⃣ Execute a API
uvicorn src.api.app:app --reload
4️⃣ Execute o Frontend

Abra o arquivo index.html diretamente no navegador ou utilize a extensão Live Server no Visual Studio Code.

🔌 Endpoints Disponíveis
GET /

Verifica se a API está em funcionamento.

Resposta:

{
    "mensagem": "API de avaliação de sentimentos Sentirec funcionando com sucesso."
}
GET /avaliacoes

Lista todas as avaliações armazenadas no banco de dados.

GET /recomendar?id_usuario={id}&top_n={n}

Retorna recomendações personalizadas para o usuário informado.

Exemplo:

GET /recomendar?id_usuario=1&top_n=5
🎓 Objetivo Acadêmico

Este projeto foi desenvolvido com fins acadêmicos, demonstrando a aplicação prática de conceitos de:

Engenharia de Dados
Machine Learning
Processamento de Linguagem Natural
Desenvolvimento de APIs
Desenvolvimento Web
👨‍💻 Autor

Felipe Bandeira Lima

Estudante de Análise e Desenvolvimento de Sistemas.
