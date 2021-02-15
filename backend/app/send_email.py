import ezgmail
from settings import RECIPIENTS

def send_email(body):
    ezgmail.send(RECIPIENTS, 'Snow in the Forecast!', body, mimeSubtype='html')
