import streamlit as st
import json
import os
from collections import defaultdict, Counter

st.set_page_config(page_title="Leitura de Leis por Cards", layout="centered")

# 🔐 Login do usuário
usuario = st.text_input("🔐 Nome de usuário:")
if not usuario:
    st.warning("Digite seu nome para continuar.")
    st.stop()

os.makedirs("dados", exist_ok=True)
ARQUIVO_JSON = f"dados/{usuario}_perguntas.json"

if os.path.exists(ARQUIVO_JSON):
    with open(ARQUIVO_JSON, "r", encoding="utf-8") as f:
        dados = json.load(f)
    for d in dados:
        if "vezes_lido" not in d:
            d["vezes_lido"] = 0
else:
    dados = []

st.sidebar.markdown("---")
fonte = st.sidebar.slider("🔠 Tamanho da Fonte (px):", 12, 30, 16)

st.markdown(f"<h1 style='font-size: {fonte + 20}px;'>📚 Leitura de Leis por Cards</h1>", unsafe_allow_html=True)

if 'leituras' not in st.session_state:
    st.session_state.leituras = {}

leis_existentes = sorted(set(d.get("lei", "") for d in dados if d.get("lei")))
concursos_existentes = sorted(set(d.get("concurso", "") for d in dados if d.get("concurso")))

# 🔹 Cadastro de nova pergunta
st.sidebar.header("➕ Cadastrar nova pergunta")
with st.sidebar.form("cadastro_form", clear_on_submit=True):
    concurso = st.selectbox("Concurso", options=[""] + concursos_existentes, index=0)
    concurso_livre = st.text_input("Outro concurso (se novo)")
    lei = st.selectbox("Lei", options=[""] + leis_existentes, index=0)
    lei_livre = st.text_input("Outra lei (se nova)")
    pergunta = st.text_area("Pergunta")
    resposta = st.text_area("Resposta")
    referencia = st.text_input("Referência (Art., Inciso, § etc.)")
    submit = st.form_submit_button("Salvar")

    if submit:
        nova = {
            "concurso": concurso_livre if concurso_livre else concurso,
            "lei": lei_livre if lei_livre else lei,
            "pergunta": pergunta,
            "resposta": resposta,
            "referencia": referencia,
            "vezes_lido": 0
        }
        dados.append(nova)
        with open(ARQUIVO_JSON, "w", encoding="utf-8") as f:
            json.dump(dados, f, ensure_ascii=False, indent=2)
        st.success("✅ Pergunta salva com sucesso!")

st.sidebar.markdown("---")
st.sidebar.markdown("📚 **Filtrar por Concurso e Lei**")
concurso_selecionado = st.sidebar.selectbox("Concurso:", ["Selecionar"] + concursos_existentes)
leis_filtradas = sorted(set(d["lei"] for d in dados if d.get("concurso") == concurso_selecionado)) if concurso_selecionado != "Selecionar" else []
lei_selecionada = st.sidebar.selectbox("Lei:", ["Selecionar"] + leis_filtradas)

filtro_leituras = st.sidebar.selectbox(
    "Filtrar cards por número de leituras:",
    ["Todos", "Nunca lidos", "1 ou mais", "5 ou mais", "10 ou mais"]
)

busca = st.text_input("🔍 Buscar por palavra-chave, artigo, lei ou concurso:")

perguntas_filtradas = []
for i, item in enumerate(dados):
    vezes = item.get("vezes_lido", 0)
    if busca.lower() in item["pergunta"].lower() or busca.lower() in item["referencia"].lower() or busca.lower() in item["lei"].lower() or busca.lower() in item.get("concurso", "").lower():
        if (concurso_selecionado == "Selecionar" or item["concurso"] == concurso_selecionado) and \
           (lei_selecionada == "Selecionar" or item["lei"] == lei_selecionada):
            if (
                filtro_leituras == "Todos" or
                (filtro_leituras == "Nunca lidos" and vezes == 0) or
                (filtro_leituras == "1 ou mais" and vezes >= 1) or
                (filtro_leituras == "5 ou mais" and vezes >= 5) or
                (filtro_leituras == "10 ou mais" and vezes >= 10)
            ):
                perguntas_filtradas.append((i, item))

