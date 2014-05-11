# -*- coding: utf-8 -*-

import os
import urllib
import webapp2
import logging
from google.appengine.ext import db
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


coordinates_html = """

  <html>

  <form action = "coin" method = "POST" enctype="multipart/form-data">
  lat: <input type = "text" name = "latitude">
  long: <input type = "text" name = "longitude">
  score: <input type = "text" name = "score">
  <input type="submit" value="submit"></button>
  </form>

  </html>

"""




json_values = ''


class ActualHeatMapValues(db.Model):
  lat = db.StringProperty()
  lon = db.StringProperty()
  score = db.StringProperty()
  address = db.StringProperty();
  city = db.StringProperty();
  country = db.StringProperty();
  district = db.StringProperty();
  entry1 = db.StringProperty(); #ramp y/n
  entry2a = db.StringProperty();  #ramp y/n
  entry2b = db.StringProperty();  #ramp y/n
  entry2c = db.StringProperty();  #ramp y/n
  entry2d = db.StringProperty();  #ramp y/n
  entry3 = db.StringProperty();   #ramp exists y/n
  ground1 = db.StringProperty();   #ground well maintained y/n
  ground2a = db.StringProperty();  #rocky ground y/n
  ground2b = db.StringProperty();  #uneven y/n
  ground2c = db.StringProperty();  #used for other purposes y/n
  ground3 = db.StringProperty();  #playground does not exist y/n
  library1 = db.StringProperty(); # library facility is available y/n
  library2a = db.StringProperty(); # library locked y/n
  library2b = db.StringProperty(); # library books kept beyond students reach y/n
  library2c = db.StringProperty(); # no time alloted in time table y/n
  library2d = db.StringProperty(); # insufficient number of books y/n
  library3 = db.StringProperty(); # library facility is not available y/n
  name = db.StringProperty(); # name
  pin = db.StringProperty(); #pincode
  repname = db.StringProperty(); #uploader name
  repphone = db.StringProperty(); #uploader phone
  state = db.StringProperty(); #state 
  taluk = db.StringProperty(); #taluk
  toilet1 = db.StringProperty(); #toilets have working doors y/n
  toilet2a = db.StringProperty(); #toilets are dirty y/n
  toilet2b = db.StringProperty(); #toilets have broken doors y/n
  toilet3a = db.StringProperty(); #toilets are there but not fuctional have no door y/n
  toilet3b = db.StringProperty(); #toilets lock on door missing y/n
  toilet3c = db.StringProperty(); #toilets have no water y/n
  toilet3d = db.StringProperty(); #toilets have no sewage mechanism y/n#
  toilet4 = db.StringProperty(); #toilets not available
  water1 = db.StringProperty(); #clean water? y/n
  water2a = db.StringProperty(); # no water supply y/n
  water2b = db.StringProperty(); # water is not clean y/n
  water2c = db.StringProperty(); # taps are not easily accessible y/n
  water3 = db.StringProperty(); # drinking water not available

class Report(db.Model):
  place = db.StringProperty()
  contact = db.StringProperty()
  blobkey = db.StringProperty()
  
class HeatMapValues(db.Model):
  lat = db.StringProperty()
  lon = db.StringProperty()
  score = db.StringProperty()
   
class MainHandler(webapp2.RequestHandler):
  def get(self):
    upload_url = blobstore.create_upload_url('/upload')
    self.response.out.write('<html><body>')
    self.response.out.write('<form action="%s" method="POST" enctype="multipart/form-data">' % upload_url)
    self.response.out.write('Complaint : <input type="text" name="contact"> <br>')
    #self.response.out.write('Region : <input type="text" name="region"> <br>')
    self.response.out.write('Place : <input type="text" name="place"> <br>')
    self.response.out.write("""Upload File: <input type="file" name="file"><br> <input type="submit"
        name="submit" value="Submit"> </form></body></html>""")

class UploadHandler(blobstore_handlers.BlobstoreUploadHandler):
  
  def post(self):
    donor = Report()
    donor.contact = self.request.get('contact')
    donor.place = self.request.get('place')
    upload_files = self.get_uploads('file')  # 'file' is file upload field in the form
    blob_info = upload_files[0]
    donor.blobkey = str(blob_info.key())
    donor.put()
    self.redirect('/')
    #self.redirect('/serve/%s' % blob_info.key())

