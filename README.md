# Weather_Automation
here dt = Unix Timestamp which is a unique id 

Here two folder:
- Compile with json file 
- Compile with API link 

Json/API consist of data of weather forecast of London Location.



By extracting the data in the list 

- Using dt_txt as key to search with the date input

For temperature:
- Taking from "main" dictionary  finding temp "data['main']['temp']"
  
For wind:
- Taking from "wind" dictionary  finding speed "data['wind']['speed']"
  
For pressure:
- Taking from  "main" dictionary  finding pressure  "data['main']['pressure']"
