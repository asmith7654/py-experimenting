import pandas as pd
#simplify paths
path_12_13_result = '/Users/Drew/Downloads/archive/2012-13/raw_scores.txt'
path_12_13_bet = '/Users/Drew/Downloads/archive/2012-13/vegas.txt'

#create dataframes from txt files
df_12_13_result = pd.read_csv(path_12_13_result, sep=',')
df_12_13_bet = pd.read_csv(path_12_13_bet, sep=',')
df_12_13_bet_ml = df_12_13_bet.iloc[:,list(range(16)) + [56]]
df_12_13_bet_ml_pin = df_12_13_bet_ml.iloc[:,[5]+[8]+[14]+[16]]

#translate odds
def amerToDec(odds):
    if(odds >0):
        decimal = (odds/100) + 1
    else:
        decimal = (100/abs(odds)) + 1
    
    return decimal

def decToAmer(odds):
    if(odds>=2):
        american = 100*(odds-1)
    else:
        american = -100/(odds-1)
    
    return american


#if best odds are better than pinnacle, keep row
df_12_13_bet_ml_pin_placed = df_12_13_bet_ml_pin[ df_12_13_bet_ml_pin['Best_Line_ML'] > df_12_13_bet_ml_pin['Pinnacle_ML'] ]

# Add the columns as decimal odds
df_12_13_bet_ml_pin_placed['Pinnacle_ML_decimal'] = df_12_13_bet_ml_pin_placed['Pinnacle_ML'].apply(amerToDec)
df_12_13_bet_ml_pin_placed['Best_Line_ML_decimal'] = df_12_13_bet_ml_pin_placed['Best_Line_ML'].apply(amerToDec)


#create EV column in placed bets df
df_12_13_bet_ml_pin_placed['EV'] = (( 1 / df_12_13_bet_ml_pin_placed['Pinnacle_ML_decimal']))*(df_12_13_bet_ml_pin_placed['Best_Line_ML_decimal'] - 1) + ((1 - (1/df_12_13_bet_ml_pin_placed['Pinnacle_ML_decimal']))*(-1))

#create dataframe of just winning bets
df_12_13_bet_ml_pin_won = df_12_13_bet_ml_pin_placed[df_12_13_bet_ml_pin_placed.iloc[:,3] == 'W']

#calculate roi and expected roi
betsPlaced = df_12_13_bet_ml_pin_placed.shape[0]
profit = df_12_13_bet_ml_pin_won['Best_Line_ML_decimal'].sum()
net = profit - betsPlaced
roi = net/betsPlaced
expected_roi = df_12_13_bet_ml_pin_placed['EV'].sum()/betsPlaced




