# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 19:07:24 2020

@author: surface book
"""

from layout import Ui_Form as Ui_Dialog
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from csv_read import csv_read
from concurrent.futures import ThreadPoolExecutor

import matplotlib
matplotlib.use("Qt5Agg")  # use QT5 for matplot
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.pyplot import MultipleLocator

# basically as same as plt class, 
# but this figure can show graphs in QTpy5
class MyFigure(FigureCanvas):
    def __init__(self,width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        super(MyFigure,self).__init__(self.fig)
        self.axes = self.fig.add_subplot(111)

# class including fuchtions of building graphs        
class Graphs:
     
    # generate cases&time graph
    def plotcase(self):
        
        # initialize csv_read class
        # you can see the code of the class in csv_read.py
        read = csv_read('us_covid19_daily_old.csv')
        self.cases, time = read.cases_time()
        
        for i in range(5):
            time.append('next{}'.format(i+1))
            
        self.time = time[:]
        grow_rate = 0
        
        for day in range(len(self.cases) - 6, len(self.cases)):
            if day+1 < len(self.cases):
                present = self.cases[day]
                next_day = self.cases[day+1]
                grow_rate += (next_day - present)/present
                
        grow_rate = grow_rate / 5
        print('5-day-growth rate{}'.format(grow_rate)) 
        prediction = [self.cases[len(self.cases)-5]]
        
        for day in range(9):
            if day+1 < 10:
                prediction.append(prediction[day]*(1+grow_rate))
        #     
        x_locat = MultipleLocator(5)
        self.F.axes.xaxis.set_major_locator(x_locat)
        # add a plot of Cumulative cases
        self.F.axes.plot(time[:-5], self.cases, 
                         marker = 'o',
                         label = 'Cumulative cases',
                         color = '#FF7E00')
        # add plot of Predicted Cases
        self.F.axes.plot(time[len(time) - 10:], prediction, 
                              color = 'black',
                              marker = 'o', 
                              alpha = 0.1,
                              label = 'Predicted Cases')
        # add title of the graph
        self.F.fig.suptitle("Confirmed Cases in US", size = 'xx-large')
        # add legend
        self.F.axes.legend()
        # add a single text
        self.F.axes.text(len(self.cases)-3, int(prediction[-1])*0.89,
                         '5-day Groth Rate:{:.2f}%'.format(grow_rate*100),
                         color = 'black',
                         style = 'oblique',
                         size = 'large',
                         alpha = 0.4)
        # add a text used to show data of a single note when mouse move on it
        self.num = self.F.axes.text(1, 500000, '',
                                    color = '#FF4500',
                                    style = 'oblique',
                                    size = 'large',
                                    ha = 'center',
                                    bbox = {'facecolor' : 'white',
                                            'alpha' : 0.75,
                                            'edgecolor' : '#FF975A'})
        self.mark = self.F.axes.text(1, 500000, '',
                                    color = '#FF3030',
                                    style = 'oblique',
                                    size = '24',
                                    ha = 'center',
                                    va = 'center')
                                            
        self.F.axes.set_xlabel('Date')
        self.F.axes.set_ylabel('Cases')
        self.F.axes.spines['right'].set_visible(False)
        self.F.axes.spines['top'].set_visible(False)
        # when mouse move on the graph, it can trigger the function onmove() 
        self.F.mpl_connect('motion_notify_event', self.onmove)
     
    # generate the map of death graph
    def plotdeatharea(self):
        read = csv_read('time_series_covid_19_deaths_US.csv')
        state_death = read.states_death()
        x = 0
        for item in state_death:
            if item[1] > 0:
                self.F1.axes.barh(item[0], item[1])
                self.F1.axes.text(item[1]*1.05, x - 0.3, item[1],
                                  size = 'large')
                x += 1
        self.F1.axes.set_xscale('log')
        self.F1.axes.set_xlabel('Death')
        
        self.F1.axes.spines['right'].set_visible(False)
        self.F1.axes.spines['top'].set_visible(False)
        
        self.F1.axes.set_title("Only showing the states having death cases", 
                               size = 'large')
        self.F1.fig.suptitle("Death of states", size = 'xx-large')
        
     # generate the graph showing cured and death    
    def plotdeathcured(self):
        read = csv_read('us_covid19_daily_old.csv')
        self.death, self.cured, self.timedeath = read.reco_death()
        x_locat = MultipleLocator(5)
        self.F2.axes.xaxis.set_major_locator(x_locat)
        self.F2.axes.plot(self.timedeath, self.death, 
                         marker = 'o',
                         label = 'Death',
                         color = '#FF4F05')
        self.F2.axes.plot(self.timedeath, self.cured, 
                         marker = 'o',
                         label = 'Cured',
                         color = '#20B2AA')
        self.F2.axes.legend()
        self.F2.fig.suptitle("Cured and Death", size = 'xx-large')
        self.num_dea = self.F2.axes.text(1, 5, '',
                                    color = '#FF3030',
                                    style = 'oblique',
                                    size = 'large',
                                    ha = 'center',
                                    bbox = {'facecolor' : 'white',
                                            'alpha' : 0.75,
                                            'edgecolor' : '#FF3030'})
                                            
        self.num_cur = self.F2.axes.text(1, 5, '',
                                    color = '#27408B',
                                    style = 'oblique',
                                    size = 'large',
                                    ha = 'center',
                                    bbox = {'facecolor' : 'white',
                                            'alpha' : 0.75,
                                            'edgecolor' : '#27408B'})
        
        self.mark_c = self.F2.axes.text(1, 500000, '',
                                    color = '#1C86EE',
                                    style = 'oblique',
                                    size = '24',
                                    ha = 'center',
                                    va = 'center')
        
        
        self.mark_d = self.F2.axes.text(1, 500000, '',
                                    color = '#EE0000',
                                    style = 'oblique',
                                    size = '24',
                                    ha = 'center',
                                    va = 'center')
                                            
        self.F2.axes.spines['right'].set_visible(False)
        self.F2.axes.spines['top'].set_visible(False)   
                                 
        self.F2.axes.set_xlabel('Date')
        self.F2.axes.set_ylabel('Cured or Death')
        self.F2.mpl_connect('motion_notify_event', self.onmove2)
        
    def plotStateCases(self):
        read = csv_read('time_series_covid_19_confirmed_US.csv')
        state_cases = read.states_death()
        x = 0
        for item in state_cases:
            if item[1] > 0:
                self.F3.axes.barh(item[0], item[1])
                self.F3.axes.text(item[1]*1.05, x - 0.3, item[1],
                                  size = 'large')
                x += 1
        self.F3.axes.set_xscale('log')
        self.F3.axes.set_xlabel('Confirmed')
        
        self.F3.axes.spines['right'].set_visible(False)
        self.F3.axes.spines['top'].set_visible(False)
        
        self.F3.axes.set_title("Only showing the states having confirmed cases", 
                               size = 'x-large')
        self.F3.fig.suptitle("Confirmed Cases of States", size = 'xx-large')

    def plotWorldConfi(self):
        read = csv_read('time_series_covid_19_confirmed.csv')
        cases, time, max_case = read.all_confi()
        x_locat = MultipleLocator(5)
        self.F4.axes.xaxis.set_major_locator(x_locat)
        for key, value in cases.items():
            self.F4.axes.plot(time, value,
                              label = key,
                              marker = '.',
                              alpha = 0.5)
        # self.F4.axes.set_yscale('log')
        self.con_cases = cases
        self.con_time = time
        self.F4.axes.legend()
        self.F4.fig.suptitle("Confirmed Cases by Country", size = 'xx-large')
        self.F4.axes.set_title("Showing confirmed cases in US, China, "+
                               'Spain and Italy', 
                               size = 'x-large')
        self.F4.axes.set_xlabel('Date')
        self.F4.axes.set_ylabel('Cases')
        self.num_cha = self.F4.axes.text(3, max_case*0.7, '',
                                    color = '#1F77B4',
                                    style = 'oblique',
                                    size = 'large',
                                    ha = 'center',
                                    bbox = {'facecolor' : 'white',
                                            'alpha' : 0.75,
                                            'edgecolor' : '#1F77B4'})
                                            
        self.num_us = self.F4.axes.text(18, max_case*0.7, '',
                                    color = '#FF7F0E',
                                    style = 'oblique',
                                    size = 'large',
                                    ha = 'center',
                                    bbox = {'facecolor' : 'white',
                                            'alpha' : 0.75,
                                            'edgecolor' : '#FF7F0E'})
                                            
        self.num_sp = self.F4.axes.text(3, max_case*0.5, '',
                                    color = '#2CA02C',
                                    style = 'oblique',
                                    size = 'large',
                                    ha = 'center',
                                    bbox = {'facecolor' : 'white',
                                            'alpha' : 0.75,
                                            'edgecolor' : '#2CA02C'})
                                            
        self.num_it = self.F4.axes.text(18, max_case*0.5, '',
                                    color = '#D62728',
                                    style = 'oblique',
                                    size = 'large',
                                    ha = 'center',
                                    bbox = {'facecolor' : 'white',
                                            'alpha' : 0.75,
                                            'edgecolor' : '#D62728'})                                    
        self.F4.mpl_connect('motion_notify_event', self.onmove4)
    
    
    def plotWorldDeath(self):
        read = csv_read('time_series_covid_19_deaths.csv')
        death, time, max_case = read.all_confi()
        x_locat = MultipleLocator(5)
        self.F5.axes.xaxis.set_major_locator(x_locat)
        for key, value in death.items():
            self.F5.axes.plot(time, value,
                              label = key,
                              marker = '.',
                              alpha = 0.5)
        # self.F4.axes.set_yscale('log')
        self.con_death = death
        self.F5.axes.legend()
        self.F5.fig.suptitle("Death Cases by Country", size = 'xx-large')
        self.F5.axes.set_title("Showing Death cases in US, China, "+
                               'Spain and Italy', 
                               size = 'x-large')
        self.F5.axes.set_xlabel('Date')
        self.F5.axes.set_ylabel('Death')
        self.dea_cha = self.F5.axes.text(3, max_case*0.7, '',
                                    color = '#1F77B4',
                                    style = 'oblique',
                                    size = 'large',
                                    ha = 'center',
                                    bbox = {'facecolor' : 'white',
                                            'alpha' : 0.75,
                                            'edgecolor' : '#1F77B4'})
                                            
        self.dea_us = self.F5.axes.text(18, max_case*0.7, '',
                                    color = '#FF7F0E',
                                    style = 'oblique',
                                    size = 'large',
                                    ha = 'center',
                                    bbox = {'facecolor' : 'white',
                                            'alpha' : 0.75,
                                            'edgecolor' : '#FF7F0E'})
                                            
        self.dea_sp = self.F5.axes.text(3, max_case*0.5, '',
                                    color = '#2CA02C',
                                    style = 'oblique',
                                    size = 'large',
                                    ha = 'center',
                                    bbox = {'facecolor' : 'white',
                                            'alpha' : 0.75,
                                            'edgecolor' : '#2CA02C'})
                                            
        self.dea_it = self.F5.axes.text(18, max_case*0.5, '',
                                    color = '#D62728',
                                    style = 'oblique',
                                    size = 'large',
                                    ha = 'center',
                                    bbox = {'facecolor' : 'white',
                                            'alpha' : 0.75,
                                            'edgecolor' : '#D62728'})                                    
        self.F5.mpl_connect('motion_notify_event', self.onmove5)
    
    
    def plotWorldRate(self):
        x_locat = MultipleLocator(5)
        self.F6.axes.xaxis.set_major_locator(x_locat)
        cases = self.con_cases
        death = self.con_death
        time = self.con_time
        self.rate = {}
        for key, case in cases.items():
            i = 0
            self.rate[key] = []
            for dea in death[key]:
                if not case[i]:
                    self.rate[key].append(0)
                    i += 1 
                else:
                    self.rate[key].append(int(dea)*100/int(case[i]))
                    i += 1
                    
        
        for key, value in self.rate.items():
            self.F6.axes.plot(time, value,
                              label = key,
                              marker = '.',
                              alpha = 0.5)
        # self.F4.axes.set_yscale('log')
        self.F6.axes.legend()
        self.F6.fig.suptitle("Death Rate by Country", size = 'xx-large')
        self.F6.axes.set_title("Showing death rate in US, China, "+
                               'Spain and Italy', 
                               size = 'x-large')
        self.F6.axes.set_xlabel('Date')
        self.F6.axes.set_ylabel('Death rate%')
        self.rea_cha = self.F6.axes.text(3, 14*0.7, '',
                                    color = '#1F77B4',
                                    style = 'oblique',
                                    size = 'large',
                                    ha = 'center',
                                    bbox = {'facecolor' : 'white',
                                            'alpha' : 0.75,
                                            'edgecolor' : '#1F77B4'})
                                            
        self.rea_us = self.F6.axes.text(18, 14*0.7, '',
                                    color = '#FF7F0E',
                                    style = 'oblique',
                                    size = 'large',
                                    ha = 'center',
                                    bbox = {'facecolor' : 'white',
                                            'alpha' : 0.75,
                                            'edgecolor' : '#FF7F0E'})
                                            
        self.rea_sp = self.F6.axes.text(3, 14*0.5, '',
                                    color = '#2CA02C',
                                    style = 'oblique',
                                    size = 'large',
                                    ha = 'center',
                                    bbox = {'facecolor' : 'white',
                                            'alpha' : 0.75,
                                            'edgecolor' : '#2CA02C'})
                                            
        self.rea_it = self.F6.axes.text(18, 14*0.5, '',
                                    color = '#D62728',
                                    style = 'oblique',
                                    size = 'large',
                                    ha = 'center',
                                    bbox = {'facecolor' : 'white',
                                            'alpha' : 0.75,
                                            'edgecolor' : '#D62728'})                                    
        self.F6.mpl_connect('motion_notify_event', self.onmove6)
        
    
# main function of combining and showing graph        
class MainDialogImgBW(QDialog,Ui_Dialog):
    def __init__(self):
        super(MainDialogImgBW,self).__init__()
        self.setupUi(self)
        self.setWindowTitle('COVID')
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint | Qt.WindowMaximizeButtonHint)
        
        self.figures = []
        self.F = MyFigure(width=3, height=2, dpi=120)
        self.figures.append(self.F)
        for i in range(1, 7):
            exec('self.F{} = MyFigure(width=3, height=2, dpi=120)'.format(i))
            exec('self.figures.append(self.F{})'.format(i))
        print(self.figures)
        # initial the figure of death and cured

        
        # make a trigger for the buttons which deployed in pyqt5 GUI class
        # ex. if the button1 is clicked, the function btnstate() will be called
        self.button1.clicked.connect(self.btnstate)
        self.button2.clicked.connect(self.btnstate2)
        self.button3.clicked.connect(self.btnstate3)
        self.button4.clicked.connect(self.btnstate4)
        self.button5.clicked.connect(self.btnstate5)
        self.button6.clicked.connect(self.btnstate6)
        self.button7.clicked.connect(self.btnstate7)
        
        # connect with the GroupBox in the GUI
        self.gridlayout = QGridLayout(self.groupBox)
        
        # call and generate the graphs
        Graphs.plotdeatharea(self)
        Graphs.plotcase(self)
        Graphs.plotdeathcured(self)
        Graphs.plotStateCases(self)
        Graphs.plotWorldConfi(self)
        Graphs.plotWorldDeath(self)
        Graphs.plotWorldRate(self)
        
        # add graphs into the GroupBox
        self.gridlayout.addWidget(self.F6, 0, 1)
        self.gridlayout.addWidget(self.F5, 0, 1)
        self.gridlayout.addWidget(self.F4, 0, 1)
        self.gridlayout.addWidget(self.F3, 0, 1)
        self.gridlayout.addWidget(self.F2, 0, 1)
        self.gridlayout.addWidget(self.F1, 0, 1)
        self.gridlayout.addWidget(self.F, 0, 1)
        
        
        # hide the graphs at begining
        for figure in self.figures:
            figure.hide()
            
    # if the button1 is clicked, show the graph of cases&time and hide others
    def btnstate(self):
        for figure in self.figures:
            figure.hide()
        self.figures[0].show()

    # button2, show F2 hide others
    def btnstate2(self):
        for figure in self.figures:
            figure.hide()
        self.figures[1].show()
    # button3       
    def btnstate3(self):
        for figure in self.figures:
            figure.hide()
        self.figures[2].show()
        
    def btnstate4(self):
        for figure in self.figures:
            figure.hide()
        self.figures[3].show()
    
    def btnstate5(self):
        for figure in self.figures:
            figure.hide()
        self.figures[4].show()

    def btnstate6(self):
        for figure in self.figures:
            figure.hide()
        self.figures[5].show()

    def btnstate7(self):
        for figure in self.figures:
            figure.hide()
        self.figures[6].show()
            
    # when program detected mouse movement on F(cases&time graph)
    def onmove(self, event):
        x = 0
        try:
            x = float(event.xdata) #, int(float(event.ydata))
            if x > -1:
                case1 = self.cases[int(x)]
                if x > 1:
                    case0 = self.cases[int(x)]-self.cases[int(x-1)]
                    self.num.set_text('Date:{}\nCases:{}\n+{}'.format(
                                        self.time[int(x)],
                                        case1,
                                        case0))
                else:
                    self.num.set_text('Date:{}\nCases:{}'.format(
                                        self.time[int(x)],
                                        case1))
                    
                self.num.set_x(round(int(x)))
                self.num.set_y(int(self.cases[int(x)])+50000)
                self.mark.set_text('+')
                self.mark.set_x(round(int(x)))
                self.mark.set_y(int(self.cases[int(x)]))
                self.F.draw()
                # print('Day:{}, Cases:{}'.format(round(x), self.cases[int(x)]))
        except:
            pass
    # movement on F2(death&cured graph)   
    def onmove2(self, event):
        x = 0
        try:
            x = float(event.xdata) #, int(float(event.ydata))
            if x > -1:
                death1 = self.death[int(x)]
                cured1 = self.cured[int(x)]
                if x > 1:   
                    death0 = self.death[int(x)]-self.death[int(x-1)]
                    cured0 = self.cured[int(x)]-self.cured[int(x-1)]
                    self.num_dea.set_text('Date:{}\nDeath:{}\n+{}'.format(
                                        self.timedeath[int(x)],
                                        death1,
                                        death0))
                    self.num_cur.set_text('Date:{}\nCured:{}\n+{}'.format(
                                        self.timedeath[int(x)],
                                        cured1,
                                        cured0))
                else:
                    self.num_dea.set_text('Date:{}\nDeath:{}'.format(
                                        self.timedeath[int(x)],
                                        death1))
                    self.num_cur.set_text('Date:{}\nCured:{}'.format(
                                        self.timedeath[int(x)],
                                        cured1))
                    
                self.num_dea.set_x(round(int(x)))
                self.num_dea.set_y(int(self.death[int(x)])-5000)
                self.mark_d.set_text('+')
                self.mark_d.set_x(round(int(x)))
                self.mark_d.set_y(int(self.death[int(x)]))
                
                self.num_cur.set_x(round(int(x)))
                self.num_cur.set_y(int(self.cured[int(x)])+2500)
                self.mark_c.set_text('+')
                self.mark_c.set_x(round(int(x)))
                self.mark_c.set_y(int(self.cured[int(x)]))                
                self.F2.draw()
                # print('Day:{}, Cases:{}'.format(round(x), self.cases[int(x)]))
        except:
            pass
        
    def onmove4(self, event):
        x = 0
        try:
            x = float(event.xdata)
            if x > -1:
                self.num_cha.set_text('China\nDate:{}\nCases:{}'.format(
                                            self.con_time[int(x)],
                                            self.con_cases['China'][int(x)]))
                self.num_us.set_text('United States\nDate:{}\nCases:{}'.format(
                                            self.con_time[int(x)],
                                            self.con_cases['US'][int(x)]))
                self.num_sp.set_text('Spain\nDate:{}\nCases:{}'.format(
                                            self.con_time[int(x)],
                                            self.con_cases['Spain'][int(x)]))
                self.num_it.set_text('Italy\nDate:{}\nCases:{}'.format(
                                            self.con_time[int(x)],
                                            self.con_cases['Italy'][int(x)]))
                self.F4.draw()
        except:
            pass
        
    def onmove5(self, event):
        x = 0
        try:
            x = float(event.xdata)
            if x > -1:
                self.dea_cha.set_text('China\nDate:{}\nDeath:{}'.format(
                                            self.con_time[int(x)],
                                            self.con_death['China'][int(x)]))
                self.dea_us.set_text('United States\nDate:{}\nDeath:{}'.format(
                                            self.con_time[int(x)],
                                            self.con_death['US'][int(x)]))
                self.dea_sp.set_text('Spain\nDate:{}\nDeath:{}'.format(
                                            self.con_time[int(x)],
                                            self.con_death['Spain'][int(x)]))
                self.dea_it.set_text('Italy\nDate:{}\nDeath:{}'.format(
                                            self.con_time[int(x)],
                                            self.con_death['Italy'][int(x)]))
                self.F5.draw()
        except:
            pass


    def onmove6(self, event):
        x = 0
        try:
            x = float(event.xdata)
            if x > -1:
                self.rea_cha.set_text('China\nDate:{}\nRate:{:.2f}%'.format(
                                            self.con_time[int(x)],
                                            self.rate['China'][int(x)]))
                self.rea_us.set_text('United States\nDate:{}\nRate:{:.2f}%'.format(
                                            self.con_time[int(x)],
                                            self.rate['US'][int(x)]))
                self.rea_sp.set_text('Spain\nDate:{}\nRate:{:.2f}%'.format(
                                            self.con_time[int(x)],
                                            self.rate['Spain'][int(x)]))
                self.rea_it.set_text('Italy\nDate:{}\nRate:{:.2f}%'.format(
                                            self.con_time[int(x)],
                                            self.rate['Italy'][int(x)]))
                self.F6.draw()
        except:
            pass

# main function
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainDialogImgBW()
    executor = ThreadPoolExecutor(max_workers=8)
    main.show()
    #app.installEventFilter(main)
    sys.exit(app.exec_())