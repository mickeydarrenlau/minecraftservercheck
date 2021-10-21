import streamlit as st
from mcstatus import MinecraftServer

st.image('Minecraft-server-check.png')

st.title("""
Get info about the largest minecraft servers on Earth :earth_africa:
""")

server_name_list = {'hub.manacube.net':'https://manacube.com/',
                    'hub.lemoncloud.net':'https://lemoncloud.net',
                    'PURPLEPRISON.NET':'https://www.purpleprison.co/',
                    'join.miningdead.com':'https://havoc.games/',
                    'hub.mineville.org':'https://manacube.com/',
                    'og.universemc.us':'https://universemc.us/',
                    'Herobrine.org':'https://herobrine.org/',
                    'bedwars.games':'https://blockdrop.org/index.php'}

for key, value in server_name_list.items():
    server = MinecraftServer.lookup(key)
    server_status = server.status()

    st.write('----------------------')

    st.title(f'{key} server')

    # Calculate percentage of online players against total joined players
    drop = round((int(server_status.players.online) / (int(server_status.players.max)) * 100))

    col1, col2, col3 = st.columns(3)

    col1.metric('Total players in server', server_status.players.max, delta='> 500 players')
    col2.metric('Players currently online', server_status.players.online, delta=f'{drop}% of members')
    col3.metric('Ping', server_status.latency, delta='Over 100ms', delta_color='inverse')

    st.write(f'For more info about **{key}** server, go to [{value}]({key})')
