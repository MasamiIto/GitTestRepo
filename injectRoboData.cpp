/************************************************************************************
* InfluxDB注入データファイル robo.txtを作成する
************************************************************************************/
#include <stdio.h>
#include <string.h>
#include <time.h>
#include <math.h>
#include <sys/time.h>
#include <unistd.h>

char measure[100];
#define MEASURE  "axis"
#define DBFILE  "robo.txt"

/************************************************************************************

************************************************************************************/
int main(void) {
  	struct timespec curTime;
	char	postStr[1024];
	char	wk[256];
	double  J[6];
	int		key;
	int     N = 10;
	int		i=0;
	double  A;
	double  t,theta;

	key =100;
	A = 100.0;
	while(1){
  		clock_gettime( CLOCK_REALTIME , &curTime );
  		printf("TIME= %10ld.%09ld\n", curTime.tv_sec, curTime.tv_nsec);
		i++;

		theta = ((double)i * 2.0*M_PI / (double)N );
		J[0] = A * sin(theta);
		J[1] = A * cos(theta);
		J[2] = A * exp((double)i  / (double)N);
		J[3] = A * sin(theta+M_PI/4);
		J[4] = A * cos(theta+M_PI/4);
		J[5] = A * exp((double)i / (double)N);
		printf("%3d :%6.2f %6.2f %6.2f %6.2f %6.2f %6.2f ", i, J[0], J[1], J[2], J[3], J[4], J[5]);
  		printf("TIME= %10ld.%09ld\n", curTime.tv_sec+i, curTime.tv_nsec);

		strcpy( postStr , "curl -i -XPOST http://172.17.0.2:8086/write?db=roboDB --data-binary "  );
		sprintf( wk , "'axis,KEY=%d ", key+i   ); strcat( postStr , wk ); 
		sprintf( wk , "J1=%f,"   , J[0]  ); strcat( postStr , wk );
		sprintf( wk , "J2=%f,"   , J[1]  ); strcat( postStr , wk );
		sprintf( wk , "J3=%f,"   , J[2]  ); strcat( postStr , wk );
		sprintf( wk , "J4=%f,"   , J[3]  ); strcat( postStr , wk );
		sprintf( wk , "J5=%f,"   , J[4]  ); strcat( postStr , wk );
		sprintf( wk , "J6=%f "   , J[5]  ); strcat( postStr , wk );
  		sprintf( wk , "%10ld%09ld '", curTime.tv_sec, curTime.tv_nsec); strcat( postStr, wk );
//		printf( "%s\n", postStr );
		system(  postStr );
		sleep(1);
	}
	return 0;
}
/************************************************************************************
*
************************************************************************************/
int main2 (void) {
  	struct timespec curTime;
	char	postStr[1024];
	char	wk[256];
	double  J[6];
	int		key;

	J[0]=1.234;
	key =100;
	while(1){
  		clock_gettime( CLOCK_REALTIME , &curTime );
  		printf("TIME= %10ld.%09ld\n", curTime.tv_sec, curTime.tv_nsec);

		strcpy( postStr , "curl -i -XPOST http://172.17.0.2:8086/write?db=roboDB --data-binary "  );
		sprintf( wk , "'axis,KEY=%d ", key   ); strcat( postStr , wk ); 
		sprintf( wk , "J1=%-6.2f"   , J[0]  ); strcat( postStr , wk );
  		sprintf( wk , "%10ld%09ld '", curTime.tv_sec, curTime.tv_nsec); strcat( postStr, wk );
//		printf( "%s\n", postStr );
		system(  postStr );
		sleep(1);
	}
	return 0;
}
