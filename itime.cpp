#include <stdio.h>
#include <time.h>


int main(void) {
  struct timespec startTime, endTime, sleepTime;

  clock_gettime(CLOCK_REALTIME, &startTime);
  sleepTime.tv_sec = 0;
  sleepTime.tv_nsec = 123;

  // 何らかの処理を実行
  for (int ii = 0; ii < 1000; ii++) {
    // 何らかの処理
    nanosleep(&sleepTime, NULL);
  }
  clock_gettime(CLOCK_REALTIME, &endTime);

  // 処理時間を出力
  printf("開始時刻　 = %10ld.%09ld\n", startTime.tv_sec, startTime.tv_nsec);
  printf("終了時刻　 = %10ld.%09ld\n", endTime.tv_sec, endTime.tv_nsec);
	return 0;
}
