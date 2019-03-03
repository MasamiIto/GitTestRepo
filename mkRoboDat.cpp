/************************************************************************************
* InfluxDB注入データファイル robo.txtを作成する
************************************************************************************/
#include <stdio.h>
#include <string.h>
#include <time.h>
#include <math.h>
#include <unistd.h>


char measure[100];
#define MEASURE  "axis"
#define DBFILE  "robo.txt"

/************************************************************************************
*
************************************************************************************/
int main(void) {
	FILE 	*fp;
	char	fname[128];
  	struct timespec curTime;
	double	J[6];
	double  A;
	double  t,theta;
//	int     N = 100;
	int     N = 10;


	
	strcpy(  measure , MEASURE );
	strcpy(  fname , DBFILE );

	if( NULL==(fp=fopen( fname , "w" ))){
		printf("**ERR**:OPEN [%s]\n", fname );
		return -1;
	}	
	A = 100.0;
  	clock_gettime( CLOCK_REALTIME , &curTime );
  	printf("TIME= %10ld.%09ld\n", curTime.tv_sec, curTime.tv_nsec);
	printf( "%s \n", measure );
	for( int i=0;i<N ; i++ ){
//  		clock_gettime( CLOCK_REALTIME , &curTime );

		theta = ((double)i * 2.0*M_PI / (double)N );
		J[0] = A * sin(theta);
		J[1] = A * cos(theta);
		J[2] = A * exp((double)i  / (double)N);
		J[3] = A * sin(theta+M_PI/4);
		J[4] = A * cos(theta+M_PI/4);
		J[5] = A * exp((double)i / (double)N);
		printf("%3d :%6.2f %6.2f %6.2f %6.2f %6.2f %6.2f ", i, J[0], J[1], J[2], J[3], J[4], J[5]);
  		printf("TIME= %10ld.%09ld\n", curTime.tv_sec+i, curTime.tv_nsec);
/*
		fprintf( fp , "%s,KEY=%d J1=%-6.2f  %10ld%09ld \n", measure, i,J[0], curTime.tv_sec+i, curTime.tv_nsec);
		fprintf( fp , "%s,KEY=%d J2=%-6.2f  %10ld%09ld \n", measure, i,J[1], curTime.tv_sec+i, curTime.tv_nsec);
		fprintf( fp , "%s,KEY=%d J3=%-6.2f  %10ld%09ld \n", measure, i,J[2], curTime.tv_sec+i, curTime.tv_nsec);
		fprintf( fp , "%s,KEY=%d J4=%-6.2f  %10ld%09ld \n", measure, i,J[3], curTime.tv_sec+i, curTime.tv_nsec);
		fprintf( fp , "%s,KEY=%d J5=%-6.2f  %10ld%09ld \n", measure, i,J[4], curTime.tv_sec+i, curTime.tv_nsec);
		fprintf( fp , "%s,KEY=%d J6=%-6.2f  %10ld%09ld \n", measure, i,J[5], curTime.tv_sec+i, curTime.tv_nsec);
*/
		fprintf( fp , "%s,KEY=%d J1=%f,J2=%f,J3=%f,J4=%f,J5=%f,J6=%f", measure,i, J[0], J[1], J[2], J[3], J[4], J[5]);
 		fprintf( fp , " %10ld%09ld\n", curTime.tv_sec+i, curTime.tv_nsec);
//		sleep( 1 );
	}
	fclose( fp );
	return 0;
}
/************************************************************************************
*
************************************************************************************/
int main2(void) {
	FILE 	*fp;
	char	fname[128];
  	struct timespec curTime;
	double	J[6];
	double  A;
	double  t,theta;
//	int     N = 100;
	int     N = 10;


	
	strcpy(  measure , MEASURE );
	strcpy(  fname , DBFILE );

	if( NULL==(fp=fopen( fname , "w" ))){
		printf("**ERR**:OPEN [%s]\n", fname );
		return -1;
	}	
	A = 100.0;
  	clock_gettime( CLOCK_REALTIME , &curTime );
  	printf("TIME= %10ld.%09ld\n", curTime.tv_sec, curTime.tv_nsec);
	printf( "%s \n", measure );
	for( int i=0;i<N ; i++ ){

		theta = ((double)i * 2.0*M_PI / (double)N );
		J[0] = A * sin(theta);
		J[1] = A * cos(theta);
		J[2] = A * exp((double)i  / (double)N);
		J[3] = A * sin(theta+M_PI/4);
		J[4] = A * cos(theta+M_PI/4);
		J[5] = A * exp((double)i / (double)N);
		printf("%3d :%6.2f %6.2f %6.2f %6.2f %6.2f %6.2f ", i, J[0], J[1], J[2], J[3], J[4], J[5]);
  		printf("TIME= %10ld.%09ld\n", curTime.tv_sec+i, curTime.tv_nsec);

		fprintf( fp , "%s,KEY=%d J1=%-6.2f  %10ld%09ld \n", measure, i,J[0], curTime.tv_sec+i, curTime.tv_nsec);
		fprintf( fp , "%s,KEY=%d J2=%-6.2f  %10ld%09ld \n", measure, i,J[1], curTime.tv_sec+i, curTime.tv_nsec);
		fprintf( fp , "%s,KEY=%d J3=%-6.2f  %10ld%09ld \n", measure, i,J[2], curTime.tv_sec+i, curTime.tv_nsec);
		fprintf( fp , "%s,KEY=%d J4=%-6.2f  %10ld%09ld \n", measure, i,J[3], curTime.tv_sec+i, curTime.tv_nsec);
		fprintf( fp , "%s,KEY=%d J5=%-6.2f  %10ld%09ld \n", measure, i,J[4], curTime.tv_sec+i, curTime.tv_nsec);
		fprintf( fp , "%s,KEY=%d J6=%-6.2f  %10ld%09ld \n", measure, i,J[5], curTime.tv_sec+i, curTime.tv_nsec);
/*		fprintf( fp , "%s,KEY=%d J1=%6.2f ,J2=%6.2f ,J3=%6.2f ,J4=%6.2f ,J5=%6.2f ,J6=%6.2f ", measure, J[0], J[1], J[2], J[3], J[4], J[5]);
 		fprintf( fp , " %10ld%09ld\n", curTime.tv_sec+i, curTime.tv_nsec);*/
	}
	fclose( fp );
	return 0;
}
