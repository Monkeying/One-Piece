/*猴子分桃问题
n个猴子，每个每次过来扔掉一只，然后均分n份后拿走一份
问桃子初始总数起码为多少 

int型result最多能算到 n=9 的情况，之后溢出 
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
		//测出最后一次分配前的剩余个数 
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
