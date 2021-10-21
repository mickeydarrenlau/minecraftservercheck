import streamlit as st
from mcstatus import MinecraftServer

st.image('Minecraft-server-check.png')

st.title("""
Get Minecraft server latency and online player count 
""")

server_name = st.text_input('Enter host link and port',
                            help='Example: https://example.org:1234')

search = st.button(label='Search')

if search:
    # Initialize server search connection
    server = MinecraftServer.lookup(server_name)
    server_status = server.status()

    # Calculate percentage of online players against total joined players
    drop = round((int(server_status.players.online)/2000)*100)

    col1, col2 = st.columns(2)

    col1.metric('Players online', server_status.players.online, delta=f'{drop}% of all signed players')
    col2.metric('Ping', server_status.latency, delta= 'Over 100ms', delta_color= 'inverse')
