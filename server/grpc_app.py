import time
import uwsgi
import psutil
import multiprocessing
import subprocess
import signal
import os
from flask import Blueprint
from server.proto.grpc_server import grpc_init

bp = Blueprint('grpc', __name__, url_prefix="/grpc")

@bp.route("/")
def hello_grpc():
    return "hello, grpc"

# @bp.route("/start", methods=['GET'])
# def start_server_grpc():
#     try:
#         t = multiprocessing.Process(target=grpc_init)
#         t.start()
#         pid = t.pid
#         # p1 = subprocess.Popen(['python', 'grpc_initor.py'])
#         # pid = p1.pid
#         print(f"start suscess pid:{pid}")
#         with open("./server/proto/pid.txt", "w") as file:
#             file.write(str(pid))
#         return f"suscess pid {str(pid)}"  
    
#     except KeyboardInterrupt:
#         print("Kill all processes")
    
#     return f"suscess pid {str(pid)}"


# @bp.route("/stop", methods=['GET'])
# def stop_server_grpc():
#     with open("./server/proto/pid.txt", "r") as file:
#         pid = int(file.readline())
#     os.kill(pid, signal.SIGTERM)
#     uwsgi.reload()
#     return f"kill suscess, grpc_process_id {pid}"


# @bp.route("/status", methods=['GET'])
# def status_server_grpc():
#     with open("./server/proto/pid.txt", "r") as file:
#         pid = int(file.readline())
#     if psutil.pid_exists(pid):
#         print("a process with pid %d exists" % pid)
#         res = "a process with pid %d exists" % pid
#     else:
#         print("a process with pid %d does not exist" % pid)
#         res = "a process with pid %d does not exist" % pid
    
#     return res