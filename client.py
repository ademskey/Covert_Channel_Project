# Used libraries
import socket,os
import threading, wave, pyaudio, pickle,struct
import wave
import socket
import threading	
import pyaudio
import pickle
import struct
import os

# Define hostname, host_ip
host_name = socket.gethostname()
host_ip = '172.20.10.5'#  socket.gethostbyname(host_name)
port = 12345
print(host_ip)
output_filename = 'output.wav'

# Create a wave file writer


def audio_stream():
	p = pyaudio.PyAudio()
	CHUNK = 1024
	stream = p.open(format=p.get_format_from_width(2),
					channels=2,
					rate=44100,
					output=True,
					frames_per_buffer=CHUNK)
	
	p = pyaudio.PyAudio()
	CHUNK = 1024
	
	# Define audio parameters
	FORMAT = p.get_format_from_width(2)
	CHANNELS = 2
	RATE = 44100

	wf = wave.open(output_filename, 'wb')
	wf.setnchannels(CHANNELS)
	wf.setsampwidth(p.get_sample_size(FORMAT))
	wf.setframerate(RATE)			
	
	# create socket
	client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	socket_address = (host_ip, port)
	print('server listening at',socket_address)
	client_socket.connect((socket_address))
	print("CLIENT CONNECTED TO",socket_address)
	data = b""
	payload_size = struct.calcsize("Q")

	# Create a wave file writer
	wf = wave.open(output_filename, 'wb')
	wf.setnchannels(CHANNELS)
	wf.setsampwidth(p.get_sample_size(FORMAT))
	wf.setframerate(RATE)

	data = b""
	payload_size = struct.calcsize("Q")

	while True:
		try:
			while len(data) < payload_size:
				packet = client_socket.recv(4*1024)  # 4K
				if not packet: break
				data += packet
			if not data:
				break
			packed_msg_size = data[:payload_size]
			data = data[payload_size:]
			msg_size = struct.unpack("Q", packed_msg_size)[0]
			while len(data) < msg_size:
				data += client_socket.recv(4*1024)
			frame_data = data[:msg_size]
			data = data[msg_size:]
			frame = pickle.loads(frame_data)
			
			# Write audio data to the wave file
			wf.writeframes(frame)

		except Exception as e:
			print(f"Exception occurred: {e}")
			break

	wf.close()
	client_socket.close()

audio_stream()
print('Audio stream closed and file saved as', output_filename)
os._exit(1)

	
t1 = threading.Thread(target=audio_stream, args=())
t1.start()


