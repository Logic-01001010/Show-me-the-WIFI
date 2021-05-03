from flask import Flask, render_template, request, send_from_directory




app = Flask(__name__)


@app.route('/')
def main():

   try:

      f = open('uploads\\cmdtemp')

      content = []


      while True:
         line = f.readline()
         line = line.replace("\n",' ')

         if not line: break
         content.append(line)

      f.close()


      return render_template('index.html', content=content)

   except:

      return "None"

@app.route('/upload', methods = ['GET', 'POST'])
def upload():
   if request.method == 'POST':

      
      
      try:
         file = request.files["file"]


         print('Saving: '+file.filename)
         
         file.save("uploads/"+file.filename)

         
         return "<script>location.href = \"/\";</script>"
      except:

         print('except')

         return "<script>location.href = \"/\";</script>"




      
if __name__ == '__main__':
   #서버 실행
   #app.run(debug = True)
   app.run(host='0.0.0.0',port='80', threaded=True, debug=True)
