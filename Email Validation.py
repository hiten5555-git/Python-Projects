email=input("Enter email: ")
if len(email)>=7:
        if email[0].isalpha():
            if ("@" in email) and (email.count('@')==1):
                if (email[-3]==".") ^ (email[-4]=="."):
                    if " " in email:
                        print("Inavalid email")
                    else:
                         for i in email:
                              if i.isalpha():
                                  if i==i.upper():
                                      print("Invalid email")
                                  else:
                                      continue
                              elif i.isdigit():
                                    continue
                              elif (i=="_") or (i==".") or (i=="@"):
                                    continue
                              else:
                                 print("Invalid email")
                         print("This is valid email")
                else:
                    print("Invalid email")
            else:
                print("Invalid email")
        else:
            print("First charachter is only lower alphabet")
else:
    print("Invalid email")
               
                        
                
                    
                                
        
                            
                                      
                                    
                             
                            
                       

    
            

            
