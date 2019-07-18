'''
UserPatternAnalysis.py
 Title: Analyze user patterns using Data(instacart-market-basket-analysis/Kaggle)
'''
# install Library List
## pip3 install pandas
## pip3 install numpy
## pip3 install matplotlib

# import Library
## 전처리 관련 클래스
import Preprocessing
## 분석 및 시각화 관련 클래스
import DataAnalysis

# 클래스 선언
prepro = Preprocessing.Preprocessing()
analysis = DataAnalysis.DataAnalysis()

# 전처리 실행
## num: 전처리(공백 or -1), 전처리 및 저장(0), 샘플링 데이터 가져오기(1)
## user: 저장 시 유저 카운트 지정
data = prepro.run(num = 1)

# 분석 및 시각화 실행
analysis.run()
