#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

/* Linux / WSL lab. One child only; no shared writable application memory. */
int main(void) {
    int value = 10;
    fflush(stdout);
    pid_t child = fork();
    if (child < 0) {
        perror("fork");
        return EXIT_FAILURE;
    }
    if (child == 0) {
        value = 20;
        printf("child pid=%ld parent=%ld value=%d\n",
               (long)getpid(), (long)getppid(), value);
        return EXIT_SUCCESS;
    }
    int status;
    if (waitpid(child, &status, 0) < 0) {
        perror("waitpid");
        return EXIT_FAILURE;
    }
    printf("parent pid=%ld child=%ld value=%d\n",
           (long)getpid(), (long)child, value);
    return WIFEXITED(status) ? WEXITSTATUS(status) : EXIT_FAILURE;
}
