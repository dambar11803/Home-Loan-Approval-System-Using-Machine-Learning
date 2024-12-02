from joblib import load 
import joblib
from django.shortcuts import render
import numpy as np
from .forms import ClientDetailsForm 
from .models import ClientDetails 
import math
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.ensemble import RandomForestClassifier
from scipy.stats import randint, uniform

from django.contrib.staticfiles.storage import staticfiles_storage

model = joblib.load('static/RandomForest.joblib')
   
def Predictloan(request):
    emi = 0.0
    IncomeToEmi = HomeToLoanAmount = 0
    tenure = 0
    result= "preview"
    form = ClientDetailsForm()
    if request.method == 'POST':
        name = request.POST.get('name')
        Gender = request.POST.get('sex')
        MartialStatus = request.POST.get('martial')
        age = int(request.POST.get('age'))
        ClientIncome = float(request.POST.get('salary'))
        FamilyIncome = float(request.POST.get('family_income'))
        HomeValue = float(request.POST.get('home_value'))
        LoanAmount = float(request.POST.get('loan_amount'))
        period = int(request.POST.get('tenure'))
        interest = float(request.POST.get('interest'))

        TotalIncome = ClientIncome+FamilyIncome
        TotalIncome = float(TotalIncome)
        TotalIncome = round(TotalIncome, 2)
        totalincome = TotalIncome
        
        #Calculaton of Emi
        p= LoanAmount 
        t = period
        t = t*12
        r = interest
        r = r/1200
        r1 = (1+r)
        r1 = math.exp(math.log(r1) * t)
        a = p*r*r1
        b = r1-1
        Emi = int(a/b)
       
        #Add New Features
        IncomeToEmi = TotalIncome / Emi
        HomeToLoanAmount = HomeValue / LoanAmount 
        maxloan = 0.7 * HomeValue
        maxloan = round(maxloan, 2)
        
        if period == 10:  
            Tenure = 0 
        else:
            Tenure = 1    
            
        #Saving Data in other variable
        homevalue = HomeValue
        loanamount = LoanAmount
        emi = Emi
        incometoemi = IncomeToEmi 
        hometoloan = HomeToLoanAmount 
        
        #Apply Log Transformation
        HomeValue = np.log1p(HomeValue)
        LoanAmount = np.log1p(LoanAmount)
        Emi = np.log1p(Emi)
        TotalIncome = np.log1p(TotalIncome)
        IncomeToEmi = np.log1p(IncomeToEmi)
        HomeToLoanAmount = np.log1p(HomeToLoanAmount)
        
        #Features Selection for Target Prediction
        features = [[HomeValue, LoanAmount, Emi, Tenure, TotalIncome, IncomeToEmi, HomeToLoanAmount]]
        
        #Make the Prediction
        prediction = model.predict(features)
        result = 'Approved' if prediction[0] == 1 else 'Rejected'
        
        #Create Dictionary
        client_details = {
            'name': name,
            'age':age,
            'incometoemi':IncomeToEmi,
            'gender':Gender,
            'martial': MartialStatus,
            'homevalue':homevalue,
            'loanamount':loanamount,
            'emi':emi,
            'tenure': period,
            'hometoloan': HomeToLoanAmount,
            'result':result,
            'maxloan':maxloan,
            'totalincome':totalincome,
        }

        return render(request, 'home.html', {'form':form, 'client':client_details})
    #else:
         #form = ClientDetailsForm()
    return render(request, 'home.html', {'form': form})
        
                    
  