class DataHandler(webapp2.RequestHandler):
  def get(self):
    self.response.out.write("This is a test write")
    logging.info("1")
    donor = Report()
    logging.info("2")
    donor.contact = 'sofihef'
    logging.info("3")
    donor.place = 'osnf'
    logging.info("4")
    donor.blobkey = 'sdfjhds'
    logging.info("5")
    donor.put()
    logging.info("6")
  def post(self):
    pass
    
class InputCoordinates(webapp2.RequestHandler):
  def get(self):
    self.response.out.write(coordinates_html)
  def post(self):
    h = HeatMapValues()
    h.lat = self.request.get('latitude')
    h.lon = self.request.get('longitude')
    h.score = self.request.get('score')
    h.put()

class ServeHandler(blobstore_handlers.BlobstoreDownloadHandler):
  def get(self, resource):
    resource = str(urllib.unquote(resource))
    blob_info = blobstore.BlobInfo.get(resource)
    self.send_blob(blob_info)


# class GenerateJson(webapp2.RequestHandler):
#   def get(self):
#     vals = db.GqlQuery("SELECT * from HeatMapValues")
#     json_values="{max:100, data["
#     for v in vals:
#       #self.response.out.write("lat:"+v.lat+" lon:"+v.lon+" score:"+v.score)
#       json_values+="{lat:"+v.lat+",lng:"+v.lon+",count: "+v.score+"}"
#     json_values+="]};"
#     # self.response.out.write(json_values);
    

heatMap_htmlp1 = """ 
  <html>
  <head>
  <meta name="viewport" content="initial-scale=1.0, user-scalable=no" />
  <title>SITA Heatmap</title>
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <style>
        body, html {
          margin:0;
          padding:0;
          font-family:Arial;
        }
        h1 {
          margin-bottom:10px;
        }
        #main {
          position:relative;
          width:1020px;
          padding:20px;
          margin:auto;
        }
        #heatmapArea {
          position:relative;
          float:left;
          width:800px;
          height:600px;
          border:1px dashed black;
        }
        #configArea {
          position:relative;
          float:left;
          width:200px;
          padding:15px;
          padding-top:0;
          padding-right:0;
        }
        .btn {
          margin-top:25px;
          padding:10px 20px 10px 20px;
          -moz-border-radius:15px;
          -o-border-radius:15px;
          -webkit-border-radius:15px;
          border-radius:15px;
          border:2px solid black;
          cursor:pointer;
          color:white;
          background-color:black;
        }
        #gen:hover{
          background-color:grey;
          color:black;
        }
        textarea{
          width:260px;
          padding:10px;
          height:200px;
        }
        h2{
          margin-top:0;
        }
      </style>
  <link rel="shortcut icon" type="image/png" href="http://www.patrick-wied.at/img/favicon.png" />
  <script type="text/javascript" src="http://maps.google.com/maps/api/js?sensor=false"></script>

  </head>
  <body>
  <div id="main">
        <h1>SITA HeatMap</h1>
        <div id="heatmapArea">
        
        </div>
        <div id="configArea">
          
          <div id="tog" class="btn">Toggle HeatmapOverlay</div>
          <div id="gen" class=""></div>
        </div>
        
  
  </div>
  <script type="text/javascript" src="http://www.patrick-wied.at/static/heatmapjs/src/heatmap.js"></script>
  <script type="text/javascript" src="http://www.patrick-wied.at/static/heatmapjs/src/heatmap-gmaps.js"></script>
  <script type="text/javascript">

  var map;
  var heatmap; 

  window.onload = function(){

    var myLatlng = new google.maps.LatLng(48.3333, 16.35);
    // sorry - this demo is a beta
    // there is lots of work todo
    // but I don't have enough time for eg redrawing on dragrelease right now
    var myOptions = {
      zoom: 2,
      center: myLatlng,
      mapTypeId: google.maps.MapTypeId.ROADMAP,
      disableDefaultUI: false,
      scrollwheel: true,
      draggable: true,
      navigationControl: true,
      mapTypeControl: false,
      scaleControl: true,
      disableDoubleClickZoom: false
    };
    map = new google.maps.Map(document.getElementById("heatmapArea"), myOptions);
    
    heatmap = new HeatmapOverlay(map, {"radius":15, "visible":true, "opacity":60});
    
    document.getElementById("gen").onclick = function(){
      var x = 5;
      while(x--){
      
        var lat = Math.random()*180;
        var lng = Math.random()*180;
        var count = Math.floor(Math.random()*180+1);
        
        heatmap.addDataPoint(lat,lng,count);
      
      }
    
    };
    
    document.getElementById("tog").onclick = function(){
      heatmap.toggle();
    };
  
  var testData=""" 

