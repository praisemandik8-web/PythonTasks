print("Welcome to Nokia, chief")

print("1 for Phone book") 
print("2 for Messages")
print("3 for chat") 
print("4 for Call register")
print("5 for Tones") 
print("6 for Settings")
print("7 for Call divert") 
print("8 for Games")
print("9 for Calculator") 
print("10 for Reminders")
print("11 for Clock") 
print("12 for Profiles")
print("13 for SIM services") 
print("14 back to main menu")  

menu_maps = int(input("Enter a number to select menu "))

match (menu_maps):
        case 1: 
            print("1. search")
            print("2. Service Nos.")
            print("3. Add name")
            print("4. Erase")
            print("5. Edit")
            print("6. Assign tone")
            print("7. Send business card")
            print("8. options")
            print("9. Speed dials")
            print("10. Voice tags")
                
            phoneBook = int(input("Enter Number "))
            if phoneBook == 8: 
                    print("1. Type of view")
                    print("2. Memory status")                   

        case 2: 
            print("1. Write messages")
            print("2. Inbox")
            print("3. Outbox")
            print("4. Pictures messages")
            print("5. Templates")
            print("6. Smileys")
            print("7. Message settings")
            print("8. Info service")
            print("9. Voice mailbox number")
            print("10. Service command editor")
                
            message_settings = int(input("Enter Number "))
            if message_settings == 7: 
                    print("1. Set")
                    print("2. Common") 
            sett = int(input("Enter Number "))       
            if sett == 1: 
                    print("1. Message centre number")
                    print("2. Mesage sent as")
                    print("2. Mesage validity")
            else: 
                    print("1. Delivery reports")
                    print("2. Reply via same centre")
                    print("2. Character support")  

        case 3: 
            print("Chat")
    
        case 4: 
            print("1. Missed calls")
            print("2. Received calls")
            print("3. Dialed numbers")
            print("4. Erase recent call lists")
            print("5. Show call duration")
            print("6. Show call costs")
            print("7. call cost settings")
            print("8. Prepaid credit")
            
            call_register = int(input("Enter Number"))
            if call_register == 5: 
                    print("1. Last call duration")
                    print("2. All calls duration")
                    print("3. Received calls duration")
                    print("4. Dialed calls duration")
                    print("5. Clear timers")

            if call_register == 6: 
                    print("1. Last call cost")
                    print("2. All calls cost")
                    print("3. Clear counters")

            if call_register == 7: 
                    print("1. call cost")
                    print("2. Show costs in")

            case 5: 
                print("1. Ringing tone")
                print("2. Ringing volume")
                print("3. Incoming call alert")
                print("4. Composer")
                print("5. Message alert tone")
                print("6. Keypad tones")
                print("7. Warning and game tones")
                print("8. Vibrating alert")
                print("9. Screen saver")
                      
            case 6: 
                print("1. Call settings")
                print("2. Phone settings")
                print("3. Security settings")
                print("4. Restore factory settings")

            settings = int(input("Enter Number"))
            if settings == 1: 
                    print("1. Automatic redial")
                    print("2. Speed dialing")
                    print("3. Call waiting options")
                    print("4. Own number sending")
                    print("5. Phone line in use")
                    print("6. Automatic answer")
            
             if settings == 2: 
                    print("1. Language")
                    print("2. Cell info display")
                    print("3. Welcome note")
                    print("4. Network selection")
                    print("5. Lights")
                    print("6. Confirm SIM service actions")

               if settings == 3: 
                    print("1. PIN code request")
                    print("2. Cell barring service")
                    print("3. Fixed dialing")
                    print("4. Closed user group")
                    print("5. Phone Security")
                    print("6. Confirm SIM service actions")

                 case 7:
                    print("Call divert")

                case 8:
                    print("Games")

                case 9:
                    print("Calculator")

                case 10:
                    print("Reminders")

                case 11: 
                    print("1. Alarm clock")
                    print("2. Clock settings")
                    print("3. Date setting")
                    print("4. Stopwatch")
                    print("5. Countdown timer")
                    print("6. Auto update of date and time")

                case 12:
                    print("Profiles")

                case 13:
                    print("Sim services")

       
                
