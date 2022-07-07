mkdir -p ~/.streamlit/

echo "\
[server]\n\
port = $PORT\n\
enableCORS = false\n\
headless = true\n\
enableXsrfProtection=false\n\
\n\
[logger]\n\
level='verbose'\n\
\n\
" > ~/.streamlit/config.toml
