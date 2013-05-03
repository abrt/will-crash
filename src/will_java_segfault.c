#include <jni.h>
#include <signal.h>
#include <stdlib.h>

JNIEXPORT void JNICALL Java_WillRaiseSigSegv_raiseSigSegv (JNIEnv *env, jclass class)
{
    puts("Raising SIGSEGV");
    raise(SIGSEGV);
}
