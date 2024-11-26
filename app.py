import streamlit as st
from PIL import Image

# Configuración inicial
st.set_page_config(page_title="Asociación Latino-Americana de Química Medicinal", layout="wide")

# Menú de navegación
menu = ["Página Principal", "Miembros y Consejo Directivo", "Convocatoria al Evento", "Agradecimientos y Contacto"]
seleccion = st.sidebar.selectbox("Navegación", menu)

# Página Principal
if seleccion == "Página Principal":
    st.title("Asociación Latino-Americana de Química Medicinal")
    #st.image("ALAQMED1.PNG", caption="26/11/2025", use_column_width=True)
    with st.container():
    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
    st.image("ALAQMED1.PNG", caption="Logo Principal", width=300)
    st.markdown("</div>", unsafe_allow_html=True)

    st.header("Misión")
    st.write("""
    Promover el desarrollo de la química medicinal en América Latina mediante la colaboración entre científicos, 
    la difusión del conocimiento, y la formación de una red sólida que impulse la innovación en el campo.
    """)
    
    st.header("Visión")
    st.write("""
    Ser una organización líder en América Latina que fomente la investigación y la aplicación de la química medicinal 
    para resolver problemas globales en salud.
    """)
    
    st.header("Objetivos")
    st.write("""
    - Fomentar la colaboración entre investigadores en química medicinal.
    - Difundir avances científicos mediante publicaciones y congresos.
    - Apoyar el desarrollo de jóvenes investigadores.
    """)

# Página de Miembros y Consejo Directivo
elif seleccion == "Miembros y Consejo Directivo":
    st.title("Miembros y Consejo Directivo")
    st.subheader("Consejo Directivo")
    st.write("""
    - **Presidente:** Dr. Juan Pérez
    - **Vicepresidente:** Dra. María López
    - **Secretario:** Dr. Carlos Sánchez
    - **Tesorero:** Dra. Ana Gómez
    """)
    st.subheader("Miembros")
    st.write("""
    - Investigadores asociados de América Latina
    - Colaboradores internacionales
    - Estudiantes y jóvenes científicos
    """)

# Página de Convocatoria al Evento
elif seleccion == "Convocatoria al Evento":
    st.title("Convocatoria al Evento")
    st.subheader("Próximo Congreso de Química Medicinal")
    st.write("""
    **Fecha:** 20-22 de junio de 2025  
    **Lugar:** Lima, Perú  
    **Condiciones para Participar:**  
    - Ser miembro activo de la Asociación.  
    - Enviar un resumen del trabajo antes del 15 de marzo de 2025.  
    - Realizar el pago de inscripción antes del 30 de abril de 2025.  
    """)
    st.subheader("Fechas Importantes")
    st.write("""
    - Apertura de inscripciones: 1 de enero de 2025  
    - Fecha límite para envío de resúmenes: 15 de marzo de 2025  
    - Notificación de aceptación: 10 de abril de 2025  
    - Fecha límite de inscripción: 30 de abril de 2025  
    """)

# Página de Agradecimientos y Contacto
elif seleccion == "Agradecimientos y Contacto":
    st.title("Agradecimientos")
    st.write("""
    Agradecemos a todos los miembros, patrocinadores y colaboradores que hacen posible nuestras actividades.  
    Juntos, avanzamos hacia un futuro mejor en la investigación química y medicinal.
    """)
    
    st.subheader("Contacto")
    st.write("""
    - **Correo Electrónico:** contacto@quimedicinal.org  
    - **Teléfono:** +52 555 123 4567  
    """)
