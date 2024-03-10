###########Available Disk Space##################
import shutil
import psutil
import email.message
import mimetypes
import os.path
import smtplib
def check_disk_full(disk,20):
    """Returns True if there isn't enough disk space, False otherwise."""
    du = shutil.disk_usage(disk)
    # Calculate the percentage of free space
    percent_free = 100 * du.free / du.total
    if percent_free < min_percent:
        return f'Error - Available disk space is less than 20%'

def check_memory_full(disk,0.5):
    du = shutil.disk_usage(disk)
    #Calculate how many free gigabytes
    gigabytes_free = du.free / 2**30
    if gigabytes_free < min_g
    subject=b:
        return f'Error - Available memory is less than 500MB'


def check_cpu_usage(80):
    usage = psutil.cpu_percent(1)

    if usage > percent

        return f'Error - CPU usage is over 80%'

def name_resolution("localipaddress"):
    localhost = socket.gethostbyname("localipaddress")
    if localhost != "127.0.0.1":
        return f'Error - localhost cannot be resolved to 127.0.0.1'

if check_disk_full(disk,20):
    subject=check_disk_full(disk,20)
elif check_memory_full(disk,0.5):
    subject=check_memory_full(disk,0.5)
elif check_cpu_usage(80):
    subject=check_cpu_usage(80)
elif name_resolution("localipaddress"):
    subject=name_resolution("localipaddress")

def generate(sender, recipient, subject, body):
  """Creates an email with an attachement."""
  # Basic Email formatting
    message = email.message.EmailMessage()
    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = subject
    message.set_content(body)

sender = "automation@example.com"
receiver = "{}@example.com".format(os.environ.get('USER'))
body = " Please check your system and resolve the issue as soon as possible."

message =generate(sender, receiver, subject, body)
emails.send(message)
