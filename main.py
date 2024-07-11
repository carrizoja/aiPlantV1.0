import streamlit as st
from openai_client import get_botanical_response


# Add a slight gradient background to the app
st.markdown("""
    <style>
    .reportview-container {
        background: linear-gradient(to right, #dae2f8, #d6a4a4);
    }
    .footer {
        font-size: 16px;
        text-align: center;
    </style>
""", unsafe_allow_html=True)

# Add an image at the top
image_url = "https://res.cloudinary.com/ijac-it-solutions/image/upload/v1720718438/img/aiplant/cvzoewtwyznypvddtsfr.png"  # Replace with your image URL
#st.image(image_url, caption="Nature at its best", use_column_width=True, width=300)

# Custom HTML for image with specific width and height
st.markdown(f"""
    <img src="{image_url}" alt="Nature at its best" style="width:300px;height:300px;">
    """, unsafe_allow_html=True)

st.title("Bienvenido/a a Ai Plant 🌿")
st.write("¡Hacé tu pregunta sobre botánica y recibí una respuesta experta!")

# user input
user_input = st.text_input("Escribe tu pregunta:")

if st.button("Preguntar"):
    if user_input:
        # Generate prompt for chatbot
        prompt = f"Como experto en botánica, necesito que respondas las preguntas de estudiantes de escuela media o secundaria de una forma amigable, amena y resumida en 150 palabras. Pregunta: {user_input}"
        response = get_botanical_response(prompt)
        st.write(response)
    else:
        st.write("Por favor, ingresa una pregunta.")


# Add a section explaining how the app works
st.header("¿Cómo funciona esta App?")
st.write("""
Esta aplicación utiliza inteligencia artificial para responder preguntas sobre botánica. Simplemente, escribí tu pregunta en el campo de texto y presiona el botón "Preguntar". Nuestro sistema de IA (entrenado por expertos en botánica) analizará tu pregunta y te proporcionará una respuesta detallada y precisa.

El proceso es el siguiente:
1. Escribí tu pregunta sobre botánica en el campo provisto.
2. Haz clic en el botón "Preguntar".
3. La aplicación procesará tu pregunta utilizando nuestro avanzado modelo de IA.
4. Recibirás una respuesta a tu pregunta en pocos segundos.

¡Es así de simple! Probá ahora y expandí tu conocimiento sobre el maravilloso mundo de las plantas.""")

# Footer
st.markdown("""
    <style>
    .footer {
        font-size: 16px;
        text-align: center;
        margin-top: 100px;
    }
    </style>
    <div class="footer">© 2024 Ai Plant. Todos los derechos reservados.</div>
    """, unsafe_allow_html=True)
    