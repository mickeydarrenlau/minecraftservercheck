import streamlit as st
from mcstatus import MinecraftServer

st.set_page_config('DarrenMC Network Status',':earth_africa:')

st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)

cols1, cols2, cols3 = st.columns([1, 6, 1])

with cols1:
    st.write("")

with cols2:
    st.title("""
            DarrenMC Network Status
            """)

with cols3:
    st.write("")

server_name_list = {'mc.darren.ee.eu.org': "Main Hub"}

for key, value in server_name_list.items():
    try:
        server = MinecraftServer.lookup(key)
        server_status = server.status()

        st.write('----------------------')
        st.title(f'{value} server')

        # Calculate percentage of online players against total joined players
        col1, col2, col3 = st.columns(3)

        # Filtering total players
        if server_status.players.max > 1000:
            col1.metric('Total signed players', server_status.players.max, delta='')
        else:
            col1.metric(f'Total signed players', server_status.players.max, delta=f'')

        # Filtering active/currently online players
        drop = round((int(server_status.players.online) / (int(server_status.players.max)) * 100))
        if drop > 10:
            col2.metric('Players online', f'{drop}%', delta=f'')
        else:
            col2.metric('Players online', f'{drop}%', delta=f'> half of members online')


        # Filtering latency
        if round(server_status.latency) > 300:
            col3.metric('Ping', round(server_status.latency), delta='Ping over 300ms', delta_color='inverse')
        else:
            col3.metric('Ping', round(server_status.latency), delta='Ping under 300ms')
    except:
        pass
