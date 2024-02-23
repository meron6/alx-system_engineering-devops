#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int infinite_while(void)
{
    while (1)
    {
        sleep(1);
    }
    return (0);
}

int main(void)
{
    pid_t child_pid;
    int i;

    for (i = 0; i < 5; i++)
    {
        child_pid = fork();
        if (child_pid > 0)
        {
            // Parent process
            printf("Zombie process created, PID: %d\n", child_pid);
            sleep(1); // Sleep to avoid creating all zombies at once
        }
        else if (child_pid == 0)
        {
            // Child process
            exit(0);
        }
        else
        {
            // Error handling if fork fails
            perror("fork");
            return (1);
        }
    }

    // Infinite loop to keep the parent process running
    return infinite_while();
}

