/*���ӷ�������
n�����ӣ�ÿ��ÿ�ι����ӵ�һֻ��Ȼ�����n�ݺ�����һ��
�����ӳ�ʼ��������Ϊ���� 

int��result������㵽 n=9 �������֮����� 
*/
#include<stdio.h>
unsigned int loop(short n, short i);

main()
{
	while(1)
	{
		short n = 0;
		unsigned int result = 0;
		scanf("%d",&n);
		if (n == 1) 
			result = 1;
		else
			result = loop(n, n);
		printf ("The initial amount is %d\n",result);	
	}
}
unsigned int loop(short n, short i)
{
	static unsigned int floor = -1;
	if (i == 1)
	{
		//������һ�η���ǰ��ʣ����� 
		do{
			floor++;
		}while (floor % (n - 1) != 0);
		return (floor / (n-1)) * n + 1;
	}
	else
	{
		unsigned int result = 0;
		do{
			result = loop(n, i - 1);
		}while(result % (n - 1) != 0);
		
		return (result / (n-1)) * n + 1;
	}
}
