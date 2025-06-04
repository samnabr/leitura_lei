**Leitura de Leis por Cards**:

---

``
# 📚 Leitura de Leis por Cards

Aplicativo web construído com **Streamlit** para auxiliar no estudo de leis, normas e regulamentos para concursos públicos.  
Cada usuário pode cadastrar **leis**, associar **perguntas e respostas**, e visualizar o conteúdo em **cards interativos**, com controle de leitura e filtros inteligentes.

---

## 🔧 Funcionalidades

- 🔐 Acesso individual por nome de usuário (dados isolados por pessoa)
- 🧾 Cadastro de:
  - Concurso
  - Lei
  - Pergunta
  - Resposta
  - Referência legal (Artigo, Inciso, §)
- 🧠 Cards interativos com:
  - Marcação de leitura (com contador)
  - Edição e exclusão
- 🔍 Filtros por:
  - Concurso
  - Lei
  - Palavra-chave
  - Quantidade de vezes lido
- 📊 Ranking de leis mais lidas
- 🌙 Controle de tamanho da fonte (acessibilidade)

---

## 🚀 Como acessar

Acesse o aplicativo diretamente pelo navegador:  
🔗 [https://lei-card.streamlit.app](https://lei-card.streamlit.app)

---

## 👨‍💻 Como rodar localmente

### 1. Clone o repositório:

```bash
git clone https://github.com/samnabr/leitura_lei.git
cd leitura_lei
````

### 2. Crie e ative um ambiente virtual (opcional):

```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
```

### 3. Instale as dependências:

```bash
pip install -r requirements.txt
```

### 4. Rode o app:

```bash
streamlit run main.py
```

---

## 🗂️ Estrutura dos arquivos

```
leitura_lei/
├── dados/                     # Dados salvos por usuário (JSON)
│   └── joao_perguntas.json
├── main.py                   # Arquivo principal da aplicação
├── requirements.txt          # Dependências do projeto
└── README.md                 # Este documento
```

---

## ✅ Requisitos

* Python 3.8+
* Streamlit

---

## 📄 Licença

Este projeto é de uso educacional. Pode ser adaptado e reutilizado livremente com os devidos créditos.

---

## ✨ Autor(a)

Desenvolvido por **Samnabr** para fins de estudo e organização pessoal.
Contribuições são bem-vindas! 🙌

```

---


```