leituras_por_lei = Counter()
mais_lido_por_lei = {}
for _, item in perguntas_filtradas:
    lei = item.get("lei", "[Sem Lei]")
    leituras_por_lei[lei] += item.get("vezes_lido", 0)
    if lei not in mais_lido_por_lei or item.get("vezes_lido", 0) > mais_lido_por_lei[lei].get("vezes_lido", 0):
        mais_lido_por_lei[lei] = item

if concurso_selecionado != "Selecionar" and lei_selecionada != "Selecionar":
    st.markdown(f"<h2 style='font-size: {fonte + 8}px;'>🎯 Concurso: {concurso_selecionado}</h2>", unsafe_allow_html=True)
    st.markdown(f"<h3 style='font-size: {fonte + 4}px;'>📘 Lei: {lei_selecionada}</h3>", unsafe_allow_html=True)
    for i, item in perguntas_filtradas:
        with st.expander(f"📌 <span style='font-size:{fonte}px'>{item['pergunta']}</span>", unsafe_allow_html=True):
            st.markdown(f"<div style='font-size: {fonte}px;'><b>Resposta:</b> {item['resposta']}</div>", unsafe_allow_html=True)
            st.caption(f"📖 Referência: {item['referencia']}  \n📘 Lei: {item['lei']}  \n🎯 Concurso: {item.get('concurso', '[Sem Concurso]')}")
            col1, col2, col3 = st.columns([1, 1, 1])

            with col1:
                if st.button(f"✅ Lido ({item.get('vezes_lido', 0)}x)", key=f"btn_lido_{i}"):
                    dados[i]["vezes_lido"] = dados[i].get("vezes_lido", 0) + 1
                    with open(ARQUIVO_JSON, "w", encoding="utf-8") as f:
                        json.dump(dados, f, ensure_ascii=False, indent=2)
                    st.rerun()

            with col2:
                with st.expander("✏️ Editar", expanded=False):
                    with st.form(f"form_editar_{i}"):
                        nova_pergunta = st.text_area("Pergunta", value=item["pergunta"])
                        nova_resposta = st.text_area("Resposta", value=item["resposta"])
                        nova_referencia = st.text_input("Referência", value=item["referencia"])
                        nova_concurso = st.text_input("Concurso", value=item["concurso"])
                        nova_lei = st.text_input("Lei", value=item["lei"])
                        confirmar = st.form_submit_button("Salvar alterações")
                        if confirmar:
                            dados[i].update({
                                "pergunta": nova_pergunta,
                                "resposta": nova_resposta,
                                "referencia": nova_referencia,
                                "concurso": nova_concurso,
                                "lei": nova_lei
                            })
                            with open(ARQUIVO_JSON, "w", encoding="utf-8") as f:
                                json.dump(dados, f, ensure_ascii=False, indent=2)
                            st.success("✅ Alterações salvas com sucesso!")
                            st.rerun()

            with col3:
                if st.button("🗑️ Excluir", key=f"excluir_{i}"):
                    dados.pop(i)
                    with open(ARQUIVO_JSON, "w", encoding="utf-8") as f:
                        json.dump(dados, f, ensure_ascii=False, indent=2)
                    st.warning("❌ Card excluído.")
                    st.rerun()

st.sidebar.markdown("---")
st.sidebar.markdown("📊 **Ranking de Leis Mais Lidas**")
mais_lidas = leituras_por_lei.most_common(5)
for lei, total in mais_lidas:
    st.sidebar.markdown(f"**{lei}** — {total} leituras")

st.sidebar.markdown("---")
st.sidebar.markdown("🔥 **Card mais lido por lei**")
for lei, item in mais_lido_por_lei.items():
    st.sidebar.markdown(f"**{lei}** → *{item['pergunta'][:50]}...* ({item['vezes_lido']}x)")
