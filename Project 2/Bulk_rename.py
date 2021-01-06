## importing libraries
from flask import Flask, redirect, url_for, request, render_template, flash
import os, string, datetime

##function : to get last modified datetime of a file/folder
def modification_date(filename): 
   t = os.path.getmtime(filename)
   return datetime.datetime.fromtimestamp(t)

##function : to get the list of all available drives
def all_drive():
   available_drives = [['%s:' % d,'%s:' % d] for d in string.ascii_uppercase if os.path.exists('%s:' % d)]
   for count,drive in enumerate(available_drives):
      if(drive[1]=="C:"):
         available_drives[count][1]=os.path.expanduser("~")
   return available_drives

##function : to find all the files/folders available at given path
def list_file(add):
   available_drives = all_drive()
   if(os.path.exists(add)):
      if(os.path.isdir(add)):
         try:
            total_files = str(len(os.listdir(add))) ## Total number of files
            if(total_files == '0'):
               flash(u'Directory is empty. You are at parent directory.','danger')
               return list_file(os.path.dirname(add))
         except WindowsError:
            flash("\n\n[WinError 5] Access is denied: "+add,'danger')
            return list_file(os.path.dirname(add))
         list = []
         for filename in os.listdir(add):
            stats = []
            if (not filename.startswith('.')) and (not filename.startswith('$')):
               stats.append(add)
               stats.append(filename)
               stats.append(modification_date(add+'/'+filename))
               if(os.path.isdir(add+'/'+filename)):      
                  stats.append('Directory')
                  stats.append('-')
               else:
                  stats.append('File')
                  ststinfo = os.stat(add+'/'+filename)
                  stats.append(str(int(ststinfo.st_size/1024)).zfill(7)+'KB')
               list.append(stats)
         return render_template("list_file.html", list=list,  drives=available_drives)
      else:
         flash(u'Given path is not a directory. You are at parent directory.','danger')
         return list_file(os.path.dirname(add))
   else:
      flash(u'Path not found.','danger')
      return redirect('/')

         
app = Flask(__name__)
app.secret_key = b'Govind Banura'

##default route / index route
@app.route("/")
@app.route("/index")
def index():
   drive = all_drive()
   return render_template("index.html", drives=drive)

## route to show all available files/folders at given path from hyperlink
@app.route('/path/<add>')
def path(add):
   return list_file(add)
      
## route to show all available files/folders at given path from input tag
@app.route('/path', methods=['POST'])
def input_path():
   add=request.form['add']
   return list_file(add)
   
## route to rename all selected files/folders to given naming convention
@app.route('/rename',methods = ['POST'])
def rename():
   files = request.form.getlist('rename[]')
   nam_con = request.form['naming_convention']
   total_files = str(len(files))
   for count, file in enumerate(files):
      src = file
      path = os.path.split(file)[0]
      filename = os.path.split(file)[1]
      extension = os.path.splitext(filename)[1] ## extention of the source file
      dst = path +'/'+ nam_con + str(count+1).zfill(len(total_files)) ##naming convention
      try: ## renaming file
         os.rename(src, dst + extension) 
      except: ## if filename already exists, Create temporary filename
         temp_count = 2
         while True:
            temp_name = dst+" ("+str(temp_count)+")"+extension
            try:
               os.rename(src, temp_name)
               break
            except:
               temp_count+=1      
   flash(u'Rename Successfully','success')
   return list_file(path)

if __name__ == '__main__':
   app.run(debug = False)
