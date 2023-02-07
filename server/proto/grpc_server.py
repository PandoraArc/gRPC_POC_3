import grpc
import json
import time
import server.proto.coffee_pb2 as coffee_pb2
import server.proto.coffee_pb2_grpc as coffee_pb2_grpc
# from . import coffee_pb2
# from . import coffee_pb2_grpc

from concurrent import futures

def pingPongJson(jsonIn):
    try: 
        if isinstance(jsonIn, dict):
            return jsonIn
        elif isinstance(jsonIn, str):
            json_dict = json.loads(jsonIn)
            response_json = json.dumps(json_dict)
            return response_json
    except Exception as e:
        return f"pingPongJson fail {e}"
    

class CoffeeServicer(coffee_pb2_grpc.CoffeeServicer):
    def OrderCoffee(self, request, context):
        print("We got some coffee order")
        print("request: ", request)
        try:
            response = coffee_pb2.CoffeeResponse()
            response.responseJsonStr = pingPongJson(request.requestJsonStr)
        except Exception as e:
            print(f"Exception {e}")
        return response

def grpc_init():
    socket = 'unix:///home/parinthon/Documents/github/gRPC_POC_3/server/proto/grpc.sock'
    #socket = '[::]:50052'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    coffee_pb2_grpc.add_CoffeeServicer_to_server(CoffeeServicer(), server)
    server.add_insecure_port(socket)
    print('Server listening on: ', socket)
    server.start()
    server.wait_for_termination()
    

# if "__main__" == __name__:
#     grpc_init()