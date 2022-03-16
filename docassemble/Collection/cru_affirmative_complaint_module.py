from docassemble.base.core import DAObject, DAList # import parent classes from .core
from docassemble.base.util import Person, Address # import parent classes from .util

__all__ = ['Collector', 'CollectorList', 'Debt', 'DebtList', 'Damages', 'DamagesList', 'CreditReport', 'SimpleCreditReport', 'CreditReportList', 'DisputedItem', 'DisputedItemList'] # list every class name here as a string element in a list, or else docassemble can't find it in the module.

class Collector(Person):
  """Represents an entity (individual or corporate) that is trying to collect a debt (in a colloquial sense) from a client. May or may not be an FDCPA debt collector or original creditor. """
  def init(self, *pargs, **kwargs):
    super(Collector, self).init(*pargs, **kwargs) # standard form of an .init() method for a docassemble object
  @property # docassemble expects an attribute, not a method for the purposes of ."complete_attribute". The decorator tells docassemble to look here for the "attribute".
  def collector_complete(self): # tells docassemble what attributes to gather, and in what order, for gathering purposes
      self.name
      self.address
      self.collector_type
      return True 

class CollectorList(DAList):
  """Represents a list of Collector objects."""
  def init(self, *pargs, **kwargs):
    super(CollectorList, self).init(*pargs, **kwargs)
    self.object_type = Collector # tells docassemble that this will be a list of Collector() objects.
    self.complete_attribute = 'collector_complete' # names the attribute that needs to return True for gathering to be complete. See Collector() above.

class Debt(DAObject):
    """Represents a single account owed to a single entity by a client."""
    def init(self, *pargs, **kwargs):
        super(Debt, self).init(*pargs, **kwargs)
        self.initializeAttribute('collector_list', CollectorList) # need to do this when and attribute is an object
        self.initializeAttribute('address', Address)
        self.initializeAttribute('damages', Damages)
    def name_debt(self): # provides predictability to how object names are displayed as text
        for collector in self.collector_list:
          if collector.collector_type == 'original creditor':
            self.name = str(collector) + ' ' + '$' + str(self.amount) + ' ' + 'debt'
            break
        else:
          self.name = 'Unknown' + ' ' + '$' + str(self.amount) + ' ' + 'debt'
    @property
    def debt_complete(self):
        # self.collector_list # is going to be both debt collectors and original creditors
        self.debt_collectors
        if hasattr(self, 'original_creditor'): # lets gathering continue despite not knowing who the original creditor is
          pass
        else:
          pass
        self.amount
        self.date_of_default
        self.damages
        # self.address
        # self.amount
        # self.in_court
        # self.case
        return True

class DebtList(DAList):
    """Represents a list of Debt objects."""
    def init(self, *pargs, **kwargs):
        super(DebtList, self).init(*pargs, **kwargs)
        self.object_type = Debt
        self.complete_attribute = "debt_complete"

class Damages(DAObject):
  """Represents damages traceable to a particular debt"""
  def init(self, *pargs, **kwargs):
    super(Damages, self).init(*pargs, **kwargs)
  @property
  def damages_complete(self):
      self.financial_description
      self.financial_amount
      self.emotional_description
      self.emotional_amount
      self.fees
      self.costs
      return True

class DamagesList(DAList):
  """Represents a list of Damages objects."""
  def init(self, *pargs, **kwargs):
    super(DamagesList, self).init(*pargs, **kwargs)
    self.object_type = Damages
    self.complete_attribute = 'damages_complete'
    

class CreditReport(DAObject):
  """Represents a single consumer report."""
  def init(self, *pargs, **kwargs):
    super(CreditReport, self).init(*pargs, **kwargs)
    self.initializeAttribute('address', Address) # need to do this when and attribute is an object
    self.initializeAttribute('debts', DebtList)
    self.initializeAttribute('disputed_items', DisputedItemList)
    self.initializeAttribute('enclosures', DAList)
  def name_report(self):
    self.name = str(self.consumer_reporting_agency.name) + ' ' + 'Credit Report'
  @property
  def credit_report_complete(self):
    self.address
    self.date
    self.debts
    self.disputed_items
    self.enclosures
    return True

class SimpleCreditReport(): # simple credit report class with no docassemble .gather() functionality
    def __init__(self, name, street_address, city, state, zip):
        self.name = name
        self.street_address = street_address
        self.city = city
        self.state = state
        self.zip = zip
        
class CreditReportList(DAList):
  """Represents a list of CreditReport objects."""
  def init(self, *pargs, **kwargs):
    super(CreditReportList, self).init(*pargs, **kwargs)
    self.object_type = CreditReport
    self.complete_attribute = 'credit_report_complete'

class DisputedItem(DAObject):
  """Represents reporting on a CreditReport object related to a 
    single debt that a consumer is disputing."""
  def init(self, *pargs, **kwargs):
    super(DisputedItem, self).init(*pargs, **kwargs)
  @property
  def disputed_items_complete(self):
    if hasattr(self, 'id_number'): # lets gathering continue despite there being no id number
      pass
    else:
      pass
    self.explanation
    self.solution
    return True
 
class DisputedItemList(DAList):
  """Represents a list of DisputedItem objects."""
  def init(self, *pargs, **kwargs):
    super(DisputedItemList, self).init(*pargs, **kwargs)
    self.object_type = DisputedItem
    self.complete_attribute = 'disputed_items_complete'
   
def cra_airtable_function():

    import itertools
    import requests
    import airtable

    agencies = dict() # name of the agency
    street_addresses = dict()
    cities = dict()
    states = dict()
    zips = dict()

    airtable = airtable.Airtable('app6jzEHzK1Xpz0xC', 'key6QH3se2Itq6TJl') # gets the contents of an airtable we made with information on all the tenant screening orgs identified by the CFPB. This is currently the test environment api key.
    tenant_screeners = airtable.get(table_name='Tenant_Screening_Companies', fields=["Agency", "Street Address", "City", "State", "Zip" ]) # dumps the airtable into a variable, which is a monster of a data structure. It's a nested dictionary full of tuples.


    length = len(tenant_screeners['records']) # this corresponds to the number of rows in the airtable, so we can know how many times the while loop below has to run
    index = 0 # sets the counter of the while loop at 0.


    while index < length: # populates the empty dicts() created above.
        agencies[index] = tenant_screeners['records'][index]['fields']['Agency']
        street_addresses[index] = tenant_screeners['records'][index]['fields']['Street Address']
        cities[index] = tenant_screeners['records'][index]['fields']['City']
        states[index] = tenant_screeners['records'][index]['fields']['State']
        zips[index] = tenant_screeners['records'][index]['fields']['Zip']
        index = index +  1

    ''' the output of the while loop above is a series of dictionaries where the keys are equal to the index and the values 
    are the actual information we want, so below we strip out the keys and just keep the values '''

    agencies = agencies.values()
    street_addresses = street_addresses.values()
    cities = cities.values()
    states = states.values()
    zips = zips.values()

    ''' we then use the zip function to combine our separate dictionaries back into one data structure, but this time one we know how to manipulate '''

    all_results = zip(agencies, street_addresses, cities, states, zips) # this is what the function should return

    return all_results  







  
