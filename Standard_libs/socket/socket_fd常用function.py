"""
python3.5
socket����
socket���Ի�ȡ
socket����
socket����
"""

int socket(int domain, int type, int protocol)
{
	return socket_fd#����socket������ļ�������
}

#socket����
{

	socket_fd.accept()#������socket�еĽ�����������
	{
		return socket_fd#�������ӵ�socket�з��ظý��ճɹ�������socket��������ɹ�����<=0
	}
	socket_fd.close()#���Ӿ���ر�
	socket_fd.listen()#������socket�еļ�����������
	socket_fd.bind(addressTubleTuble)#�󶨼����ĵ�ַ��bind֮��socket_fdֻ����Ŀ�ĵ�ַΪ�õ�ַ�İ�
	socket_fd.connect(addressTuble)#�󶨶Զ˵�socket��ַ���������ӵ�socket��
	{
		�����ӵ�
	}
	{
		�ر�ģ����ڼ�bind,��connect��socket_fd.���������У��շ��İ���Ŀ�ĵ�ַ��Դ��ַ�ֱ���bind,connectָ����
		�󶨵�ַ�еĶ˿ں����Ϊ0��������ϵͳ�Զ�Ϊ�����һ�����õĶ˿ںţ������ӵ�socketһ��ʹ�������
	}
	socket_fd.connect_ex(addressTuble)
	socket_fd.settimeout(value)
	{
		
	}
	socket_fd.setblocking(flag)
	{
		sock.setblocking(True) is equivalent to sock.settimeout(None)
		sock.setblocking(False) is equivalent to sock.settimeout(0.0)#�ڷ���������£�recv,accept�Ⱥ����������ݽ��ܵ�ʱ��ֱ�ӷ���socket.error�����ȴ���
	}
}
#socket���Ի�ȡ
{
	socket_fd.getsockname()
	{
		return addressTuble tuple#���ذ󶨵ĵ�ַԪ��
	}
	socket_fd.getpeername()
	{
		return remote addressTuble tuple#����Զ�˵ĵ�ַԪ��
	}
	socket_fd.fileno()
	{
		return socket_fd��s file descriptor (a small integer), or -1 on failure.#����socket���ļ�������
	}
	socket_fd.gettimeout()
	{
		Return the timeout in seconds (float) associated with socket operations, or None if no timeout is set.#����timeout��ֵ������None���setblocking��True)/settimeout(None)
	}
}
#socket���ݽ���
{
	socket_fd.recv(int bufsize)
	{
		return bytes object representing the data received#���ؽ��ܵ����ֽ�����
		bufsize is the maximum amount of data to be received at once#bufsizeָ����һ�ν����е�������󳤶�
		bufsize is better to be power of 2 to match with hardware#bufsize�����2���ݷ����������Ӻ�Ӳ���ṹ��ϸ���
	}
	socket_fd.recvfrom(int bufsize)
	{
		return (bytes,addressTuble) the tuple of bytes objects and addressTuble tuple#�����ֽ����ݺͽ���Դ��ַԪ���Ԫ��
		bufsize is the maximum amount of data to be received at once#bufsizeָ����һ�ν����е�������󳤶�
		bufsize is better to be power of 2 to match with hardware#bufsize�����2���ݷ����������Ӻ�Ӳ���ṹ��ϸ���
	}
	socket_fd.recv_into(buffer,)
	{
		return the number of bytes received#���ؽ��յ����ֽ�����
		Receive data from the socket, writing it into buffer instead of creating a new bytestring#ֱ�ӽ����յ�����д��buffer�У����ٲ���bytestring����
	}
	socket_fd.recvfrom_into(buffer)
	{
		return (nbytes,addressTuble)the number of bytes received, addressTuble tuple#����һ��Ԫ�飬���յ����ֽ����������յ�Դ��ַԪ��
		Receive data from the socket, writing it into buffer instead of creating a new bytestring#ֱ�ӽ����յ�����д��buffer�У����ٲ���bytestring����
	}
}
#socket���ݷ���
{
	socket_fd.send(bytestring)
	{
		return the number of bytes sent#���ط��ͳ�ȥ���ֽ�����bytestring��һ����һ��send�ܷ��ͳɹ�����Ҫ�����ص�������bytestring���Ƚ����жϣ�ѭ������
		The socket must be connected to a remote socket#���socket����connect��һ��Զ�˵�ַ
	}
	socket_fd.sendall(bytestring)
	{
		return None on success. On error, an exception is raised#�������ȫ�����ͳɹ�������None�����û��ȫ�����ͳɹ���raiseһ��socket.error
		The socket must be connected to a remote socket#���socket����connect��һ��Զ�˵�ַ
	}
	socket_fd.sendto(bytestring,addressTuble)
	{
		return the number of bytes sent#���ط��ͳɹ����ֽ���
		The socket_fd should not be connected to a remote socket, since the destination socket is specified by addressTuble#��socketӦ����û��connect��һ��Զ�˵�ַ��
		The format of addressTuble depended on the domain of this socket #�����ַ�ĸ�ʽ�ɸ�socekt_fd��domain��family��ַ�壩����
	}
	socket_fd.sendfile(file, offset=0, count=None)
	{
		return the total number of bytes which were sent#���ش��ͳɹ������ֽ���
		Send a file until EOF#ʹ��socket����һ���ļ��е�����ֱ���ļ���β
		file must be a regular file object opened in binary mode#�ļ������ǳ���Ķ������ļ�������ʹ�ö�����ģʽ��
		The socket must be of SOCK_STREAM type. Non- blocking sockets are not supported.#��socket�����������������ģ���������
		offset specified the position of beginning in the file#ָ������������ʼ�����ļ��е�λ��
		count specified exact number of bytes to be sent#ָ��Ҫ������������ĳ���
	}
}