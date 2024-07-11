import streamlit as st
from openai_client import get_botanical_response


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
        prompt = f"Como experto en botánica, necesito que respondas las preguntas de estudiantes de escuela media o secundaria de una forma amigable, amena y resumida en no más de 200 tokens. Pregunta: {user_input}"
        response = get_botanical_response(prompt)
        st.write(response)
    else:
        st.write("Por favor, ingresa una pregunta.")

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
    