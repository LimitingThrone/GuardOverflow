#include <string>
#include <iostream>

using namespace std; 

int main()
{
  begin:
  int authentication = 0;
  char cUsername[10], cPassword[10];
  char cUser[10], cPass[10];

  cout << "Username: ";
  cin >> cUser;

  cout << "Pass: ";
  cin >> cPass;

  strcpy(cUsername, cUser);
  strcpy(cPassword, cPass);

  if(strcmp(cUsername, "admin") == 0 && strcmp(cPassword, "adminpass") == 0)
  {
    authentication = 1;
  }
  if(authentication)
  {
    cout << "Access granted\n";
    cout << (char)authentication;
  } 
  else 
  {
    cout << "Wrong username and password\n";
  }

  system("pause");
  goto begin;
}
