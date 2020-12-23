from docassemble.base.core import DAObject, DAList # import parent classes from .core
from docassemble.base.util import Person, Address # import parent classes from .util

__all__ = ['Collector','CollectorList', 'Debt', 'DebtList', 'Damages', 'DamagesList'] # list every class name here as a string element in a list, or else docassemble can't find it in the module.

class Collector (Person):
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

class Debt (DAObject):
    """Represents a single account owed to a single entity by a client."""
    def init(self, *pargs, **kwargs):
        super(Debt, self).init(*pargs, **kwargs)
        self.initializeAttribute('collector_list', CollectorList) # need to do this when and attribute is an object
        self.initializeAttribute('address', Address)
        self.initializeAttribute('damages', Damages)
    def name_debt(self): # provides predictability to how object names are displayed as text
        if hasattr(self, 'original_creditor'):
          self.name = str(self.original_creditor) + ' ' + '$' + str(self.amount) + ' ' + 'debt'
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
      
class DebtList(DAList):
    """Represents a list of Debt objects."""
    def init(self, *pargs, **kwargs):
        super(DebtList, self).init(*pargs, **kwargs)
        self.object_type = Debt
        self.complete_attribute = "debt_complete"



  