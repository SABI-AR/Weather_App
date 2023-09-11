import streamlit as st
import  requests

API_KEY = "7835e2721b70b23398c7d5a8be887fb4"

def convert_to_celsius(temperature_to_kelvin):
    return temperature_to_kelvin -273.15


def Find_Current_Weather(city):
    base_url= f"https://api.openweathermap.org/data/2.5/weather?q={city }&appid={API_KEY}"
    weather_data = requests.get(base_url).json()
    
    try:
        general = weather_data['weather'][0]['main']
        icon_id = weather_data['weather'][0]['icon']
        temperature = round(convert_to_celsius(weather_data['main']['temp']))
        icon = f" https://openweathermap.org/img/wn/{icon_id}@2x.png"
    except KeyError:
        st.error("City Not Found")
        st.stop
    return general,temperature,icon
    

def main():
    st.header("Find the weather")
    city=st.text_input("Enter the ciity").lower()
    if st.button("Find"):
        general,Temperature,icon = Find_Current_Weather(city)
        col_1,col_2 = st.columns(2)
        with col_1:
            st.metric(label= "Temperature",value=f"{Temperature}°C")
        with col_2:
            st.write(general)
            st.image(icon)
  

    




if __name__ == '__main__':
    main()