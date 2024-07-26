# This is server code to send video and audio frames over TCP
# Import dependencies
import socket
import threading, wave, pyaudio,pickle,struct

# Define hostname, hostip, print that to terminal, and then define port (arbirtrary)
host_name = socket.gethostname()
host_ip = '192.168.14.190'#  socket.gethostbyname(host_name)
print(host_ip)
port = 12345

# def function for audio stream
def audio_stream():
    # Create socket and bind to ip
    server_socket = socket.socket()
    port = 12345
    server_socket.bind((host_ip, port))

    # Listen on socket
    server_socket.listen(5)
    CHUNK = 1024
    wf = wave.open("test.wav", 'rb')

    # create pyaudio object
    p = pyaudio.PyAudio()
    print('server listening at',(host_ip, (port-1)))
   
    # Use pyaudio
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    input=True,
                    frames_per_buffer=CHUNK)

    # Accept socket connection
    client_socket,addr = server_socket.accept()
    print("Accepted Connection!")
 
    data = None
    while True:
        if client_socket:
            while True:
                # Read data from socket
                data = wf.readframes(CHUNK)
                a = pickle.dumps(data)
                message = struct.pack("Q",len(a))+a
                client_socket.sendall(message)
                
t1 = threading.Thread(target=audio_stream, args=())
t1.start()

