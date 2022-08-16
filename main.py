import grpc
import test_pb2 as tpb
import test_pb2_grpc as tpbg


def run():
    #como cliente nos conectamos al servidor grpc 
    # que esta actualmente en nuestro local en un puerto 50052
    with grpc.insecure_channel('localhost:50052') as channel:
        stub = tpbg.SquareRootServiceStub(channel)
        response = stub.squareRoot(tpb.Number(input=2))
        print(response.resulta)

if __name__ == '__main__':
    run()
