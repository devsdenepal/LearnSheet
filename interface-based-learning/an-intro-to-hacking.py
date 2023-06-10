import os
import pywhatkit
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
def display_title():
    clear_screen()
    print("\033[1;34m=== Introduction to Hacking ===\033[0m")
    print("The Hacking Manual welcomes you!")
    print("By this tool,you will cover the basics of ethical hacking and cybersecurity.")
    print("Let's get started!\nAuthor: Dev. Gautam Kumar@TechnologyMedia")
def display_menu():
    print("\033[1mMenu:\033[0m")
    print("1. \033[1;32mIntroduction to Ethical Hacking\033[0m")
    print("2. \033[1;33mSetting up Your Hacking Environment\033[0m")
    print("3. \033[1;36mReconnaissance and Information Gathering\033[0m")
    print("4. \033[1;35mExploitation Techniques\033[0m")
    print("5. \033[1;31mPost-Exploitation and Maintaining Access\033[0m")
    print("6. \033[1;33mSocial Engineering\033[0m")
    print("7. \033[1;36mWeb Application Security\033[0m")
    print("8. \033[1;32mCapture the Flag (CTF) Challenges\033[0m")
    print("9. \033[1;35mAdditional Resources\033[0m")
    print("0. \033[1;31mExit\033[0m")
def select_option():
    choice = input("\nEnter the option number to continue: ")
    return choice
def process_option(choice):
    if choice == '1':
        display_topic("Introduction to Ethical Hacking",
                      "Ethical hacking is the practice of identifying vulnerabilities and securing computer systems and networks. This guide provides an overview of ethical hacking and its importance in cybersecurity.")
    elif choice == '2':
        display_topic("Setting up Your Hacking Environment",
                      "Setting up a hacking environment is crucial for ethical hackers. This guide helps you set up your hacking environment with the necessary tools and software.")
    elif choice == '3':
        display_topic("Reconnaissance and Information Gathering",
                      "Reconnaissance involves gathering information about a target to assess its vulnerabilities. This guide covers techniques for reconnaissance and information gathering in ethical hacking.")
    elif choice == '4':
        display_topic("Exploitation Techniques",
                      "Exploitation techniques are used to gain unauthorized access to computer systems or networks. This guide explores various exploitation techniques, including network and application-level attacks.")
    elif choice == '5':
        display_topic("Post-Exploitation and Maintaining Access",
                      "Post-exploitation involves activities performed after gaining access to a target system. This guide focuses on post-exploitation and maintaining access in ethical hacking scenarios.")
    elif choice == '6':
        display_topic("Social Engineering",
                      "Social engineering is the art of manipulating individuals to gain unauthorized access to information or systems. This guide delves into social engineering techniques and their use in ethical hacking.")
    elif choice == '7':
        display_topic("Web Application Security",
                      "Web applications often have vulnerabilities that can be exploited by attackers. This guide covers web application security and common vulnerabilities, such as SQL injection and cross-site scripting (XSS).")
    elif choice == '8':
        display_topic("Capture the Flag (CTF) Challenges",
                      "Capture the Flag (CTF) challenges are cybersecurity competitions that test participants' hacking skills. This guide introduces CTF challenges and provides resources to practice your hacking abilities.")
    elif choice == '9':
        display_topic("Additional Resources for getting started with hacking","Additional resources related to hacking!")
    elif choice == '0':
        clear_screen()
        print("Thank you for exploring the world of ethical hacking!")
        print("Stay curious, keep learning, and always hack ethically.")
        print("Goodbye!")
    else:
        print("\033[91mInvalid option. Please try again.\033[0m")
def display_topic(title, summary):
    clear_screen()
    print(f"\033[1;34m=== {title} ===\033[0m")
    print(summary)
    pywhatkit.playonyt(title)
def run_workshop():
    display_title()
    while True:
        display_menu()
        option = select_option()
        if option == '0':
            break
        process_option(option)
        input("\nPress Enter to continue...")
        display_title()
run_workshop()
