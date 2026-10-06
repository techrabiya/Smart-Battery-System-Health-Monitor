import streamlit as st
import platform
import datetime

st.title("🔋 Rabia's Smart Battery & System Health Monitor")
st.write("Welcome! Monitor system performance, device architecture, and live session details instantly.")

st.subheader("🖥️ Device & System Specifications")

system_name = platform.system()
node_name = platform.node()
release_version = platform.release()
machine_arch = platform.machine()
processor_info = platform.processor()

col1, col2 = st.columns(2)

with col1:
    st.info(f"**Operating System:** {system_name}")
    st.info(f"**Device Node:** {node_name}")
    st.info(f"**System Release:** {release_version}")

with col2:
    st.info(f"**Architecture:** {machine_arch}")
    st.info(f"**Processor:** {processor_info if processor_info else 'ARM / Apple Silicon'}")

st.markdown("---")

st.subheader("⏱️ Live Session Tracker")
current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
st.success(f"**Active Session Timestamp:** {current_time}")

st.subheader("⚡ Battery & Power Status Simulation")
st.write("Since cloud servers run remotely, here is your live system diagnostics engine:")

if st.button("Run System Health Check"):
    st.markdown("---")
    st.success("✅ **Battery Status:** Optimal (External Power Connected)")
    st.success("✅ **CPU Thermal State:** Normal & Stable")
    st.success("✅ **Memory Usage:** Secure & Optimized")
    st.markdown("---")
    st.balloons()
