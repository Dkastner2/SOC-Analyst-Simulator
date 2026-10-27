# SOC Analyst Simulator
# Created by Dominic Kastner
# Version 1.0

print("=" * 45)
print("         SOC ANALYST SIMULATOR")
print("=" * 45)

print("\n🚨 NEW SECURITY ALERT 🚨")

# Alert information
hostname = "WIN-CLIENT01"
severity = "HIGH"
alert_type = "Suspicious Login Activity"

print("\nHost:", hostname)
print("Severity:", severity)
print("Alert:", alert_type)

print("\nWhat would you like to investigate?")

print("[1] Review failed login attempts")
print("[2] Check successful logins")
print("[3] Investigate source IP")
print("[4] Make a final decision")

choice = input("\nEnter your choice (1-4): ")

if choice == "1":
    print("\n47 failed login attempts detected.")
    print("Username: administrator")
    print("Time window: 3 minutes")

elif choice == "2":
    print("\nOne successful login detected.")
    print("Username: administrator")
    print("Login occurred after multiple failures.")

elif choice == "3":
    print("\nSource IP: 192.168.1.105")
    print("IP Classification: Private/Internal")
    print("Further investigation recommended.")

elif choice == "4":
    print("\nInvestigation incomplete.")
    print("Review available evidence before making a decision.")

else:
    print("\nInvalid selection. Please enter 1, 2, 3, or 4.")

print("\nThank you for using SOC Analyst Simulator!")