heatMap_htmlp2= """ 
    

  // this is important, because if you set the data set too early, the latlng/pixel projection doesn't work
  google.maps.event.addListenerOnce(map, "idle", function(){
    heatmap.setDataSet(testData);
  });
  };

  </script>
  </body>
  </html>

"""

class GenerateHeatMap(webapp2.RequestHandler):
    def get(self):
      vals = db.GqlQuery("SELECT * from HeatMapValues")
      json_values="{max:100, data:["
      for v in vals:
        #self.response.out.write("lat:"+v.lat+" lon:"+v.lon+" score:"+v.score)
        json_values+="{lat:"+v.lat+",lng:"+v.lon+",count: "+v.score+"},"
      json_values+="]};"
      logging.info(json_values)
      heatMap_html = heatMap_htmlp1 +json_values+ heatMap_htmlp2
      self.response.out.write(heatMap_html)
      pass






leaflet_htmlp1 = """

      <!DOCTYPE html>
      <html>
      <head>
      <title>Leaflet Quick Start Guide Example</title>


      <link rel="stylesheet" href="http://cdn.leafletjs.com/leaflet-0.7.2/leaflet.css" />
      </head>
      <body>
      <div id="map" style="width =100vw; height:100vh"></div>

      <script src="http://cdn.leafletjs.com/leaflet-0.7.2/leaflet.js"></script>
      <script>

      var map = L.map('map').setView([21.0000, 78.0000], 5);

      L.tileLayer('https://{s}.tiles.mapbox.com/v3/{id}/{z}/{x}/{y}.png', {
        maxZoom: 18,
        attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, ' +
          '<a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
          'Imagery © <a href="http://mapbox.com">Mapbox</a>',
        id: 'examples.map-9ijuk24y'
      }).addTo(map);


  """


leaflet_htmlp2 = """


  </script>
  </body>
  </html>


  """

class Leaflet(webapp2.RequestHandler):
  def get(self):
    leaflet = ''    
    vals = db.GqlQuery("SELECT * from HeatMapValues")
    for v in vals:
      if(int(v.score)<50):
        color="red"
      elif(int(v.score)>=50 and int(v.score)<=75):
        color="yellow"
      else:
        color = "green"

    #color = "red"
      logging.info("hola!")
      leaflet += """

      L.circle(["""+v.lat+""","""+v.lon+"""], 500, {
      color: '"""+color+"""',
      fillColor: '#f03',
      fillOpacity: 0.5
      }).addTo(map).bindPopup("I am a circle.");
      

      """
    logging.info(leaflet)
    self.response.out.write(leaflet_htmlp1+leaflet+leaflet_htmlp2)
      #self.response.out.write(leaflet)
    #self.response.out.write(leaflet_htmlp2)
    

realpost_html = """



  <html>

  <form action="realpost" method = "POST">

  <input type = "text" name = "entry2a">
  </form>

  </html>


"""

