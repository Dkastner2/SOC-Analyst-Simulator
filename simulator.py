import random
# Version 1.4
# SOC SHIFT: Threat Hunter
# Created by Dominic Kastner

cases = [
    {
        "name": "Midnight Login Storm",
        "host": "WS-FINANCE-07",
        "severity": "HIGH",
        "evidence": [
            "47 failed login attempts in 3 minutes.",
            "Source IP: 203.0.113.42 (external test address).",
            "Successful login followed the failed attempts.",
            "An unusual PowerShell process started after login."
        ],
        "answer": "TP",
        "explanation": (
            "The failed logins, successful authentication, and "
            "unusual process activity together warrant escalation. "
            "The evidence is consistent with a possible compromise."
        )
    },
    {
        "name": "The Administrator's Mistake",
        "host": "WS-IT-02",
        "severity": "MEDIUM",
        "evidence": [
            "12 failed authentication attempts detected.",
            "Source IP: 192.168.1.25 (internal address).",
            "Successful login occurred after the failures.",
            "IT change records confirm an approved password reset."
        ],
        "answer": "FP",
        "explanation": (
            "The activity matches an authorized password reset. "
            "The alert is benign in this simulated scenario."
        )
    },
    {
        "name": "The Suspicious Scheduled Task",
        "host": "WS-HR-04",
        "severity": "HIGH",
        "evidence": [
            "A new scheduled task appeared outside business hours.",
            "The task launches PowerShell with an encoded command.",
            "The task runs under an unexpected privileged account.",
            "No approved maintenance activity was recorded."
        ],
        "answer": "TP",
        "explanation": (
            "Unexpected scheduled-task persistence combined with "
            "encoded PowerShell execution warrants investigation "
            "and escalation."
        )
    },
    {
        "name": "The Security Scanner",
        "host": "SRV-WEB-01",
        "severity": "MEDIUM",
        "evidence": [
            "Hundreds of connection attempts targeted multiple ports.",
            "Source IP: 192.168.1.50 (internal address).",
            "The source belongs to the security assessment subnet.",
            "The activity matches an approved vulnerability scan."
        ],
        "answer": "FP",
        "explanation": (
            "The traffic matches an authorized security scan. "
            "It is a benign true detection, treated as a false "
            "positive for this simplified alert game."
        )
    }
]

score = 0
correct = 0
streak = 0

random.shuffle(cases)

print("=" * 55)
print("             SOC SHIFT: THREAT HUNTER")
print("=" * 55)
print("Welcome, Analyst.")
print("Your night shift has started.")
print("Investigate the alerts and protect the network!")

for number, case in enumerate(cases, start=1):

    print("\n" + "=" * 55)
    print(f"CASE {number}: {case['name']}")
    print("=" * 55)

    print("Host:", case["host"])
    print("Severity:", case["severity"])

    reviewed = set()

    while True:

        print("\nANALYST ACTIONS")
        print("[1] Review Authentication / Event Logs")
        print("[2] Investigate Source or Origin")
        print("[3] Check Related Activity")
        print("[4] Review Supporting Evidence")
        print("[5] Make Final Decision")
        print("[6] View Score")

        choice = input("\nSelect an action: ").strip()

        if choice in ["1", "2", "3", "4"]:

            index = int(choice) - 1

            print("\nEVIDENCE DISCOVERED:")
            print(case["evidence"][index])

            if index not in reviewed:
                reviewed.add(index)
                score += 5
                print("+5 Investigation Points!")
            else:
                print("Evidence already reviewed.")

        elif choice == "6":

            print("\nCURRENT SCORE:", score)
            print("CORRECT DECISIONS:", correct)
            print("CURRENT STREAK:", streak)

        elif choice == "5":

            print("\nFINAL CLASSIFICATION")
            print("[1] True Positive - Escalate")
            print("[2] False Positive - Close")
            print("[3] Continue Investigating")

            decision = input("Your decision: ").strip()

            if decision == "3":
                print("Returning to investigation...")
                continue

            if decision not in ["1", "2"]:
                print("Invalid decision.")
                continue

            if not reviewed:
                print("Review evidence before making a decision.")
                continue

            answer = "TP" if decision == "1" else "FP"

            if answer == case["answer"]:

                correct += 1
                streak += 1

                bonus = 50 + (streak * 10)
                score += bonus

                print("\nCORRECT DECISION!")
                print(f"+{bonus} Points!")

            else:

                streak = 0
                print("\nINCORRECT DECISION!")
                print("Your streak has been reset.")

            print("\nCASE REVIEW:")
            print(case["explanation"])

            if len(reviewed) < 4:
                print(
                    "\nTip: You reviewed only",
                    len(reviewed),
                    "of 4 evidence items."
                )

            break

        else:
            print("Invalid selection. Try again.")

print("\n" + "=" * 55)
print("                SHIFT COMPLETE")
print("=" * 55)

print("Cases Solved:", correct, "/", len(cases))
print("Final Score:", score)

if correct == 4:
    rank = "ELITE THREAT HUNTER"
elif correct == 3:
    rank = "SOC ANALYST II"
elif correct == 2:
    rank = "SOC ANALYST I"
else:
    rank = "SOC TRAINEE"

print("Your Rank:", rank)
print("\nThanks for playing SOC SHIFT!")
