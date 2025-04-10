from django.shortcuts import render

# Create your views here.
import os
import subprocess
import datetime
import pytz
from django.http import HttpResponse

def htop_view(request):
    full_name = "John Doe"  # Replace with your actual name
    username = os.getlogin()
    
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S %Z')

    try:
        top_output = subprocess.check_output(['top', '-b', '-n', '1']).decode('utf-8')
    except Exception as e:
        top_output = f"Error running top command: {str(e)}"

    response = f"""
    <html>
    <head><title>/htop</title></head>
    <body style="font-family: monospace; white-space: pre-wrap;">
        <h2>System Monitor (/htop)</h2>
        <strong>Name:</strong> {full_name}<br>
        <strong>Username:</strong> {username}<br>
        <strong>Server Time (IST):</strong> {server_time}<br><br>
        <h3>Top Output</h3>
        <pre>{top_output}</pre>
    </body>
    </html>
    """
    return HttpResponse(response)

