dataDictionary = {
  'SMOKE100': {
    '': 'missing',
    '1': 'smoker',
    '2': 'never smoked',
    '7': "don't know",
    '9': 'refused'
  },
  'GENHLTH' : {
    '': 'missing',
    '1': 'excellent',
    '2': 'very good',
    '3': 'good',
    '4': 'fair',
    '5': 'poor',
    '7': "don't know",
    '9': 'refused'
    },
  'POORHLTH' : {
    '': 'missing',
    '88': 0,
    '77': "don't know",
    '99': 'refused'
    },
  'EXERANY2' : {
    '' : 'missing',
    '1': 'yes',
    '2': 'no',
    '7': "don't know",
    '9': 'refused'
    },
  'SLEPTIM1' : {
    '': 'missing',
    '77': "don't know",
    '99': 'refused'
  },
  'SEX' : {
    '1': 'male',
    '2': 'female',
  },
  'SMOKDAY2' : {
    '': 'missing',
    '1': 'every day',
    '2': 'some days',
    '3': 'not at all',
    '7': "don't know",
    '9': 'refused'
  },
  'AVEDRNK2' : {
     '': 'missing',
    '77': "don't know",
    '99': 'refused'
  },
  'MAXDRNKS'  : {
     '': 'missing',
    '77': "don't know",
    '99': 'refused'
  },
  "_STATE" : {
    '9': 'CT',
    '37': 'NC'
  }
}

continuousVars = ['POORHLTH', 'SLEPTIM1', 'AVEDRNK2', 'MAXDRNKS']
categoricalVars = ['SMOKE100', 'GENHLTH', 'SMOKDAY2','_STATE', 'EXERANY2', 'SEX']

varQuestion = {
  'SMOKE100': 'Have you smoked at least 100 cigarettes in your entire life?', 
  'GENHLTH' : 'Would you say that in general your health is',
  'POORHLTH': 'During the past 30 days, for about how many days did poor physical or mental health keep you from doing your usual activities, such as self-care, work, or recreation?',
  'EXERANY2': 'During the past month, other than your regular job, did you participate in any physical activities or exercises such as running, calisthenics, golf, gardening, or walking for exercise?',
  'SLEPTIM1': 'On average, how many hours of sleep do you get in a 24-hour period?',
  'SEX' : 'Sex of respondent',
  'SMOKDAY2' : 'Do you now smoke cigarettes every day, some days, or not at all?',
  'AVEDRNK2' : 'One drink is equivalent to a 12-ounce beer, a 5-ounce glass of wine, or a drink with one shot of liquor. During the past 30 days, on the days when you drank, about how many drinks did you drink on the average?',
  'MAXDRNKS' : 'During the past 30 days, what is the largest number of drinks you had on any occasion?' ,
  "_STATE" : 'State where respondent lives'
  }