from fastapi import FastAPI, status, Request
from fastapi.responses import JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
import socket
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

app = FastAPI()

# Mount the static files directory
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def read_index():
    return FileResponse("static/index.html")

@app.post("/send-command", status_code=status.HTTP_204_NO_CONTENT)
async def send_command(request: Request):
    data = await request.json()
    command = data.get("command")

    if not command:
        logging.error("No command provided")
        return JSONResponse(content={"error": "No command provided"}, status_code=status.HTTP_400_BAD_REQUEST)

    logging.info(f"Received command: {command}")

    ip = "127.0.0.1"
    port = 49000

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(3.0)

        msg = 'CMND\x00'  # Sending a command (with terminating null byte)
        msg += command  # the command to send
        msg = msg.encode('utf-8')  # convert from unicode to utf-8 encoded string
        print(msg)
        sock.sendto(msg, (ip, port))

        logging.info(f"Command sent to {ip}:{port}")

        sock.close()
    except Exception as e:
        logging.error(f"Failed to send command: {e}")
        return JSONResponse(content={"error": "Failed to send command"}, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return JSONResponse(content={"message": "Command sent successfully"}, status_code=status.HTTP_200_OK)
