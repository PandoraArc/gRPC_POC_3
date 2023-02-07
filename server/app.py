from server import create_app
import multiprocessing
from server.proto.grpc_server import grpc_init

app = create_app()
t = multiprocessing.Process(target=grpc_init)
t.start()

if __name__ == "__main__":
    app.run()
    #t.start()