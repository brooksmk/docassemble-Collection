# docassemble-madebtcollections

## Changelog

* 2018-09-26 Stripped down validation/exemption/do-not call letter to more basic 
  functionality. Removed statements about social security income.
  
* 2018-09-26 removed GBLS logo from validationOnly template.

* 2018-09-26 fixed bug where interview used wrong template.

* 2018-09-26 fixed additional bug where interview used wrong template.

* 2018-10-04 added metadata block to display interview title on GBLS website.

* 2018-10-09 added signature capability to validationOnly interview.

* 2018-10-15 corrected bug where validationOnly template included do not call language
  in validation letters.
  
* 2018-10-15 added client address to address block in template.

* 2018-12-03 changed package description, renamed validation/do not call letter
  interview, fixed validation / do not call letter error where wrong name was displaying for original
  creditor, changed validation / do not call letter formatting, added ability for
  interviewee to add additional information to validation / do not call letter.
  
* 2018-12-03 uploaded new validation/do not call letter template.

* 2018-12-03 added motion to vacate default and certificate of service interviews

* 2018-12-05 readded motion to vacate default interview after restoring lost code.

* 2018-12-05 removed title from certificateOfService metadata block.

* 2018-12-05 added intro screen to motionToVacateDefault.

* 2018-12-21 adding exemptions interview and function.

* 2018-12-25 changing exemptions function and adding table display

* 2018-12-27 added questions related to non-wage income to exemptOrNot.

* 2018-12-28 added warning message related to pension/annuity/retirement income to exemptOrNot.

* 2018-12-28 added Unemployment to fully exempt income amounts and corrected exemptOrNot.py

* 2019-01-06 added exit screen for users seeking information about child support or government debts, updated exemptOrNot.py for new Massachusetts minimum wage

* 2019-01-07 added support for fully non-exempt types of income, fixed out of index error where jobs or non_job_income lists were empty.

* 2019-02-18 added support for assets.

* 2019-02-19 fixed issue where text was being displayed in a gray box like it was code because 
  apparently in Markdown four spaces means "format something to look like code".
  Who knew!

* 2019-03-02 deleted various unused .yml files, python modules, and one template.
