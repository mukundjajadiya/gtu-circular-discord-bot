from apscheduler.schedulers.background import BackgroundScheduler
from today_circular import get_today_circular, get_time
from old_circular import get_old_circular_list
from url_to_pdf import Getpdf
from send_file_to_dc import Bot
import time
import os
import glob

bot = Bot()
sent_circulars = []
sent_pdf_names = []

def custom():
    global sent_circulars
    counter = 0
    global sent_pdf_names
    today_circulars = get_today_circular()

    try:
        for circular in today_circulars:
            # if circular not in sent_circulars :
            if not any(sent_circular['content'] == circular['content'] for sent_circular in sent_circulars):
                url = f"{circular['link']}"
                pdf = Getpdf(url= url) 
                pdf_full_path = pdf.generate_pdf(filename = circular['content'])
                time.sleep(1)
                file_name = pdf_full_path.split("/")[-1]

                sent_circulars.append(circular)
                sent_pdf_names.append(file_name)

                # bot.message_sender("Enter your message here...")
                bot.file_sender(pdf_full_path)
                time.sleep(1)
                counter += 1

            else:
                if counter == 0:
                    print(f"{get_time()}: [Note] circular already sent.")
                    counter += 1
       
        old_circulars = get_old_circular_list()
        for old_circular in old_circulars:
            if old_circular in sent_circulars:
                sent_circulars.remove(old_circular)
                print("[DELETE] Old circular deleted successfully.")

    except Exception as e:
        print(e)


def delete_pdf_file():
    global sent_pdf_names
    if len(sent_circulars) == len(sent_pdf_names) and os.path.exists(os.path.join('pdf/', sent_pdf_names[-1])):
        print(f"{get_time()}: [DELETE] Deleting PDF file..........")
        try:
            for sent_pdf_name in sent_pdf_names:
                os.remove(os.path.join('pdf/',sent_pdf_name))
            print(f"{get_time()}: [SUCCESS] All PDF file deleted successfully.")
        except Exception as e:
            print(e)

    else:
        print(f"{get_time()}: [Note] All pdf files are deleted already.")

sched = BackgroundScheduler(daemon=True)
sched.add_job(custom, 'interval', minutes=5)
sched.add_job(delete_pdf_file, 'interval', minutes=17)
sched.start()
print("App starting...")
bot.client.run(bot.TOKEN)
