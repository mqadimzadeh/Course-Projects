import numpy as np
import pandas as pd
from scipy.integrate import solve_ivp
from scipy.optimize import minimize
import matplotlib.pyplot as plt
from datetime import timedelta, datetime
import tkinter
import time
import requests
import tkinter as tk 
from tkinter import ttk 
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup as bs

START_DATE = {
  'Japan': '1/22/20',
  'Italy': '1/31/20',
  'Republic of Korea': '1/22/20',
  'Iran (Islamic Republic of)': '2/19/20'
}

class Learner(object):
    def __init__(self, country, loss, start_date, predict_range,s_0, i_0, r_0):
        self.country = country
        self.loss = loss
        self.start_date = start_date
        self.predict_range = predict_range
        self.s_0 = s_0-i_0-r_0
        self.i_0 = i_0
        self.r_0 = r_0


    def load_confirmed(self, country):
        df = pd.read_csv('data/time_series_19-covid-Confirmed.csv')
        country_df = df[df['Country/Region'] == country]
        return country_df.iloc[0].loc[self.start_date:]


    def load_recovered(self, country):
        df = pd.read_csv('data/time_series_covid19_recovered.csv')
        country_df = df[df['Country/Region'] == country]
        return country_df.iloc[0].loc[self.start_date:]


    def load_dead(self, country):
        df = pd.read_csv('data/time_series_covid19_deaths.csv')
        country_df = df[df['Country/Region'] == country]
        return country_df.iloc[0].loc[self.start_date:]
    

    def extend_index(self, index, new_size):
        values = index.values
        current = datetime.strptime(index[-1], '%m/%d/%y')
        while len(values) < new_size:
            current = current + timedelta(days=1)
            values = np.append(values, datetime.strftime(current, '%m/%d/%y'))
        return values
    

        


    def predict(self, beta, gamma, data, recovered, death, country, s_0, i_0, r_0):
        new_index = self.extend_index(data.index, self.predict_range)
        size = len(new_index)
        def SIR(t, y):
            S = y[0]
            I = y[1]
            R = y[2]
            return [-beta*S*I, beta*S*I-gamma*I, gamma*I]
        extended_actual = np.concatenate((data.values, [None] * (size - len(data.values))))
        extended_recovered = np.concatenate((recovered.values, [None] * (size - len(recovered.values))))
        extended_death = np.concatenate((death.values, [None] * (size - len(death.values))))
        return new_index, extended_actual, extended_recovered, extended_death, solve_ivp(SIR, [0, size], [s_0,i_0,r_0], t_eval=np.arange(0, size, 1))


    def train(self):

        recovered = self.load_recovered(self.country)
        death = self.load_dead(self.country)
        data = (self.load_confirmed(self.country) - recovered - death)
        
        optimal = minimize(loss, [0.001, 0.001], args=(data, recovered, self.s_0, self.i_0, self.r_0), method='L-BFGS-B', bounds=[(0.00000001, 0.4), (0.00000001, 0.4)])
        print(optimal)
        beta, gamma = optimal.x
        new_index, extended_actual, extended_recovered, extended_death, prediction = self.predict(beta, gamma, data, recovered, death, self.country, self.s_0, self.i_0, self.r_0)
        df = pd.DataFrame({'Infected data': extended_actual, 'Recovered data': extended_recovered, 'Death data': extended_death, 'Susceptible': prediction.y[0], 'Infected': prediction.y[1], 'Recovered': prediction.y[2]}, index=new_index)
        fig, ax = plt.subplots(figsize=(15, 10))
        ax.set_title(self.country)
        plt.ion()
        df.plot(ax=ax)
        plt.pause(0.0001)
        print(f"country={self.country}, beta={beta:.8f}, gamma={gamma:.8f}, r_0:{(beta/gamma):.8f}")
        fig.savefig(f"{self.country}.png")



def loss(point, data, recovered, s_0, i_0, r_0):
    size = len(data)
    beta, gamma = point
    def SIR(t, y):
        S = y[0]
        I = y[1]
        R = y[2]
        return [-beta*S*I, beta*S*I-gamma*I, gamma*I]
    solution = solve_ivp(SIR, [0, size], [s_0,i_0,r_0], t_eval=np.arange(0, size, 1), vectorized=True)
    l1 = np.sqrt(np.mean((solution.y[1] - data)**2))
    l2 = np.sqrt(np.mean((solution.y[2] - recovered)**2))
    alpha = 0.1
    return alpha * l1 + (1 - alpha) * l2



# =============================================================================
# ob = Learner("Japan", 0, '1/22/20', 150, 60000000, 1, 0)
# ob.train()
# =============================================================================

def callback():
    x = int(pop.get())
    while x > 6000:
        x = x / 10
    x = int(x)
    ob = Learner(countrychoosen.get(), 0, '1/22/20', 150, x, 1, 0)
    ob.train()

        
def update_data_callback():

    r = requests.get('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
    file = open('data/time_series_19-covid-Confirmed.csv','w')
    file.write(r.text)
    file.close()
    r = requests.get('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
    file = open('data/time_series_covid19_deaths.csv','w')
    file.write(r.text)
    file.close()
    r = requests.get('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv')
    file = open('data/time_series_covid19_recovered.csv','w')
    file.write(r.text)
    file.close()
    messagebox.showinfo("Notice", "All datasets updated!")



def pop_updater(country_name):
    r = requests.get('https://www.worldometers.info/world-population/' + country_name + '-population/')
    soup = bs(r.text, 'html.parser')
    x= soup.findAll("li")
    try:
        y = x[7].findAll("strong")
        return int(y[1].text.replace(",",""))
        
    except:
        y = x[8].findAll("strong")
        return int(y[1].text.replace(",",""))
    
def pop_value(eventObject):
    pop.delete("0",tk.END)
    name = countrychoosen.get()
    name = name.lower()
    population = pop_updater(name)
    pop.insert(0, str(population))
    
# Creating tkinter window 
window = tk.Tk() 
window.title('SIR Modeling') 
window.geometry('500x200') 


# label text for title 
ttk.Label(window, text = "SIR Toolbox Widget",  
          background = 'green', foreground ="white",  
          font = ("Times New Roman", 15)).grid(row = 0, column = 1) 
  
# label 
ttk.Label(window, text = "Select the Country :", 
          font = ("Times New Roman", 10)).grid(column = 0, 
          row = 5, padx = 10, pady = 25) 
ttk.Label(window, text = "country population :", 
          font = ("Times New Roman", 10)).grid(column = 0, 
          row = 7, padx = 10, pady = 25)                           
#Button                                               
ttk.Button(window,text="Update data",command = update_data_callback).place(x=400,y=150)
ttk.Button(window,text="Graph SIR",command = callback).place(x=300,y=150)

#Entries         
name = tk.StringVar()
pop = ttk.Entry(window, width = 15, textvariable = name)
pop.place(x=130,y=120)

# Combobox creation 
n = tk.StringVar() 
countrychoosen = ttk.Combobox(window, width = 40, textvariable = n)
update_data_callback()
df = pd.read_csv('data/time_series_19-covid-Confirmed.csv')
names = list(df['Country/Region'])
# Adding combobox drop down list 
countrychoosen['values'] = names
  
countrychoosen.grid(column = 1, row = 5)
countrychoosen.bind("<<ComboboxSelected>>",pop_value)


window.mainloop() 
