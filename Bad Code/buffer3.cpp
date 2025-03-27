#include <iostream>
#include <cstring>
#include <chrono>
#include <thread>
using namespace std;

// TERMINAL TEXT COLORS
const std::string GREEN = "\033[32m";
const string RED = "\033[31m";
const string YELLOW = "\033[33m";
const string RESET = "\033[0m"; // Reset to default color

void displayBanner();
void displayWelcome();

void printWithDelay(const std::string &message,
                    std::chrono::milliseconds delay, const std::string &color = RESET)
{
   std::cout << color << message << RESET << std::flush << "\n";
   std::this_thread::sleep_for(delay);
}

void correctPassword()
{
   displayWelcome();
   system("/bin/sh");
}

bool login()
{
   cout << "\n\n\n";
   printWithDelay("O.S.S. COMMAND SHELL INITIATED...", std::chrono::milliseconds(200), RED);
   printWithDelay(">>> ROOT ACCESS IMMINENT <<<", std::chrono::milliseconds(200), RED);
   printWithDelay(">>> Enter Password to Elevate to ROOT SHELL:", std::chrono::milliseconds(200), RED);
   printWithDelay(">>> WARNING: FULL SYSTEM CONTROL WILL BE GRANTED.", std::chrono::milliseconds(200), RED);
   cout << YELLOW << ">>> PASSWORD: " << RESET;
   char password[20]; // Vulnerable to stack-based buffer overflow attack
   cin >> password;
   // If exploited correctly, the stack pointer can be overwritten to return to the address of the correctPassword function.
   return strcmp(password, "superSecretPassword") == 0;
}

int main()
{
   displayBanner();
   if (login())
      correctPassword();
   else
   {
      cout << "Error: Unauthorized Access Attempt\n";
      cout << "Your access credentials are incorrect.\n";
      cout << "Ensure your input is meticulously crafted—sometimes even the smallest buffer can spell disaster.\n";
      cout << "Please verify your details and try again.\n";
   }
}

void displayWelcome()
{
   cout << "\n\n";
   printWithDelay("> Access Level: ROOT", std::chrono::milliseconds(500), GREEN);
   printWithDelay("> System Ready", std::chrono::milliseconds(500), GREEN);
   printWithDelay("Kernel Access: GRANTED...", std::chrono::milliseconds(500), GREEN);
   printWithDelay("Command Override: ENGAGED...", std::chrono::milliseconds(500), GREEN);
   printWithDelay("Root Directives: AVAILABLE...", std::chrono::milliseconds(500), GREEN);
   printWithDelay("Initializing OSS Red Team Protocol...", std::chrono::milliseconds(800), GREEN);
   printWithDelay("Protocol Status: FULL OPERATIONAL", std::chrono::milliseconds(600), GREEN);
   printWithDelay("Security Measures: ENFORCED", std::chrono::milliseconds(700), RED);
   printWithDelay("User Authentication: VERIFIED", std::chrono::milliseconds(500), GREEN);
   printWithDelay("System Integrity: SECURED", std::chrono::milliseconds(600), GREEN);
   printWithDelay("Network Configurations: OPTIMIZED", std::chrono::milliseconds(700), GREEN);
   printWithDelay("Launching OSS Offensive Tools...", std::chrono::milliseconds(800), GREEN);
   printWithDelay("Offensive Tools: ACTIVATED", std::chrono::milliseconds(500), GREEN);
   printWithDelay("Executing Red Team Operations...", std::chrono::milliseconds(700), RED);
   printWithDelay("Operation Status: SUCCESSFUL", std::chrono::milliseconds(600), GREEN);
   printWithDelay("Access Control: ENHANCED", std::chrono::milliseconds(700), GREEN);
   printWithDelay("Finalizing Red Team Integration...", std::chrono::milliseconds(800), GREEN);
   printWithDelay("OSS Integration: COMPLETE\n", std::chrono::milliseconds(500), RED);
   printWithDelay("Welcome to OSS Red Team Operations, CSUF!", std::chrono::milliseconds(1000), GREEN);
}

void displayBanner()
{
   cout << GREEN << " _______     _______     _______       _______  _______  _       \n";
   cout << "(  ___  )   (  ____ \\   (  ____ \\     (  ____ \\(  ___  )( (    /|\n";
   cout << "| (   ) |   | (    \\/   | (    \\/     | (    \\/| (   ) ||  \\  ( |\n";
   cout << "| |   | |   | (_____    | (_____      | |      | |   | ||   \\ | |\n";
   cout << "| |   | |   (_____  )   (_____  )     | |      | |   | || (\\ \\) |\n";
   cout << "| |   | |         ) |         ) |     | |      | |   | || | \\   |\n";
   cout << "| (___) | _ /\\____) | _ /\\____) | _   | (____/\\| (___) || )  \\  |\n";
   cout << "(_______)(_)\\_______)(_)\\_______)(_)  (_______/(_______)|/    )_)\n";
   const string SPACING(20, ' ');
   cout << SPACING << "                                                                 \n";
   cout << SPACING << "⠀⠀⠀⠀⠀⠀⣠⣴⣾⣿⣿⣿⣿⣿⣿⣶⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀\n";
   cout << SPACING << "⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣄⠀⠀⠀⠀⠀\n";
   cout << SPACING << "⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣆⠉⠉⢉⣿⣿⣿⣷⣦⣄⡀⠀\n";
   cout << SPACING << "⠀⠚⢛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄\n";
   cout << SPACING << "⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⠿⠿⣿⡇\n";
   cout << SPACING << "⢀⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠁⠀⠀⠀⠀⠀⠀⠈⠃\n";
   cout << SPACING << "⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n";
   cout << SPACING << "⠀⠀⠀⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n";
   cout << SPACING << "⠀⠀⠀⠹⣿⣿⡇⠈⠻⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n";
   cout << SPACING << "⠀⠀⠀⠀⠈⠻⡇⠀⠀⠈⠙⠿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
        << RESET;
}
