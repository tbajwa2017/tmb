#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()

{

char * char_ptr ;

char_ptr = (char *)calloc(65536 , sizeof(char)) ;
if ( char_ptr == NULL )
{
printf("Memory not allocated and inititalized.\n") ;
exit(100) ;
}


/*memcpy(char_ptr,"C",strlen(char_ptr)) ;
*/
printf("%d\n", strlen(char_ptr)) ;
while (1)
{
sleep(100);
}
return (0) ;

}


