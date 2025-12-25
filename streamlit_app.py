import streamlit as st

def start_app(pipeline):
    # Заголовок приложения
    st.title("Question Answering App")
    st.write("Сервис использует языковую модель для ответа на вопрос по контексту.")
    st.write("""
        - Модель: `deepset/roberta-base-squad2`
        - Задача: Ответы на вопросы (Question Answering)
        - Источник: [Hugging Face Model Hub](https://huggingface.co/deepset/roberta-base-squad2)
        """)

    # Инициализация пайплайна
    @st.cache_resource
    def load_model():
        return pipeline()

    pipe = load_model()

    # Функция для получения ответа
    def get_answer(question, context):
        result = pipe(question= question, context= context)
        return result

    # Функция для отображения результата
    def display_result(result):
        st.subheader("Результат:")
        st.write(f"**Ответ:** {result['answer']}")
        st.write(f"**Уверенность (score):** {result['score']:.4f}")
        st.write(f"**Начало:** {result['start']}")
        st.write(f"**Конец:** {result['end']}")


    st.header("Задайте вопрос и введите контекст")
    context = st.text_area("Контекст", height=150, placeholder="Введите текст, по которому нужно ответить на вопрос...")
    question = st.text_input("Вопрос", placeholder="Введите вопрос...")
        
    if st.button("Получить ответ"):
        if context and question:
            with st.spinner("Обработка..."):
                result = get_answer(question, context)
            display_result(result)
        else:
            st.warning("Пожалуйста, введите и контекст, и вопрос.")
