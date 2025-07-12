import streamlit as st

st.set_page_config(page_title="Viabilidad de Viaje Uber", page_icon="🚗")
st.title("🚗 Calculadora de Viabilidad de Viaje - Uber")

valor_viaje = st.number_input("💰 Valor del viaje (CLP)", min_value=0)
kilometros = st.number_input("📏 Distancia estimada del viaje (km)", min_value=0.0)

rendimiento_km_l = 18  # km por litro
precio_bencina = 1300  # CLP por litro

if st.button("Calcular Viabilidad"):
    litros = kilometros / rendimiento_km_l
    costo = litros * precio_bencina
    ganancia = valor_viaje - costo

    st.markdown("---")
    st.write(f"⛽ **Litros usados:** {litros:.2f} L")
    st.write(f"💸 **Costo de bencina:** ${costo:,.0f} CLP")
    st.write(f"📈 **Ganancia neta:** ${ganancia:,.0f} CLP")

    if ganancia > 0:
        st.success("✅ El viaje es **VIABLE**.")
    else:
        st.error("❌ El viaje **NO es viable**.")
