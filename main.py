from modeltrain import face_detector, modeltrainer
import threading
import modeltrain
import cv2
# Get the training data we previously made
def mail(img) :
    from termcolor import colored
    from colorama import init 
    import smtplib
    import imghdr
    from email.message import EmailMessage
    import cv2
    init(autoreset=True)
    print(colored(text ="\t\t\t\n======================= Some Other User Detected ==================================\n", color='cyan', on_color='on_grey',attrs= ['blink']))
    print(colored(text ="\t\t\t\n======================= Sending Mail ==================================\n", color='cyan', on_color='on_grey',attrs= ['blink']))    
    print("Capturing.....")
    cv2.imwrite('./intruder.jpg',img)
    #type here your email address
    sender_email = "XXXXXX@gmail.com"
    password = "XXXXXX" #your password of generate this application password from your gmail account
        
    #type here recievers email address.
    reciever_email="XXXXXX@gmail.com"
    

    securityMessage = EmailMessage()                         
    securityMessage['Subject'] = "SECURITY ALERT" 
    securityMessage['From'] = sender_email                   
    securityMessage['To'] = reciever_email                   
    securityMessage.set_content('Possible Intrusion : This Person is trying to access your system...Have a look!') 

    with open('./intruder.jpg', 'rb') as f:
        image_data = f.read()
        image_type = imghdr.what(f.name)
        image_name = f.name
    
    securityMessage.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

        smtp.login(sender_email,password)              
        smtp.send_message(securityMessage) 
    print("Mail Sent Successfully")
    print(colored(text ="\t\t\t\n======================= Sending Whatsapp Message  ==================================\n", color='cyan', on_color='on_grey',attrs= ['blink']))
    print("Hold on.....this may take a while")

    from twilio.rest import Client

# client credentials are read from TWILIO_ACCOUNT_SID and AUTH_TOKEN
    client = Client()

    # this is the Twilio sandbox testing number
    from_whatsapp_number='whatsapp:+1XXXXXX'
    # replace this number with your own WhatsApp Messaging number
    to_whatsapp_number='whatsapp:+91XXXXXX'

    client.messages.create(body='Security Alert : Someone tried using the system...check your mail!',
                        from_=from_whatsapp_number,
                        to=to_whatsapp_number)
    print("\nMessage Sent Successfully..")
   # print("Message id : " + message.sid)

def weblauch():
    from termcolor import colored
    from colorama import init 
    import os
    init(autoreset=True)
    
    print(colored(text ="\t\t\t\n======================= Juzer Detected Launching Webserver ==================================\n", color='cyan', on_color='on_grey',attrs= ['blink']))
    os.system("terraform init")
    os.system("terraform apply --auto-approve")

juzer_model = modeltrain.modeltrainer()
user2_model=  modeltrain.user2modeltrainer()
# Open Webcam
cap = cv2.VideoCapture(0)
count = 0
count2 = 0


while True:

    ret, frame = cap.read()
    
    image, face = face_detector(frame)
    
    try:
            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

            # Pass face to prediction model
            # "results" comprises of a tuple containing the label and the confidence value
            results = juzer_model.predict(face)
            results2 = user2_model.predict(face)
            # harry_model.predict(face)

            if results[1] < 50:
                confidence = int( 100 * (1 - (results[1])/400) )
                display_string = str(confidence) + '% Confident it is User'
            
            elif results2[1] < 50:
                confidence2 = int( 100 * (1 - (results[1])/400) )
                display_string = str(confidence) + '% Confident it is User'
            #print(confidence2)
            if confidence > 80 and count <=20 and results[1] < 50 :

                count  = count + 1
            
                cv2.putText(image, "Hey Juzer", (250, 100), cv2.FONT_HERSHEY_COMPLEX, 1, 	(120,21,207), 2)
                cv2.putText(image, "Launching the infrastructure", (50, 420), cv2.FONT_HERSHEY_COMPLEX, 1, (29,210,232), 2)
                cv2.putText(image, "on AWS using Terraform", (140, 470), cv2.FONT_HERSHEY_COMPLEX, 1, (29,210,232), 2)
                cv2.imshow('Main', image )
                if count == 15 :
                    t = threading.Thread(target=weblauch)
                    #t = threading.Thread(target=weblauch)
                    t.start()

            elif confidence > 80 and results[1] < 50 :

                #print(confidence)
                cv2.putText(image, "Hey Juzer", (250, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (29,210,232), 2)
                
                #cv2.putText(image, "I dont know, how r u", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2)
                #image[50:297,100:347] = digit_lst["3"]
                cv2.imshow('Main', image )
                #cv2.imshow('Face Recognition', image )
            elif confidence2 > 77 and count2 <=20 :

                count2  = count2 + 1
                if count2 == 15 :
                    t2 = threading.Thread(target=mail,args=[image])
                    #t = threading.Thread(target=weblauch)
                    t2.start()
                cv2.putText(image, "Hey Qasim", (250, 100), cv2.FONT_HERSHEY_COMPLEX, 1, 	(120,21,207), 2)
                cv2.putText(image, "Sending Alert Now", (230, 420), cv2.FONT_HERSHEY_COMPLEX, 1, (29,210,232), 2)
                #cv2.putText(image, "on AWS using Terraform", (140, 470), cv2.FONT_HERSHEY_COMPLEX, 1, (29,210,232), 3)
                cv2.imshow('Main', image )



            elif confidence2 > 77 :

                #print(confidence)
                cv2.putText(image, "Hey Qasim", (250, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (29,210,232), 2)
                
                #cv2.putText(image, "I dont know, how r u", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2)
                #image[50:297,100:347] = digit_lst["3"]
                cv2.imshow('Main', image )
                #cv2.imshow('Face Recognition', image )


            else: 
                #cv2.putText(image, "Not Recognized", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2)
                cv2.imshow('Main', image )
              
            
    except Exception as e:
            cv2.imshow('Main', image )
            pass
    
    
     
    if cv2.waitKey(10) == 13: #13 is the Enter Key
        break
    
stop_threads = True
cap.release()
cv2.destroyAllWindows()     #(209, 80, 0, 255