#!/usr/bin/env python3
"""
Simple HTTP server to serve the docs folder
This allows the search-index.json to be loaded via fetch API
"""
import http.server
import socketserver
import os

# Change to the docs directory
os.chdir(os.path.dirname(__file__))

PORT = 8080
Handler = http.server.SimpleHTTPRequestHandler

print(f"""
🚀 N8N Workflows Documentation Server
=====================================

Server running at: http://localhost:{PORT}
Press Ctrl+C to stop the server

Note: This server is for local development only.
For production, use the main application server (python run.py)
""")

try:
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        httpd.serve_forever()
except KeyboardInterrupt:
    print("\n\n👋 Server stopped!")
