#include <stdio.h> // write in python
#include <string.h>

#define q0 0
#define q1 1
#define q2 2
#define q3 3
#define q4 4
#define q_dead 5

int isSingleLineComment(const char *s)
{
    int state = q0;
    for (int i = 0; s[i]; i++)
    {
        char c = s[i];
        if (state == q0)
            state = (c == '/') ? q1 : q_dead;
        else if (state == q1)
            state = (c == '/') ? q2 : q_dead;
        else if (state == q2)
            state = q2;
        else
            return 0;
        if (state == q_dead)
            return 0;
    }
    return state == q2;
}

int isMultiLineComment(const char *s)
{
    int state = q0;
    for (int i = 0; s[i]; i++)
    {
        char c = s[i];
        if (state == q0)
            state = (c == '/') ? q1 : q_dead;
        else if (state == q1)
            state = (c == '*') ? q2 : q_dead;
        else if (state == q2)
            state = (c == '*') ? q3 : q2;
        else if (state == q3)
        {
            if (c == '/')
                return 1;
            else if (c != '*')
                state = q2;
        }
        else
            return 0;
        if (state == q_dead)
            return 0;
    }
    return 0;
}

int main()
{
    char str[1000];
    int choice;
    printf("--- Comment Checker Menu ---\n");
    do
    {
        printf("1. Check a comment\n2. Exit\nEnter choice: ");
        scanf("%d", &choice);
        getchar();

        if (choice == 1)
        {
            printf("Enter a comment line: ");
            fgets(str, sizeof(str), stdin);
            str[strcspn(str, "\n")] = 0;

            if (isSingleLineComment(str))
                printf("Valid SINGLE-LINE comment.\n");
            else if (isMultiLineComment(str))
                printf("Valid MULTI-LINE comment.\n");
            else
                printf("Not a valid C comment.\n");
        }
        else if (choice != 2)
        {
            printf("Invalid choice. Please enter 1 or 2.\n");
        }
    } while (choice != 2);

    printf("Exiting program. Goodbye!\n");
    return 0;
}
