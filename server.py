import http.server
import socketserver

PORT = 8000  # 端口号（可修改）

# 设置服务器
Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("", PORT), Handler)

print(f"服务器已启动，访问地址: http://localhost:{PORT}")
httpd.serve_forever()