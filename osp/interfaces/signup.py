import os
from osp.classes import Manager, Buyer, Seller, Address
import datetime, secrets, string, random, smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

senderAddress = os.environ["OSP_MAIL"]
senderPass = os.environ["OSP_PASSWORD"]

def SendMail(text, subject, receiverAddress):
    """
    Utility function to send mail
    """
    try:
        message = MIMEMultipart()
        message['From'] = senderAddress
        message['To'] = receiverAddress
        message['Subject'] = subject
        mail_content = text
        session = smtplib.SMTP('smtp.gmail.com', 587)
        session.starttls()
        session.login(senderAddress, senderPass)
        message.attach(MIMEText(mail_content, 'plain'))
        session.sendmail(senderAddress, receiverAddress, message.as_string())
        session.quit()
    except:
        raise

def GeneratePassword():
    """
    Utility function to generate random passwords
    """
    passlen = random.randint(6,10)
    passchars = string.ascii_letters+string.digits+'@_!$'
    return ''.join(secrets.choice(passchars) for _ in range(passlen))

def ManagerSignUp(data):
    """
    Create a new manager based on the data provided\n
    A dictionary with the following structure is expected as input\n
    {
        'name': string,
        'email': valid email string,
        'number': 10 digit string,
        'houseNumber': string,
        'street': string,
        'locality': string,
        'city': string,
        'state': string,
        'pincode': 6 digit string,
        'gender': string,
        'dob': string in yyyy-mm-dd format
    }\n
    It then assigns an id and password to the user and sends it on the email provided\n
    It returns a tuple (status, msg) with status=True if signup was successful and False otherwise,
    msg contains any exceptions during the signup process
    """
    user = Manager()
    try:
        # if Manager.objects(email=data['email']).count():
        #     raise Exception("Manager with given email ID already exists.")
        
        user.password = GeneratePassword()
        user.name = data['name']
        user.email = data['email']
        user.number = data['number']
        user.address = Address(houseNumber=data['houseNumber'], street=data['street'], locality=data['locality'], city=data['city'], state=data['state'], pincode=data['pincode']).save()
        user.gender = data['gender']
        user.dateOfBirth = datetime.datetime.strptime(data['dob'], "%Y-%m-%d")
        user.save()
        user.uniqueid = str(user.id)
        user.save()
        
        text = f'''Hello {user.name},

        Here are your login credentials for the portal:
            User ID: {user.uniqueid}
            Password: {user.password}

        Thank you.
        Regards,
        Team OSP
        '''
        subject = 'Welcome to Online Sales Portal'
        SendMail(text, subject, user.email)
        return (True, "Signup successful. Check your inbox for login credentials.")

    except Exception as e:
        if user.address:
            user.address.delete()
        return (False, str(e))


def CustomerSignUp(data, isBuyer=True):
    """
    Create a new customer (buyer/seller) based on the data provided\n
    If isBuyer is set to true a buyer is created otherwise a seller
    A dictionary with the following structure is expected as input\n
    {
        'name': string,
        'email': valid email string,
        'number': 10 digit string,
        'city': string
    }\n
    It then assigns an id and password to the user and sends it on the email provided\n
    It returns a tuple (status, msg) with status=True if signup was successful and False otherwise,
    msg contains any exceptions during the signup process
    """
    if isBuyer:
        user = Buyer()
    else:
        user = Seller()
    try:
        if isBuyer:
            if Buyer.objects(email=data['email']).count():
                raise Exception("Buyer with given email ID already exists.")
        else:
            if Seller.objects(email=data['email']).count():
                raise Exception("Seller with given email ID already exists.")

        user.password = GeneratePassword()
        user.name = data['name']
        user.email = data['email']
        user.number = data['number']
        user.city = data['city']
        user.save()
        user.uniqueid = str(user.id)
        user.save()
        
        session = smtplib.SMTP('smtp.gmail.com', 587)
        session.starttls()
        session.login(senderAddress, senderPass)
        text = GenerateMail(user.name, user.uniqueid, user.password, user.email)
        session.sendmail(senderAddress, user.email, text)
        session.quit()
        return (True, "Signup successful. Check your inbox for login credentials.")

    except Exception as e:
        return (False, str(e))
