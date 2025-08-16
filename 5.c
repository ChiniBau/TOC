#include <stdio.h> // Write in python
#include <string.h>
#include <ctype.h>

int isKeyword(char *s)
{
    char *kw[] = {"auto", "break", "case", "char", "const", "continue", "default", "do", "double",
                  "else", "enum", "extern", "float", "for", "goto", "if", "inline", "int", "long", "register",
                  "restrict", "return", "short", "signed", "sizeof", "static", "struct", "switch", "typedef",
                  "union", "unsigned", "void", "volatile", "while"};
    for (int i = 0; i < sizeof(kw) / sizeof(kw[0]); i++)
        if (strcmp(s, kw[i]) == 0)
            return 1;
    return 0;
}

int isValidId(char *s)
{
    if (!(isalpha(s[0]) || s[0] == '_'))
        return 0;
    for (int i = 1; s[i]; i++)
        if (!(isalnum(s[i]) || s[i] == '_'))
            return 0;
    return !isKeyword(s);
}

int main()
{
    char str[100];
    int ch;
    printf("Menu:\n1. Check keyword\n2. Check identifier\n3. Exit\n");
    do
    {
        printf("Enter your choice: ");
        scanf("%d", &ch);
        getchar();
        if (ch == 1)
        {
            printf("Enter string: ");
            fgets(str, sizeof(str), stdin);
            str[strcspn(str, "\n")] = 0;
            printf(isKeyword(str) ? "'%s' is a keyword.\n" : "'%s' is NOT a keyword.\n", str);
        }
        else if (ch == 2)
        {
            printf("Enter string: ");
            fgets(str, sizeof(str), stdin);
            str[strcspn(str, "\n")] = 0;
            printf(isValidId(str) ? "'%s' is a valid identifier.\n" : "'%s' is NOT a valid identifier.\n", str);
        }
        else if (ch != 3)
        {
            printf("Invalid choice!\n");
        }
    } while (ch != 3);
    return 0;
}
