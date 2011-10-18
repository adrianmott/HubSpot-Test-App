import cgi
from pyspot import *

from google.appengine.ext import db
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class MainPage(webapp.RequestHandler):
    def get(self):
        self.response.out.write("""
          <html>
            <head>
            <title>Title in header (should be Stripped)</title>
            <link rel=stylesheet href="https://leads-search.appspot.com/stylesheets/bootstrap.css" type="text/css" />
            </head>
            <body>
            <div class="container">
              <hs:link rel="stylesheet" href="https://leads-search.appspot.com/stylesheets/bootstrap.css" type="text/css" />
              <img src="http://adrianmott.com/images/amott.png" />
              <hs:title>Ttile in Body (should be present in the app!)</hs:title>
              <!-- <a href="http://adrianmott.com">click me</a> -->
              <form name="guidform" action="result" method="post">
                <div class="clearfix">
              		<label for="xlInput">Search for a lead by email, last name, first name or company:</label>
                  <div class="input">
                    <input class="xlarge" id="xlInput" name="search_field" size="30" type="text" />
                  </div>
                </div>
                <div class="clearfix">
                  <label for="xlInput">Enter your API Key: </label>
                  <div class="input">
                    <input class="xlarge" id="xlInput" name="api_key" size="30" type="text" />
                  </div>
                </div>
                <div class="clearfix">
                  <div class="actions">
                    <button type="submit" class="btn danger">Get Lead Info</button>&nbsp;<button type="reset" class="btn">Cancel</button>
                  </div>
                </div>
          		</form>
            </div>
            </body>
          </html>""")
    


class LeadSearch(webapp.RequestHandler):
    def post(self):
        api_key = (cgi.escape(self.request.get('api_key')))
        search_param = self.request.get('search_field')
        hs_client = HubSpotLeadsClient(api_key)
        lead = hs_client.search_leads(search_param)
        lead_count = 0
        caller = self.request.get('hubspot.marketplace.caller')
        user_id = self.request.get('hubspot.marketplace.user_id')
        portal_id = self.request.get('hubspot.marketplace.portal_id')
        app_name = self.request.get('hubspot.marketplace.app.name')
        callback = self.request.get('hubspot.marketplace.app.callbackUrl')
        page_url = self.request.get('hubspot.marketplace.app.pageUrl')
        canvas_url = self.request.get('hubspot.marketplace.app.canvasUrl')
        signature = self.request.get('hubspot.marketplace.signature')
        for leads in lead:
            #print leads.guid #and whatever else you want to pull from the lead!
            lead_count += 1
            self.response.out.write("""
            <link rel=stylesheet href="https://leads-search.appspot.com/stylesheets/bootstrap.css" type="text/css" />
            <div class="container">
            <h2>Lead %d</h2>
            <p class='detail'>Lead GUID: %s<br>
            <p class='detail'>Name: %s %s <br> 
            <p class='detail'>Email: %s <br>
            <p class='detail'>Phone: %s<br>
            <p class='detail'>Company: %s <br>
            <p class='detail'>Page Views: %s<br>
            <p class='detail'>Visits: %s <br>
            <p class='detail'>First URL: %s<br>
            <p class='detail'>Found the Site Via: %s<br>"""
            % (lead_count, leads.guid, leads.first_name, leads.last_name, leads.email, leads.phone, leads.company, leads.page_views, leads.visits, leads.first_url, leads.found_via))
            if (leads.is_customer == True):
                self.response.out.write("""<p class="detail">Customer or Lead?: Customer<br>""")
                self.response.out.write("""
                <p class="param">Caller: %s <br>
                <p class="param">User ID: %s <br>
                <p class="param">Portal ID: %s <br>
                <p class="param">App Name: %s <br>
                <p class="param">Callback URL: %s <br>
                <p class="param">Page URL: %s <br>
                <p class="param">Canvas URL: %s <br>
                <p class="param">Request Signature: %s <br>"""
                % (caller, user_id, portal_id, app_name, callback, page_url, canvas_url, signature))
            else:
                self.response.out.write("""<p class="detail">Customer or Lead?: Lead<br>""")
                self.response.out.write("""
                <p class="detail">Lead Link: <a href=%s>Click Here</a> <br>
                <p class="detail">Lead Grade: %s<br>
                <p class="detail">Twitter Username: %s<br>
                <p class="detail">Website: %s<br>
                <p class="detail">Lead Nurturing Active?: %s <br>
                </div></body></html>"""
                % (leads.public_lead_link, leads.lead_score, leads.twitter_name, leads.website, leads.lead_nurturing_active))
                self.response.out.write("""
                <p class="param">Caller: %s <br>
                <p class="param">User ID: %s <br>
                <p class="param">Portal ID: %s <br>
                <p class="param">App Name: %s <br>
                <p class="param">Callback URL: %s <br>
                <p class="param">Page URL: %s <br>
                <p class="param">Canvas URL: %s <br>
                <p class="param">Request Signature: %s <br>"""
                % (caller, user_id, portal_id, app_name, callback, page_url, canvas_url, signature))
                    

application = webapp.WSGIApplication(
    [('/', MainPage),
    ('/result', LeadSearch)],
    debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()

