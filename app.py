import pandas as pd
import sklearn , pickle
from flask import render_template, Flask , request
from flask_cors import cross_origin




app = Flask(__name__)
model = pickle.load(open("flight_rf.pkl", "rb"))

@app.route("/")
@cross_origin()
def home():
    return render_template("index.html")



@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":

        
        
        date_departure = request.form["Dep_Time"]
        Month_of_Journey = int(pd.to_datetime(date_departure, format ="%Y-%m-%dT%H:%M").month)
        Day_of_Journey = int(pd.to_datetime(date_departure, format="%Y-%m-%dT%H:%M").day)
        # Departure
        Departure_hour = int(pd.to_datetime(date_departure, format ="%Y-%m-%dT%H:%M").hour)
        Departure_minute = int(pd.to_datetime(date_departure, format ="%Y-%m-%dT%H:%M").minute)
       

        # Arrival
        date_arrival = request.form["Arrival_Time"]
        Arrival_hour = int(pd.to_datetime(date_arrival, format ="%Y-%m-%dT%H:%M").hour)
        Arrival_min = int(pd.to_datetime(date_arrival, format ="%Y-%m-%dT%H:%M").minute)
        
        # Date_of_Journey
       
        

        

        # Total Stops
        Total_stops = int(request.form["stops"])
        
        # Duration
        duration_hour = abs(Arrival_hour - Departure_hour)
        duration_min = abs(Arrival_min - Departure_minute)
       
        
        

        # Airline
        # AIR ASIA = 0 (not in column)
        airline=request.form['airline']
        if (airline=='IndiGo'):
            JA = 0
            Indigo = 1
            AI = 0
            MC = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            MCPE = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0 

        

        

        elif (airline=='Air India'):
            #AI will be one rest will be zero 
            Vistara = 0
            GoAir = 0
            MCPE = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0 
            JA = 0
            Indigo = 0
            AI = 1
            MC = 0
            SpiceJet = 0
            
             
            
        elif (airline =='SpiceJet'):
            Vistara = 0
            GoAir = 0
            MCPE = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0
            JA = 0
            Indigo = 0
            AI = 0
            MC = 0
            SpiceJet = 1
            

      
            
        elif (airline=='Vistara'):
            Vistara = 1
            SpiceJet = 0
            GoAir = 0
            MCPE = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0
            JA = 0
            Indigo = 0
            AI = 0
            MC = 0

        elif (airline=='Jet Airways Business'):
            SpiceJet = 0
            Vistara = 0
            Jet_Airways_Business = 1
            GoAir = 0
            MCPE = 0
            Vistara_Premium_economy = 0
            Trujet = 0 
            JA = 0
            Indigo = 0
            AI = 0
            MC = 0
            

        elif(airline=='Jet Airways'):
            Trujet = 0 
            Vistara = 0
            GoAir = 0
            MCPE = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
           
            #Jet Airways will be one rest will be 0
            JA = 1
            Indigo = 0
            AI = 0
            MC = 0
            SpiceJet = 0
                

        elif (airline=='GoAir'):
            SpiceJet = 0
            Vistara = 0
            GoAir = 1
            JA = 0
            Indigo = 0
            AI = 0
            MCPE = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0
            MC = 0
            
            

        elif (airline=='Multiple carriers Premium economy'):
            MCPE = 1
            Vistara = 0
            GoAir = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0
            JA = 0
            Indigo = 0
            AI = 0
            MC = 0
            SpiceJet = 0
            

        elif (airline=='Trujet'):
            Trujet = 1
            MCPE = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            JA = 0
            Indigo = 0
            AI = 0
            MC = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0

        

        elif (airline=='Vistara Premium economy'):
            Vistara_Premium_economy = 1
            MCPE = 0
            Jet_Airways_Business = 0
            JA = 0
            Indigo = 0
            AI = 0
            MC = 0
            Vistara = 0
            GoAir = 0
            Trujet = 0
            SpiceJet = 0
            
            
        elif (airline=='Multiple carriers'):
            MC = 1
            MCPE = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            JA = 0
            Indigo = 0
            AI = 0
            

        else:
            Vistara_Premium_economy = 0
            JA = 0
            Indigo = 0
            Vistara = 0
            GoAir = 0
            MCPE = 0
            Jet_Airways_Business = 0
            AI = 0
            MC = 0
            SpiceJet = 0
            Trujet = 0
            
            

        
        # Source
        # Banglore = 0 (not in column)
        Source = request.form["Source"]
        if (Source == 'Delhi'):
            Kolkata = 0
            Mumbai = 0
            Madras = 0
            Delhi = 1
            

        elif (Source == 'Chennai'):
            Kolkata = 0
            Mumbai = 0
            Delhi = 0
            Madras = 1

        

        elif (Source == 'Mumbai'):
            Mumbai = 1
            Delhi = 0
            Kolkata = 0
            Madras = 0

        
        elif (Source == 'Kolkata'):
            Kolkata = 1
            Mumbai = 0
            Madras = 0
            Delhi = 0
            

        else:

            Mumbai = 0
            Madras = 0
            Delhi = 0
            Kolkata = 0

        

        # Destination
        # Banglore = 0 (not in column)
        Source = request.form["Destination"]
        if (Source == 'Cochin'):
            Hyderabad_d = 0
            Kolkata_d = 0
            Cochin_d = 1
            Delhi_d = 0
            NewDelhi_d = 0
            
            
        
        elif (Source == 'Delhi'):
            Cochin_d = 0
            NewDelhi_d = 0
            Hyderabad_d = 0
            Kolkata_d = 0
            Delhi_d = 1
            

        elif (Source == 'New_Delhi'):
            NewDelhi_d = 1
            Delhi_d = 0
            Hyderabad_d = 0
            Kolkata_d = 0
            Cochin_d = 0
            

        elif (Source == 'Hyderabad_d'):
            Kolkata_d = 0
            Cochin_d = 0
            NewDelhi_d = 0
            Hyderabad_d = 1
            Delhi_d = 0
            

        elif (Source == 'Kolkata'):
            Hyderabad_d = 0
            NewDelhi_d = 0
            Kolkata_d = 1
            Cochin_d = 0
            Delhi_d = 0

        else:
            Cochin_d = 0
            Delhi_d = 0
            NewDelhi_d = 0
            Hyderabad_d = 0
            Kolkata_d = 0

        
        
        
        pred=model.predict([[
            Departure_hour,
            Departure_minute,
            Arrival_hour,
            MCPE,
            SpiceJet,
            Trujet,
            Vistara,
            Vistara_Premium_economy,
            Arrival_min,
            Total_stops,
            Day_of_Journey,
            Month_of_Journey,
            duration_hour,
            duration_min,
            Madras,
            Delhi,
            Kolkata,
            Mumbai,
            Cochin_d,
            Delhi_d,
            Hyderabad_d,
            Kolkata_d,
            NewDelhi_d,
            AI,
            GoAir,
            Indigo,
            JA,
            Jet_Airways_Business,
            MC,
            
            
        ]])

        result =round(pred[0],2)

        return render_template('index.html',prediction_text="Your Flight ticket price is Rs. {}".format(result ))


    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
