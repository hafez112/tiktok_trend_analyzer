# TikTok Trend Analyzer Pro - Passenger WSGI
# For cPanel hosting with Phusion Passenger
# By: Eng. Hafez Al-Sulaihi

import sys
import os

# إضافة المجلد للمسار
INTERP = os.path.expanduser("~/venv/bin/python")
if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)

sys.path.insert(0, os.path.dirname(__file__))

# Streamlit app
from streamlit.web.bootstrap import run

def application(environ, start_response):
    """WSGI application wrapper for Streamlit"""
    status = '200 OK'
    headers = [('Content-type', 'text/html; charset=utf-8')]
    start_response(status, headers)

    import threading
    def start_streamlit():
        run(
            main_script_path="app.py",
            command_line=None,
            args=[],
            flag_options={}
        )

    thread = threading.Thread(target=start_streamlit)
    thread.daemon = True
    thread.start()

    return [b"Streamlit app is starting... Please refresh in a few seconds."]
