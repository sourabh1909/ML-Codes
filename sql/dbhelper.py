import mysql.connector

class DB:
    def __init__(self):
        # connect database
        try:
            self.conn = mysql.connector.connect(
                host='127.0.0.1', # 127.0.1.1
                port = 3300,
                user = 'root',
                password ='sourabh',
                database = 'flights'
            )
            self.mycursor = self.conn.cursor()
            print('connection establish')
        except:
            print('connection error')
            
    def fetch_city_names(self):
        city = []
        
        self.mycursor.execute("""
            SELECT distinct(DESTINATION) FROM flights.flights
            UNION
            SELECT distinct(source) FROM flights.flights
                              """)
        
        data = self.mycursor.fetchall()
        
        for item in data:
            city.append(item[0])
            
        return city
    
    def fetch_all_flights(self,source,destination):
        self.mycursor.execute("""
        SELECT airline, route, dep_time, duration, price 
        FROM flights
        WHERE source = %s AND destination = %s
    """, (source, destination))
        
        data = self.mycursor.fetchall()
        return data
    
    def fetch_airline_ferq(self):
        
        airline = []
        freq =[]
        
        self.mycursor.execute("""
            select airline,count(*) from flights
            group by airline                  
                              """)
        
        data = self.mycursor.fetchall()
        
        for item in data:
            airline.append(item[0])
            freq.append(item[1])
            
        return airline,freq
    
    def busy_airport(self):
        city = [] 
        freq = []
        
        self.mycursor.execute("""
            select source,count(*) from (
            select source from flights
            union all
            select destination from flights
            ) t

            group by t.source
            order by count(*) desc
                              """)
        
        data = self.mycursor.fetchall()
        
        for item in data:
            city.append(item[0])
            freq.append(item[1])
            
        return city,freq
    
    def daily_freq(self):
        date = [] 
        freq1 = []
        
        self.mycursor.execute("""
            select date_of_journey, count(*) from flights
            group by date_of_journey                  
            """)
        
        data = self.mycursor.fetchall()
        
        for item in data:
            date.append(item[0])
            freq1.append(item[1])
            
        return date,freq1
    
    def flights_analysis(self):
        air=[]
        price=[]
        
        
        
        data = self.mycursor.fetchall()
        return data
    
    