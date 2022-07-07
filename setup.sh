mkdir -p ~/.streamlit/

echo "\
[server]\n\
port = $PORT\n\
enableCORS = false\n\
headless = true\n\
server.enableXsrfProtection=false\n\
\n\
[logging]\n\
level="verbose"\n\
\n\
" > ~/.streamlit/config.toml