class RealPost(webapp2.RequestHandler):
  def get(self):
    self.response.out.write("The get method"+realpost_html)
  def post(self):
    s = 0
    a = ActualHeatMapValues()
    a.lat = self.request.get('lat')
    logging.info("lat"+self.request.get('lat'))
    

    a.lon = self.request.get('lon')
    logging.info("lon"+self.request.get('lon'))
    

    a.score = ''#TBD
    

    a.address = self.request.get('address')
    logging.info("address"+self.request.get('address'))
    

    a.city = self.request.get('city')
    logging.info("city"+self.request.get('city'))
    

    a.country = self.request.get('country')
    

    a.district = self.request.get('district')
    

    a.entry1 = self.request.get('entry1')
    if(self.request.get('entry1')=='y'):
      s+=1
    else:
      s-=1
    

    a.entry2a = self.request.get('entry2a')  #ramp y/n
    logging.info("entry2a"+self.request.get('entry2a'))
    if(self.request.get('entry2a')=='y'):
      s+=1
    else:
      s-=1
    a.entry2b = self.request.get('entry2b')  #ramp y/n
    if(self.request.get('entry2b')=='y'):
      s+=1
    else:
      s-=1
    logging.info(""+str(s))
    #self.response.out.write(""+score)
    a.entry2c = self.request.get('entry2c')  #ramp y/n
    if(self.request.get('entry2c')=='y'):
      s+=1
    else:
      s-=1

    a.entry2d = self.request.get('entry2d')  #ramp y/n
    if(self.request.get('entry2d')=='y'):
      s+=1
    else:
      s-=1

    a.entry3 = self.request.get('entry3')   #ramp exists y/n
    if(self.request.get('entry3')=='y'):
      s+=1
    else:
      s-=1

    a.ground1 = self.request.get('ground1')   #ground well maintained y/n
    if(self.request.get('ground1')=='y'):
      s+=1
    else:
      s-=1



    a.ground2a = self.request.get('ground2a')  #rocky ground y/n
    if(self.request.get('ground2a')=='y'):
      s+=1
    else:
      s-=1


    a.ground2b = self.request.get('ground2b')  #uneven y/n
    if(self.request.get('ground2b')=='y'):
      s+=1
    else:
      s-=1

    a.ground2c = self.request.get('ground2c')  #used for other purposes y/n
    if(self.request.get('ground2c')=='y'):
      s+=1
    else:
      s-=1

    a.ground3 = self.request.get('ground3')  #playground does not exist y/n
    if(self.request.get('ground2c')=='y'):
      s+=1
    else:
      s-=1


    a.library1 = self.request.get('library1') # library facility is available y/n
    if(self.request.get('library1')=='y'):
      s+=1
    else:
      s-=1



    a.library2a = self.request.get('library2a') # library locked y/n
    if(self.request.get('library2a')=='y'):
      s+=1
    else:
      s-=1


    a.library2b = self.request.get('library2b') # library books kept beyond students reach y/n
    if(self.request.get('library2b')=='y'):
      s+=1
    else:
      s-=1

    a.library2c = self.request.get('library2c') # no time alloted in time table y/n
    if(self.request.get('library2c')=='y'):
      s+=1
    else:
      s-=1

    a.library2d = self.request.get('library2d') # insufficient number of books y/n
    if(self.request.get('library2d')=='y'):
      s+=1
    else:
      s-=1

    a.library3 = self.request.get('library3'); # library facility is not available y/n
    if(self.request.get('library3')=='y'):
      s+=1
    else:
      s-=1

    a.name = self.request.get('name') # name
    
    a.pin = self.request.get('pin') #pincode
    
    a.repname = self.request.get('repname') #uploader name
    
    a.repphone = self.request.get('repphone') #uploader phone
    
    a.state = self.request.get('state') #state 
    
    a.taluk = self.request.get('taluk') #taluk
    
    a.toilet1 = self.request.get('toilet1') #toilets have working doors y/n
    if(self.request.get('toilet1')=='y'):
      s+=1
    else:
      s-=1

    a.toilet2a = self.request.get('toilet2a') #toilets are dirty y/n
    if(self.request.get('toilet2a')=='y'):
      s+=1
    else:
      s-=1

    a.toilet2b = self.request.get('toilet2b') #toilets have broken doors y/n
    if(self.request.get('toilet2b')=='y'):
      s+=1
    else:
      s-=1

    a.toilet3a = self.request.get('toilet3a') #toilets are there but not fuctional have no door y/n
    if(self.request.get('toilet3a')=='y'):
      s+=1
    else:
      s-=1

    a.toilet3b = self.request.get('toilet3b') #toilets lock on door missing y/n
    if(self.request.get('toilet3b')=='y'):
      s+=1
    else:
      s-=1


    a.toilet3c = self.request.get('toilet3c') #toilets have no water y/n
    if(self.request.get('toilet3c')=='y'):
      s+=1
    else:
      s-=1

    a.toilet3d = self.request.get('toilet3d') #toilets have no sewage mechanism y/n#
    if(self.request.get('toilet3d')=='y'):
      s+=1
    else:
      s-=1

    a.toilet4 = self.request.get('toilet4') #toilets not available
    if(self.request.get('toilet4')=='y'):
      s+=1
    else:
      s-=1


    a.water1 = self.request.get('water1') #clean water? y/n
    if(self.request.get('water1')=='y'):
      s+=1
    else:
      s-=1

    a.water2a = self.request.get('water2a') # no water supply y/n
    if(self.request.get('water2a')=='y'):
      s+=1
    else:
      s-=1

    a.water2b = self.request.get('water2b') # water is not clean y/n
    if(self.request.get('water2b')=='y'):
      s+=1
    else:
      s-=1

    a.water2c = self.request.get('water2c') # taps are not easily accessible y/n
    if(self.request.get('water2c')=='y'):
      s+=1
    else:
      s-=1

    a.water3 = self.request.get('water3') # drinking water not available
    if(self.request.get('water3')=='y'):
      s+=1
    else:
      s-=1

    logging.info("total:"+str(s))
    s = s/10;
    s = s*10;
    a.score = str(s)
    self.response.out.write("got the values")
    a.put()
    logging.info('values inserted into datastore')


