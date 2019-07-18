'''
UserPatternAnalysis.py
 Title: Analyze user patterns using Data(instacart-market-basket-analysis/Kaggle)
'''
# install Library List
## pip3 install pandas
## pip3 install numpy
## pip3 install matplotlib

# Import Library
## Data Preprocessing Classes
import Preprocessing
## Classes related to analysis and visualization
import DataAnalysis

# Class declaration
prepro = Preprocessing.Preprocessing()
analysis = DataAnalysis.DataAnalysis()

# Running Process
while True:
    print('Run Data PreProcessing ▶ 1')
    print('Run Analysis and Visualization ▶ 2')
    choice = int(input('Choose the Job:'))
    
    if choice == 1:
        # Run Data Preprocessing
        ## num: PreProcessing(-1), PreProcessing & Save(0), Read Sample Data(1)
        ## user: Specify user counts when saving
        n = int(input('PreProcessing(-1), PreProcessing & Save(0), Read Sample Data(1):'))
        if n not in [-1, 0, 1]:
            break
        u = 0
        if n == 0:
            u = int(input('User Count:'))

        data = prepro.run(num = n, user = u)
    elif choice == 2:
        # Run Analysis and Visualization
        analysis.run()
        break
    else:
        print('Re-Enter')
