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

continousVars = ['POORHLTH', 'SLEPTIM1', 'AVEDRNK2', 'MAXDRNKS']
categoricalVars = ['SMOKE100', 'GENHLTH', 'SMOKDAY2','_STATE', 'EXERANY2', 'SEX']