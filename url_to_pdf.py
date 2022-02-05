import requests
import os

class Getpdf():
    def __init__(self, url, dir_path="pdf/"):
        self.url = str(url)
        self.folder_path = dir_path

    def generate_pdf(self, filename=None):
        file_name = filename
        try:
            data = requests.get(self.url)
            if data.status_code == 200:
                if not os.path.exists(self.folder_path):
                    os.makedirs(self.folder_path)

                if not file_name:
                    file_name  = self.url.split('/')[-1]
                
                else:
                    file_name = f'{filename}.pdf'
                
                full_path = os.path.join(self.folder_path, file_name)
                if not os.path.exists(full_path):
                    with open(f'{full_path}', 'wb') as f:
                        f.write(data.content)
                        
                    print(f"{'-'*100}\n[SUCCESS] {filename} created successfully at  {self.folder_path} DIR.")
                return full_path

        except Exception as e:
            print(f"{'-'*100}\n[ERROR] {e}")
            return