class RealHeat(webapp2.RequestHandler):
  def get(self):
      vals = db.GqlQuery("SELECT * from ActualHeatMapValues")
      json_values="{max:100, data:["
      for v in vals:
        #self.response.out.write("lat:"+v.lat+" lon:"+v.lon+" score:"+v.score)
        if (v.lat == ""):
          v.lat = "12.42"
        if (v.lon== ""):
          v.lon = "23.45"
        if(v.score == ""):
          v.score = "90"

        json_values+="{lat:"+v.lat+",lng:"+v.lon+",count: "+v.score+"},"
      json_values+="]};"
      logging.info(json_values)
      heatMap_html = heatMap_htmlp1 +json_values+ heatMap_htmlp2
      self.response.out.write(heatMap_html)
      pass


class RealLeaf(webapp2.RequestHandler):
  def get(self):
    leaflet = ''    
    vals = db.GqlQuery("SELECT * from ActualHeatMapValues")
    for v in vals:
      if(v.score):
        if(int(v.score)<50):
          color="red"
        elif(int(v.score)>=50 and int(v.score)<=75):
          color="yellow"
        else:
          color = "green"

      #color = "red"
        logging.info("hola!")
        if(v.lat == ""):
          v.lat="12.32"
        if(v.lon == ""):
          v.lon = "23.43"
        if(v.name == ""):
          v.name = "school name missing"
        if(v.address == ""):
          v.address = "school address missing" 
        leaflet += """

        L.circle(["""+v.lat+""","""+v.lon+"""], 500, {
        color: '"""+color+"""',
        fillColor: '#f03',
        fillOpacity: 0.5
        }).addTo(map).bindPopup('"""+v.name+""","""+v.address+"""');
        

        """
    logging.info(leaflet)
    self.response.out.write(leaflet_htmlp1+leaflet+leaflet_htmlp2)



class RealGet(webapp2.RequestHandler):
  def get(self):
    self.response.headers['Access-Control-Allow-Origin'] = '*'
    self.response.out.write("""[""")
    vals = db.GqlQuery("SELECT * from ActualHeatMapValues")
    count =0
    for v in vals:

        
        if (count==0):
          count=1
        else:
          self.response.out.write(""",""")
        self.response.out.write("""{"name":"
          """+v.name+"""
          ","address":"
          """+v.address+"""
          ","city":"
          """+v.city+"""
          ","state":"
          """+v.state+"""
          ","ramp":"
          """+v.entry1+"""
          ","ground":"
          """+v.ground1+"""
          ","library":"
          """+v.library1+"""
          ","toilet":"
          """+v.toilet1+"""
          ","water":"
          """+v.water1+"""
          "}""")
    self.response.out.write("""]""")    
        

app = webapp2.WSGIApplication([('/', MainHandler),
                               ('/upload', UploadHandler),
                               ('/serve/([^/]+)?', ServeHandler),
                               ('/data', DataHandler),
                               ('/coin', InputCoordinates),
                               ('/heatmap', GenerateHeatMap),
                               ('/leaflet', Leaflet),
                               ('/realpost', RealPost),
                               ('/realheat', RealHeat),
                               ('/realleaf', RealLeaf),
                               ('/realget', RealGet)],
                              debug=True)