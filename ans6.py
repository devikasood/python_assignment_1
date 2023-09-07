def extract_usernames_and_domains(emails):
    usernames = []
    domains = []
    
    for email in emails:
        parts = email.split("@")
        
        if len(parts) == 2:
            username, domain = parts
            usernames.append(username)
            domains.append(domain)
    
    return usernames, domains

def main():
    n = int(input("Enter the number of students: "))
    
    email_tuple = tuple(input(f"Enter email ID for student {i + 1}: ") for i in range(n))
    
    usernames, domains = extract_usernames_and_domains(email_tuple)
    
    print("Email IDs tuple:", email_tuple)
    print("Usernames tuple:", tuple(usernames))
    print("Domains tuple:", tuple(domains))

if __name__ == "__main__":
    main()
