#include<stdio.h>
#include<string.h>

#define debug true //Toggle to See Variable Data And Pointer Locations

using namespace std;

int main(int argc, char* argv[]){      // Get arguments from command line
  
  if(argc==1){
    fprintf(stderr,"Usage <Password-as-Argument> \n");return -1;
  }
  int i=0;char check = 'n';             
  char a[20];
  char stack_cookie = 'S';             // The Stack cookie Variable -> 8 bits , 1 character , too small , but works for an example
  char b[20];                          
  for(i=0;i<20;i++){
  a[i]='A';b[i]='A';
  }

  strcpy(a,"somestupidpassword!");      //Put password in one array for comparing - a
  strcpy(b,argv[1]);                    //copy input password to another string   - b
  if(debug==true){                      //print all The data of string a with pointer locations
  printf("   A Data               :               B Data  \n");
  for(i=0;i<20;i++){
    printf("   %c at %p  - ",a[i],&a[i]);
    printf(" %c at %p  \n",b[i],&b[i]);
    }

  printf("\n  Validation Pointer Value : %c , Location : %p \n",check,&check);
  //Print validation pointer location and data !
  printf("\n\n   A = %s \n   B = %s  \n\n    STRCMP OUTPUT : %d \n",a,b,strcmp(a,b));
  //Display Strings and display their comparison output !
}

  if(strcmp(a,b)==0)check='y'; //bool-check
  if(debug == true)printf("\n  Validation Pointer Value : %c , Location : %p \n",check,&check);

  //CHECKMATE

  if(check=='n')printf("\n   - Wrong Password ! Access Denied !  ");
  else if (check == 'y' && stack_cookie == 'S')printf("\n   - Access Granted ! Welcome ! "); // Also Check for stack cookie integrity
  else printf("\n   - Stop Messing With the STACK!! ");
  printf("\n");

  return 0;
}
