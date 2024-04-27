from queue import Queue

queue = Queue()


def generate_request(request):
    queue.put(request)
    print(f"Request {request} was added to system")


def process_request():
    if queue.empty():
        print("The queue is empty. There is nothing to process")
    else:
        request = queue.get()
        print("Processing the request: ", request)


counter = 0
while True:
    generate_request(counter)
    process_request()
    counter += 1
