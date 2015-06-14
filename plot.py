#!/usr/bin/env python
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter, WeekdayLocator,\
     DayLocator, MONDAY
from matplotlib.finance import quotes_historical_yahoo_ohlc, candlestick_ohlc
from grs import Stock
from matplotlib.dates import date2num
import datetime

class Manager(object):

    def get_stock(self, stock, month):
        res = []
        _stock = Stock(stock, month)
        raw_data = _stock.raw
        print raw_data
        for data in raw_data:
            re0 = [int(val) for val in data[0].split('/')]
            re0[0] = re0[0] + 1911
            dt = datetime.date(*re0)
            print dt
            date = date2num(dt)
            tp_data = (
                       date,
                       data[3],
                       data[4],
                       data[5],
                       data[6]
            )
            res.append(tp_data)
        print res
        return res

    def plot_finance(self):
    # (Year, month, day) tuples suffice as args for quotes_historical_yahoo
        date1 = (2014, 1, 1)
        date2 = (2014, 1, 2) 
    
    
        mondays = WeekdayLocator(MONDAY)        # major ticks on the mondays
        alldays = DayLocator()              # minor ticks on the days
        weekFormatter = DateFormatter('%b %d')  # e.g., Jan 12
        dayFormatter = DateFormatter('%d')      # e.g., 12
    
        #quotes = quotes_historical_yahoo_ohlc('INTC', date1, date2)
        quotes = self.get_stock('3057', 12)
        if len(quotes) == 0:
            raise SystemExit
        print quotes
    
        fig, ax = plt.subplots()
        fig.subplots_adjust(bottom=0.2)
        ax.xaxis.set_major_locator(mondays)
        ax.xaxis.set_minor_locator(alldays)
        ax.xaxis.set_major_formatter(weekFormatter)
        #ax.xaxis.set_minor_formatter(dayFormatter)
    
        #plot_day_summary(ax, quotes, ticksize=3)
        candlestick_ohlc(ax, quotes, width=0.6)
    
        ax.xaxis_date()
        ax.autoscale_view()
        plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')
    
        plt.show()

if __name__ == '__main__':
    st = Manager()
    st.plot_finance()
