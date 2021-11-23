# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 14:53:40 2020
@author: Vivek SRIVASTAVA
"""

import datetime 
import pandas as pd
from pandas.tseries.holiday import AbstractHolidayCalendar, Holiday, nearest_workday, \
    USMartinLutherKingJr, USPresidentsDay, GoodFriday, USMemorialDay, \
    USLaborDay, USThanksgivingDay

'''
 
'''
class USTradingCalendar(AbstractHolidayCalendar):
    """
    This class inherits from an Abstract Calendar and consists of only weekends.
    All popular US holidays have been added to this class manually. 
    Below is the Holiday List
        Holiday('New Years Day', month=1, day=1, observance=nearest_workday),
        USMartinLutherKingJr,
        USPresidentsDay,
        GoodFriday,
        USMemorialDay,
        Holiday('US Independence Day', month=7, day=4, observance=nearest_workday),
        USLaborDay,
        USThanksgivingDay,
        Holiday('Christmas', month=12, day=25, observance=nearest_workday)
    Object of this class consists of CheckHoliday method
    which checks if the passed argument is a US Holiday or not and returns the object
    
    """
    rules = [
        Holiday('New Years Day', month=1, day=1, observance=nearest_workday),
        USMartinLutherKingJr,
        USPresidentsDay,
        GoodFriday,
        USMemorialDay,
        Holiday('US Independence Day', month=7, day=4, observance=nearest_workday),
        USLaborDay,
        USThanksgivingDay,
        Holiday('Christmas', month=12, day=25, observance=nearest_workday)
        ]
    
    def CheckHoliday(self,check_date):
        
        """
        |- Feed this method a date in the format of 'YYYY-MM-DD' or a datetime.date object
        |- similar to datetime.date(YYYY, MM, DD)
        |- This method from the USTradingCalendar returns the object itself.
             
        |- Below is the response returned by the method
        |- inst = inst.CheckHoliday('YYYY-MM-DD')
        |- Returned object consists of below attributes:
            |- inst.BoolResponse: Checks whether the passed argument is a US Holiday or not
            |- inst.HolidayName: Returns the name of the Holiday
            |- inst.UserFriendlyResponse: If the user wants to print a default message
            |- inst.Holidays: This attributes holds a dataframe of Holiday dates and corresponding names
        """
        if isinstance(check_date,str):
            target_year = datetime.datetime.strptime(check_date,"%Y-%m-%d").year
            target_date = datetime.datetime.strptime(check_date,"%Y-%m-%d")
        elif isinstance(check_date,datetime.date):
            target_year = check_date.year
            target_date = check_date
        USHolidays = self.holidays(datetime.datetime(target_year-1, 12, 31), datetime.datetime(target_year, 12, 31),return_name=True)
        USHolidays= USHolidays.reset_index(name='Holidays').rename(columns={'index':'Date'})
        USHolidays["Date"]=pd.to_datetime(USHolidays["Date"])
        if pd.to_datetime(target_date) in set(USHolidays["Date"]):
            self.HolidayName=USHolidays[USHolidays["Date"]==pd.Timestamp(target_date)]["Holidays"][1]
            self.UserFriendlyResponse=f"It was a US Holiday on {target_date.strftime('%Y-%m-%d')} on account of {self.HolidayName}"
            self.BoolResponse= True
        else:
            self.UserFriendlyResponse= f"It was a not a US Holiday on {target_date.strftime('%Y-%m-%d')}."
            self.BoolResponse= False
            self.HolidayName=None
        return self
