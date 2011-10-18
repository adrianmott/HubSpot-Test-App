class Lead():
  '''Defines the HubSpot Lead object for use in the PySpot Wrapper'''
  def __init__(self, lead_data):
    self.data_parse(lead_data)
  
  def data_parse(self, lead_data):
    self.address = lead_data['address']
    self.analytics_details = lead_data['analyticsDetails']
    self.views_imported = lead_data['analyticsDetails']['allViewsImported']
    self.modified_time = lead_data['analyticsDetails']['countsModifiedAt']
    self.first_visit = lead_data['analyticsDetails']['firstVisitAt']
    self.last_page_view_time = lead_data['analyticsDetails']['lastPageViewAt']
    self.last_visit_time = lead_data['analyticsDetails']['lastVisitAt']
    self.page_views = lead_data['analyticsDetails']['pageViewCount']
    self.visits = lead_data['analyticsDetails']['visitCount']
    self.city = lead_data['city']
    self.closed_at = lead_data['closedAt']
    self.company = lead_data['company']
    self.country = lead_data['country']
    self.crm_details = lead_data['crmDetails']
    
    self.eligible_for_email = lead_data['eligibleForEmail']
    self.email = lead_data['email']
    self.email_bounced = lead_data['emailBounced']
    self.email_opt_out = lead_data['emailOptOut']
    self.fax = lead_data['fax']
    self.first_campaign = lead_data['firstCampaign']
    self.first_name = lead_data['firstName']
    self.first_referring_domain = lead_data['firstRefDomain']
    self.first_referrer_url = lead_data['firstReferrer']
    self.first_url = lead_data['firstURL']
    self.first_visit_time = lead_data['firstVisitSetAt']
    self.found_via = lead_data['foundVia']
    self.full_found_via = lead_data['fullFoundViaString']
    self.guid = lead_data['guid']
    self.is_imported = lead_data['imported']
    self.industry = lead_data['industry']
    self.converted_time = lead_data['insertedAt']
    self.ip_address = lead_data['ipAddress']
    self.is_customer = lead_data['isCustomer']
    self.is_deleted = lead_data['isDeleted']
    self.title = lead_data['jobTitle']
    self.last_converted_time = lead_data['lastConvertedAt']
    self.last_modified_time = lead_data['lastModifiedAt']
    self.last_name = lead_data['lastName']
    #add forms here - or custom fields when bedrock is ready!!
    self.lead_json_link = lead_data['leadJsonLink']
    self.private_lead_link = lead_data['leadLink']
    self.public_lead_link = lead_data['publicLeadLink']
    self.lead_nurturing_active = lead_data['leadNurturingActive']
    self.lead_nurturing_campaign_id = lead_data['leadNurturingCampaignId']
    self.message = lead_data['message']
    self.num_conversion_events = lead_data['numConversionEvents']
    self.phone = lead_data['phone']
    self.portal_id = lead_data['portalId']
    self.raw_lead_score = lead_data['rawScore']
    self.salutation = lead_data['salutation']
    self.lead_score = lead_data['score']
    self.source_id = lead_data['sourceId']
    self.state = lead_data['state']
    self.twitter_name = lead_data['twitterHandle']
    self.user_token = lead_data['userToken']
    self.website = lead_data['website']
    self.zip_code = lead_data['zip']
  


    