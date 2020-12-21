//gcc -o FindBitPos FindBitPos.c

#include <stdio.h>

int ConvertToBit(char Input)
{
    char Output[32];
    int BitPos = 0;
    
    for (int Index = 7; Index >= 0; Index--)
    {
        BitPos++;

        //Convert character to binary
        if (Input & (1 << Index)) {
            Output[Index] = '1';
        }
        else {
            Output[Index] = '0';
        }

        //Leave when first set bit has been found
        if (Output[Index] == '1') {
            break;
        }
    }

    return BitPos;
}


void main(int argc, char *argv[])
{
    int i = 0;
    FILE *FilePointer;
    char Content;
    int BitFound = 0;

    FilePointer = fopen(argv[1], "rb");

    while ((Content = fgetc(FilePointer)) != EOF)
    {
        i++;

        if (Content != NULL)
        {
            BitFound = ConvertToBit(Content);

            printf("%d", BitFound);
            printf(":");
            printf("%d", i);

            break;
        }
    }
    fclose(FilePointer);
}
