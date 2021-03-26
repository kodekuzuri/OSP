from osp.classes import Manager, Buyer, Seller, Address
import datetime, secrets, string, random, smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# make these environment variable finally
senderAddress = 'osp.noreply@gmail.com'
senderPass = 'osp@nap3'

def GenerateMail(name, userId, password, receiverAddress):
    """
    Utility function to generate mail content
    """
    message = MIMEMultipart()
    message['From'] = senderAddress
    message['To'] = receiverAddress
    message['Subject'] = 'Welcome to Online Sales Portal'
    mail_content = f'''Hello {name},

    Here are your login credentials for the portal:
        User ID: {userId}
        Password: {password}
    
    Thank you.
    Regards,
    Team OSP
    '''
    message.attach(MIMEText(mail_content, 'plain'))
    return message.as_string()

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
        'address': {
            'houseNumber': string,
            'street': string,
            'locality': string,
            'city': string,
            'state': string,
            'pincode': 6 digit string
        },
        'gender': string,
        'dob': valid date object
    }\n
    It then assigns an id and password to the user and sends it on the email provided\n
    It returns a tuple (status, msg) with status=True if signup was successful and False otherwise,
    msg contains any exceptions during the signup process
    """
    user = Manager()
    try:
        if Manager.objects(email=data['email']).count():
            raise Exception("Manager with given email ID already exists.")
        
        user.password = GeneratePassword()
        user.name = data['name']
        user.email = data['email']
        user.number = data['number']
        addrdata = data['address']
        user.address = Address(houseNumber=addrdata['houseNumber'], street=addrdata['street'], locality=addrdata['locality'], city=addrdata['city'], state=addrdata['state'], pincode=addrdata['pincode']).save()
        user.gender = data['gender']
        user.dateOfBirth = data['dob']
        user.save()
        user.uniqueid = str(user.id)
        user.save()
        
        session = smtplib.SMTP('smtp.gmail.com', 587)
        session.starttls()
        session.login(senderAddress, senderPass)
        text = GenerateMail(user.name, user.uniqueid, user.password, user.email)
        session.sendmail(senderAddress, user.email, text)
        session.quit()
        return (True, "Signup Successful")

    except Exception as e:
        if user.address:
            user.address.delete()
        return (False, e)


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
        return (True, "Signup Successful")

    except Exception as e:
        return (False, e)
