import streamlit as st

def load_css():
    with open("style.css") as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
    st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

def st_button(icon, url, label, iconsize):
    if icon == 'whatsapp':
        button_code = f'''
        <p>
            <a href={url} class="btn btn-outline-primary btn-lg btn-block" type="button" aria-pressed="true">
                <svg xmlns="http://www.w3.org/2000/svg" width={iconsize} height={iconsize} fill="currentColor" class="bi bi-whatsapp" viewBox="0 0 16 16">
                    <path d="M12.9 2.1a7.828 7.828 0 0 0-5.6-2.3c-4.4.6-7.8 5-8.4 9.4a7.828 7.828 0 0 0 2.3 5.6l.2.2-1.2 3.7 3.7-1.2.2.2a7.828 7.828 0 0 0 5.6-2.3c4.4-4.4 5-7.8 5-8.4a7.828 7.828 0 0 0-2.3-5.6zm-1.8 12.4l-1.1-1.1c-.3-.3-.8-.4-1.2-.2-.6.2-3.6 1.9-4.2 2.2-.4.2-.8.1-1.2-.2L2.1 12c-.3-.3-.5-.6-.5-1s.2-.8.5-1l1.3-1.3c-.2-.6-.3-1.2-.2-1.8s.4-1.2.9-1.7c1-.9 2.3-1.3 3.6-1.1.4.1.8.2 1.2.4.3.2.7.1 1-.1s.6-.5.7-.9c.1-.4 0-.8-.2-1.2s-.5-.7-.9-.8c-1.2-.4-2.5-.1-3.5.9-1.1 1-1.6 2.5-1.5 4.1.1 1.6 1 3.1 2.4 4.2 1.3 1 2.8 1.6 4.3 1.6 1.2-.1 2.3-.5 3.2-1.2.2-.1.4-.3.6-.4s.3-.4.4-.6.2-.4.3-.6c.1-.2.1-.4.1-.6s0-.4-.1-.6zm-2.3-1.9c-.3 0-.7 0-1 .1-.7.1-1.4.3-2 .7-.1.1-.3.2-.4.4s-.2.4-.2.6c0 .2 0 .4.1.6s.2.3.4.4c.2.2.4.2.6.2.5 0 1 0 1.5-.4s.8-.8.8-1.4c0-.7-.4-1.3-.9-1.8-.5-.4-1.1-.7-1.8-.7zm-3.2 0c-.3 0-.7 0-1 .1-.7.1-1.4.3-2 .7-.1.1-.3.2-.4.4s-.2.4-.2.6c0 .2 0 .4.1.6s.2.3.4.4c.2.2.4.2.6.2.5 0 1 0 1.5-.4s.8-.8.8-1.4c0-.7-.4-1.3-.9-1.8-.4-.4-1-.7-1.7-.7z"/>
                </svg>  
                {label}
            </a>
        </p>'''

    return st.sidebar.markdown(button_code, unsafe_allow_html=True)