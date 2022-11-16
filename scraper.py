from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

# Enlace a NASA Exoplanet
START_URL = "https://exoplanets.nasa.gov/exoplanet-catalog/"

# Controlador web
browser = webdriver.Edge("D:/Setup/chromedriver_win32/msedgedriver.exe")
browser.get(START_URL)

time.sleep(10)

scarped_data = []

# Definir el método de extracción de datos para Exoplanet
def scrape():

    #Recorre 11 paginas de la table
    for i in range(0,10):
        print(f'Scrapping page {i+1} ...' )

        ## AGREGAR EL CÓDIGO AQUÍ ##
        #mando llamar BeautifulSoup para obtener la informacion de la pagina
        soup=BeautifulSoup(browser.page_source,"html.parser")
        #recorre las etiquetas ul
        for ul_tag in soup.find_all("table",attrs={"class","wikitable sortable jquery-tablesorter"}):
            bright_star_table=soup.find("table",attrs={"class","wikitable sortable jquery-tablesorter"})
            table_body=bright_star_table.find("tbody")
            table_rows=table_body.find_all("tr")
            
            for row in table_rows:
                table_cols=row.find_all("td")
                #print(table_cols)
                temp_list=[]

                for col_data in table_cols:
                    #print(col_data.text)

                    data=col_data.text.strip()
                    #print(data)

                    temp_list.append(data)
                
                scarped_data.append(temp_list)

stars_data=[]
for i in range (0.len(scarped_data)):
    Star_names=scarped_data[i][1]
    Distance=scarped_data[i][3]
    Mass=scarped_data[i][5]
    Radius=scarped_data[i][6]
    Lum=scarped_data[i][7]
    required_data=[Star_names,Distance,Mass,Radius,Lum]
    stars_data.append(required_data)

headers=["Star_name","Distance","Mass","Radius","Luminosity"]

star_df_1=pd.DataFrame(star_data,columns=headers)
star_df_1.to_csv("scraped_data.csv",index=True,index_label="id")

