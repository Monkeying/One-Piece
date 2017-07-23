"""
python3.5
socket设置
socket属性获取
socket接收
socket发送
"""

int socket(int domain, int type, int protocol)
{
	return socket_fd#返回socket句柄的文件描述符
}

#socket设置
{

	socket_fd.accept()#有连接socket中的接收连接请求
	{
		return socket_fd#在有连接的socket中返回该接收成功的链接socket句柄，不成功返回<=0
	}
	socket_fd.close()#连接句柄关闭
	socket_fd.listen()#有连接socket中的监听连接请求
	socket_fd.bind(addressTubleTuble)#绑定监听的地址，bind之后socket_fd只接收目的地址为该地址的包
	socket_fd.connect(addressTuble)#绑定对端的socket地址，在有连接的socket中
	{
		有连接的
	}
	{
		特别的，对于即bind,又connect的socket_fd.在无连接中，收发的包的目的地址，源地址分别由bind,connect指定。
		绑定地址中的端口号如果为0，代表由系统自动为其分配一个可用的端口号，无连接的socket一般使用这个。
	}
	socket_fd.connect_ex(addressTuble)
	socket_fd.settimeout(value)
	{
		
	}
	socket_fd.setblocking(flag)
	{
		sock.setblocking(True) is equivalent to sock.settimeout(None)
		sock.setblocking(False) is equivalent to sock.settimeout(0.0)#在非阻塞情况下，recv,accept等函数在无数据接受的时候直接返回socket.error，不等待。
	}
}
#socket属性获取
{
	socket_fd.getsockname()
	{
		return addressTuble tuple#返回绑定的地址元组
	}
	socket_fd.getpeername()
	{
		return remote addressTuble tuple#返回远端的地址元组
	}
	socket_fd.fileno()
	{
		return socket_fd’s file descriptor (a small integer), or -1 on failure.#返回socket的文件描述符
	}
	socket_fd.gettimeout()
	{
		Return the timeout in seconds (float) associated with socket operations, or None if no timeout is set.#返回timeout的值，或者None如果setblocking（True)/settimeout(None)
	}
}
#socket数据接收
{
	socket_fd.recv(int bufsize)
	{
		return bytes object representing the data received#返回接受到的字节数据
		bufsize is the maximum amount of data to be received at once#bufsize指定在一次接收中的数据最大长度
		bufsize is better to be power of 2 to match with hardware#bufsize最好是2的幂方数，这样子和硬件结构结合更好
	}
	socket_fd.recvfrom(int bufsize)
	{
		return (bytes,addressTuble) the tuple of bytes objects and addressTuble tuple#返回字节数据和接收源地址元组的元祖
		bufsize is the maximum amount of data to be received at once#bufsize指定在一次接收中的数据最大长度
		bufsize is better to be power of 2 to match with hardware#bufsize最好是2的幂方数，这样子和硬件结构结合更好
	}
	socket_fd.recv_into(buffer,)
	{
		return the number of bytes received#返回接收到的字节总数
		Receive data from the socket, writing it into buffer instead of creating a new bytestring#直接将接收的数据写入buffer中，不再产生bytestring对象
	}
	socket_fd.recvfrom_into(buffer)
	{
		return (nbytes,addressTuble)the number of bytes received, addressTuble tuple#返回一个元组，接收到的字节总数，接收的源地址元组
		Receive data from the socket, writing it into buffer instead of creating a new bytestring#直接将接收的数据写入buffer中，不再产生bytestring对象
	}
}
#socket数据发送
{
	socket_fd.send(bytestring)
	{
		return the number of bytes sent#返回发送出去的字节数，bytestring不一定用一句send能发送成功。需要将返回的数字与bytestring长度进行判断，循环发送
		The socket must be connected to a remote socket#这个socket必须connect到一个远端地址
	}
	socket_fd.sendall(bytestring)
	{
		return None on success. On error, an exception is raised#如果数据全部发送成功，返回None。如果没有全部发送成功则raise一个socket.error
		The socket must be connected to a remote socket#这个socket必须connect到一个远端地址
	}
	socket_fd.sendto(bytestring,addressTuble)
	{
		return the number of bytes sent#返回发送成功的字节数
		The socket_fd should not be connected to a remote socket, since the destination socket is specified by addressTuble#该socket应该是没有connect到一个远端地址的
		The format of addressTuble depended on the domain of this socket #传入地址的格式由该socekt_fd的domain（family地址族）决定
	}
	socket_fd.sendfile(file, offset=0, count=None)
	{
		return the total number of bytes which were sent#返回传送成功的总字节数
		Send a file until EOF#使用socket传输一个文件中的数据直到文件结尾
		file must be a regular file object opened in binary mode#文件必须是常规的二进制文件，并且使用二进制模式打开
		The socket must be of SOCK_STREAM type. Non- blocking sockets are not supported.#该socket必须是面向数据流的，非阻塞的
		offset specified the position of beginning in the file#指定传输流的起始点在文件中的位置
		count specified exact number of bytes to be sent#指定要传输的数据流的长度
	}
}