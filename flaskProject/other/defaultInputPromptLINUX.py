# NOTE: This may also work in OSX with readline or pyreadline installed
# Create Python venv if needed:
# virturalenv <dir_name>
# Install pyreadline:
# pip install pyreadline

def default_input(prompt, prefill='Default String'):
    readline.set_startup_hook(lambda: readline.insert_text(prefill))
    try:
        return raw_input(prompt)
    finally:
        readline.set_startup_hook()
